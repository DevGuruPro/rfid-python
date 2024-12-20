import os
import threading
import time
import uuid
from datetime import datetime
import tempfile

import pygame
import requests
import schedule
import json
import sqlite3
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from PySide6.QtCore import Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QHeaderView, QTableWidget, QTableWidgetItem, QPushButton, \
    QLabel, QSizePolicy

from settings import HEALTH_UPLOAD_URL, RECORD_UPLOAD_URL, LOGIN_URL
from ui.ui_main import Ui_MainWindow
from ui.wav_data import wav_data
from utils.commons import extract_from_gps, get_date_from_utc, find_gps_port, is_ipv4_address, \
    find_smallest_available_id, calculate_speed_bearing, convert_formatted_payload, pre_config_gps

from utils.gps import GPS
from utils.logger import logger
from utils.rfid import RFID
from widget.loadingDlg import LoadingDlg


class MainWnd(QMainWindow):
    main_closed = Signal()
    upload_record = Signal()

    def __init__(self, user_name, token, email, password):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        text_label = QLabel("Internet Connection Status : ", self)
        text_label.setGeometry(self.geometry().right() - 300, 15, 300, 30)
        text_label.setStyleSheet(u"QLabel{\n"
                                 "font-size: 10pt; /* Font size */\n"
                                 "font-weight: bold; /* Bold font */\n"
                                 "}")
        text_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        text_label.adjustSize()

        self.internet_label = QLabel("Connected", self)
        self.internet_label.setGeometry(self.geometry().right() - 300 + text_label.width(), 15, 80, 30)
        self.internet_label.setStyleSheet(u"QLabel {\n"
                                          "font-size: 10pt; /* Font size */\n"
                                          "color: green;\n"
                                          "}")
        self.internet_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        self.internet_label.adjustSize()

        logout_button = QPushButton("Logout", self)
        logout_button.setGeometry(400, 7, 50, 30)
        logout_button.setCursor(Qt.CursorShape.PointingHandCursor)
        logout_button.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
                                                  stop:0 #222222, stop:1 #aaaaaa);
                border: 2px solid white;
                border-radius: 10px;
                min-width: 80px;
                min-height: 30px;
                font-size: 10pt;
                font-weight: bold;
                color: white;
            }

            QPushButton:hover {
                background-color: #a0a0a0; /* Slightly different green on hover */
            }

            QPushButton:pressed {
                background-color: #909090; /* Darker green when pressed */
            }""")
        # Connect the button's clicked signal to a slot
        logout_button.clicked.connect(self.on_log_out)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.ui.tableWidget.setSelectionMode(QTableWidget.SelectionMode.NoSelection)

        # Fill the table with some data and make items non-editable
        for row in range(self.ui.tableWidget.rowCount()):
            for column in range(self.ui.tableWidget.columnCount()):
                item = QTableWidgetItem("")
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEditable &
                              ~Qt.ItemFlag.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, column, item)

        self.ui.radio_api_default.clicked.connect(self.select_api_type)
        self.ui.radio_api_custom.clicked.connect(self.select_api_type)
        self.ui.radio_api_both.clicked.connect(self.select_api_type)

        self.ui.radio_login_basic.clicked.connect(self.select_login_type)
        self.ui.radio_login_token.clicked.connect(self.select_login_type)

        self.ui.token_widget.hide()
        self.ui.custom_widget.hide()

        self.ui.edit_rfid_host.textChanged.connect(self.on_rfid_host_text_changed)
        self.ui.gps_checkBox.clicked.connect(self.on_gps_checked)
        self.ui.radio_external_gps.clicked.connect(self.on_gps_type)
        self.ui.radio_internet_gps.clicked.connect(self.on_gps_type)
        self.ui.setting_save_btn.released.connect(self.setting_save)
        self.ui.api_save_btn.released.connect(self.api_save)

        self.ui.speed_limit.clicked.connect(self.on_speed_check)
        self.ui.tag_limit.clicked.connect(self.on_tag_check)
        self.ui.rssi_limit.clicked.connect(self.on_rssi_check)
        self.ui.check_run_db.clicked.connect(self.on_run_db_check)
        self.ui.login_cred.clicked.connect(self.on_login_cred_check)

        self.ui.gps_wid.setDisabled(True)
        self.ui.speed_chw.setDisabled(True)
        self.ui.rssi_chw.setDisabled(True)
        self.ui.tag_chw.setDisabled(True)
        self.ui.login_chw.setDisabled(True)

        self.userName = user_name
        self.token = token
        self.email = email
        self.password = password

        self._stop = threading.Event()

        self.gps = GPS(port="")
        self.scan_port_stop = threading.Event()
        self.scan_port_thread = threading.Thread(target=self.monitor_gps_port)

        self.internet_gps = threading.Thread(target=self.get_internet_gps_data)
        self.igps_stop = threading.Event()

        pre_config_gps()
        self.load_setting()

        self.rfid = RFID()
        self.rfid.sig_msg.connect(self.monitor_rfid_status)
        self.rfid.start()

        self.scheduler_thread = threading.Thread(target=self.start_scheduler)
        self.scheduler_thread.start()

        self.upload_record.connect(self.upload_scanned_data)

        self.notify_thread = threading.Thread(target=self.beep_sound)

        self.db_connection = sqlite3.connect('database.db')
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute('''
                            CREATE TABLE IF NOT EXISTS records (
                                id INTEGER PRIMARY KEY,
                                rfidTag TEXT NOT NULL,
                                antenna INTEGER NOT NULL,
                                RSSI INTEGER NOT NULL,
                                latitude REAL NOT NULL,
                                longitude REAL NOT NULL,
                                speed REAL NOT NULL,
                                heading REAL NOT NULL,
                                locationCode TEXT NOT NULL,
                                username TEXT NOT NULL,
                                tag1 TEXT NOT NULL,
                                value1 TEXT NOT NULL,
                                tag2 TEXT NOT NULL,
                                value2 TEXT NOT NULL,
                                tag3 TEXT NOT NULL,
                                value3 TEXT NOT NULL,
                                tag4 TEXT NOT NULL,
                                value4 TEXT NOT NULL,
                                timestamp INTEGER NOT NULL
                            )
                        ''')
        self.db_connection.commit()

        self.database = []
        self.use_db = False

        self.last_lat = None
        self.last_lon = None
        self.last_utctime = None
        self.cur_lat = 0
        self.cur_lon = 0
        self.bearing = 0
        self.speed = 0
        try:
            pygame.mixer.init()
            logger.debug("Pygame mixer initialized successfully.")
        except Exception as e:
            logger.error(f"An unexpected error occurred while pygame initialization: {e}")

    #     self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
    #     self.ui.tableWidget.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
    #     for row in range(self.ui.tableWidget.rowCount()):
    #         for column in range(self.ui.tableWidget.columnCount()):
    #             item = QTableWidgetItem("")
    #             item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEditable &
    #                           ~Qt.ItemFlag.ItemIsEnabled)
    #             self.ui.tableWidget.setItem(row, column, item)
    #
    #     self.ui.radio_api_default.clicked.connect(self.select_api_type)
    #     self.ui.radio_api_custom.clicked.connect(self.select_api_type)
    #     self.ui.radio_api_both.clicked.connect(self.select_api_type)
    #     self.ui.radio_login_basic.clicked.connect(self.select_login_type)
    #     self.ui.radio_login_token.clicked.connect(self.select_login_type)
    #     self.ui.edit_rfid_host.textChanged.connect(self.on_rfid_host_text_changed)
    #     self.ui.gps_checkBox.clicked.connect(self.on_gps_checked)
    #     self.ui.radio_external_gps.clicked.connect(self.on_gps_type)
    #     self.ui.radio_internet_gps.clicked.connect(self.on_gps_type)
    #     self.ui.setting_save_btn.released.connect(self.setting_save)
    #     self.ui.api_save_btn.released.connect(self.api_save)
    #     self.ui.speed_limit.clicked.connect(self.on_speed_check)
    #     self.ui.tag_limit.clicked.connect(self.on_tag_check)
    #     self.ui.rssi_limit.clicked.connect(self.on_rssi_check)
    #     self.ui.check_run_db.clicked.connect(self.on_run_db_check)
    #     self.ui.token_widget.hide()
    #     self.ui.custom_widget.hide()
    #
    #     self.use_db = False
    #     self.gps = GPS(port="")
    #     self.scan_port_stop = threading.Event()
    #     self.scan_port_thread = threading.Thread(target=self.monitor_gps_port)
    #     self.igps_stop = threading.Event()
    #     self.internet_gps = threading.Thread(target=self.get_internet_gps_data)
    #     self.rfid = None
    #     self._stop = threading.Event()
    #     self.scheduler_thread = None
    #     self.notify_thread = threading.Thread(target=self.beep_sound)
    #
    #     self.userName = user_name
    #     self.token = token
    #     self.email = email
    #     self.password = password
    #     self.db_connection = sqlite3.connect('database.db')
    #     self.db_cursor = self.db_connection.cursor()
    #     self.db_cursor.execute('''
    #                 CREATE TABLE IF NOT EXISTS records (
    #                     id INTEGER PRIMARY KEY,
    #                     rfidTag TEXT NOT NULL,
    #                     antenna INTEGER NOT NULL,
    #                     RSSI INTEGER NOT NULL,
    #                     latitude REAL NOT NULL,
    #                     longitude REAL NOT NULL,
    #                     speed REAL NOT NULL,
    #                     heading REAL NOT NULL,
    #                     locationCode TEXT NOT NULL,
    #                     username TEXT NOT NULL,
    #                     tag1 TEXT NOT NULL,
    #                     value1 TEXT NOT NULL,
    #                     tag2 TEXT NOT NULL,
    #                     value2 TEXT NOT NULL,
    #                     tag3 TEXT NOT NULL,
    #                     value3 TEXT NOT NULL,
    #                     tag4 TEXT NOT NULL,
    #                     value4 TEXT NOT NULL,
    #                     timestamp INTEGER NOT NULL
    #                 )
    #             ''')
    #     self.db_connection.commit()
    #     self.database = []
    #
    #     self.last_lat = None
    #     self.last_lon = None
    #     self.last_utctime = None
    #     self.cur_lat = 0
    #     self.cur_lon = 0
    #     self.bearing = 0
    #     self.speed = 0
    #
    #     self.upload_record.connect(self.upload_scanned_data)
    #
    #     self.loadingDlg = LoadingDlg()
    #
    #     self.lt = threading.Thread(target=self.loading_thread)
    #     self.lt.start()
    #     self.loadingDlg.setModal(True)
    #     self.loadingDlg.exec()
    #
    # def loading_thread(self):
    #
    #     self.load_setting()
    #
    #     self.rfid = RFID()
    #     self.rfid.sig_msg.connect(self.monitor_rfid_status)
    #     self.rfid.start()
    #
    #     self._stop = threading.Event()
    #     self.scheduler_thread = threading.Thread(target=self.start_scheduler)
    #     self.scheduler_thread.start()
    #
    #     pygame.mixer.init()
    #
    #     while not self.loadingDlg.isVisible():
    #         time.sleep(1)
    #
    #     self.loadingDlg.hide()

    def on_run_db_check(self):
        if self.ui.check_run_db.isChecked():
            self.use_db = True
        else:
            self.use_db = False

    def on_log_out(self):
        self.close()
        if os.path.isfile('setting/login.cre'):
            os.remove('setting/login.cre')
            # logger.debug("Credential file has been deleted successfully.")
        self.main_closed.emit()

    def on_speed_check(self):
        if self.ui.speed_limit.isChecked():
            self.ui.speed_chw.setEnabled(True)
        else:
            self.ui.speed_chw.setDisabled(True)

    def on_tag_check(self):
        if self.ui.tag_limit.isChecked():
            self.ui.tag_chw.setEnabled(True)
        else:
            self.ui.tag_chw.setDisabled(True)

    def on_rssi_check(self):
        if self.ui.rssi_limit.isChecked():
            self.ui.rssi_chw.setEnabled(True)
        else:
            self.ui.rssi_chw.setDisabled(True)

    def on_login_cred_check(self):
        if self.ui.login_cred.isChecked():
            self.ui.login_chw.setEnabled(True)
        else:
            self.ui.login_chw.setDisabled(True)

    def on_gps_checked(self):
        if self.ui.gps_checkBox.isChecked():
            self.ui.gps_wid.setEnabled(True)
        else:
            self.ui.gps_wid.setDisabled(True)

    def on_gps_type(self):
        if self.ui.radio_internet_gps.isChecked():
            if self.internet_gps.is_alive():
                return
            self.gps.stop()
            self.scan_port_stop.set()
            self.scan_port_thread.join(.1)
            self.igps_stop.clear()
            self.internet_gps = threading.Thread(target=self.get_internet_gps_data)
            self.internet_gps.start()
        elif self.ui.radio_external_gps.isChecked():
            if self.internet_gps.is_alive():
                self.igps_stop.set()
                self.internet_gps.join(.1)
            if self.gps.is_alive():
                return
            pp = find_gps_port()
            if pp is not None:
                sta = True if self.ui.gps_connection_status.text() == "Connected" else False
                self.gps = GPS(port=pp, baud_rate=int(self.ui.edit_gps_baud.text()),
                               current_status=sta)
                self.gps.sig_msg.connect(self.monitor_gps_status)
                self.gps.start()
            elif self.ui.gps_connection_status.text() == "Connected":
                self.monitor_gps_status(False)
            self.scan_port_stop.clear()
            self.scan_port_thread = threading.Thread(target=self.monitor_gps_port)
            self.scan_port_thread.start()

    def monitor_gps_port(self):
        pass
        # while not self.scan_port_stop.is_set():
        #     pp = find_gps_port()
        #     logger.debug(f"port:{pp}")
        #     if pp is not None:
        #         if self.gps.is_alive() and self.gps.port != pp:
        #             self.gps.stop()
        #         if not self.gps.is_alive():
        #             sta = True if self.ui.gps_connection_status.text() == "Connected" else False
        #             self.gps = GPS(port=pp, baud_rate=int(self.ui.edit_gps_baud.text()),
        #                            current_status=sta)
        #             self.gps.sig_msg.connect(self.monitor_gps_status)
        #             self.gps.start()
        #     time.sleep(1)

    def get_internet_gps_data(self):
        while not self.igps_stop.is_set():
            self.cur_lat, self.cur_lon, self.speed, self.bearing = 0, 0, 0, 0
            # Define the retry strategy
            retry_strategy = Retry(
                total=1,  # Total number of retries
                backoff_factor=1,  # Backoff factor for retries
                status_forcelist=[429, 500, 502, 503, 504],  # HTTP statuses to retry on
                allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]  # Methods to retry
            )

            # Adapter for requests session
            adapter = HTTPAdapter(max_retries=retry_strategy)
            http = requests.Session()
            http.mount("http://", adapter)
            http.mount("https://", adapter)
            try:
                response = requests.get('http://ip-api.com/json/', timeout=3)
                response.raise_for_status()
                data = response.json()
                # logger.debug(f"gps response:{response},{data}")
                if data['status'] == 'success':
                    if self.ui.gps_connection_status.text() == "Disconnected":
                        self.monitor_gps_status(True)
                    self.cur_lat, self.cur_lon = data['lat'], data['lon']
                    milliseconds_time = int(time.time() * 1_000_000)
                    if self.last_lat is not None:
                        self.speed, self.bearing = calculate_speed_bearing(self.last_lat, self.last_lon,
                                                                           self.last_utctime, self.cur_lat,
                                                                           self.cur_lon,
                                                                           milliseconds_time)
                    self.last_lat = self.cur_lat
                    self.last_lon = self.cur_lon
                    self.last_utctime = milliseconds_time
            except Exception:
                if self.ui.gps_connection_status.text() == "Connected":
                    self.monitor_gps_status(False)
            time.sleep(4)

    def beep_sound(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_wav:
            tmp_wav.write(wav_data)
            tmp_wav_path = tmp_wav.name
        try:
            sound = pygame.mixer.Sound(tmp_wav_path)
            sound.play()
        except pygame.error:
            logger.error("pygame error.")
        finally:
            os.unlink(tmp_wav_path)

    def on_rfid_host_text_changed(self, text):
        if is_ipv4_address(text):
            self.rfid.set_reader(text, True if self.ui.rfid_connection_status.text() == "Connected" else False)

    def load_setting(self):
        if os.path.isfile('setting/module.setting'):
            try:
                with open('setting/module.setting', 'r') as load_file:
                    setting_data = json.load(load_file)
                    self.ui.edit_rfid_noti.setText(setting_data['RFID']['notify'])
                    self.ui.edit_rfid_host.setText(setting_data['RFID']['host'])
                    self.ui.edit_rfid_rsa1.setText(setting_data['RFID']['rsa1'])
                    self.ui.edit_rfid_rsa2.setText(setting_data['RFID']['rsa2'])
                    self.ui.edit_rfid_lsa1.setText(setting_data['RFID']['lsa1'])
                    self.ui.edit_rfid_lsa2.setText(setting_data['RFID']['lsa2'])
                    self.ui.edit_rfid_ra1.setText(setting_data['RFID']['ra1'])
                    self.ui.edit_rfid_ra2.setText(setting_data['RFID']['ra2'])

                    if setting_data['gps']['checked']:
                        self.ui.gps_checkBox.setChecked(True)
                        self.ui.gps_wid.setEnabled(True)
                    else:
                        self.ui.gps_checkBox.setChecked(False)
                        self.ui.gps_wid.setDisabled(True)
                    if setting_data['gps']['is_external']:
                        self.ui.radio_external_gps.setChecked(True)
                        pp = find_gps_port()
                        if pp is not None:
                            self.ui.edit_gps_port.setText(pp)
                            self.gps = GPS(port=pp)
                            self.gps.sig_msg.connect(self.monitor_gps_status)
                            self.gps.start()
                        self.scan_port_stop.clear()
                        self.scan_port_thread = threading.Thread(target=self.monitor_gps_port)
                        self.scan_port_thread.start()
                    else:
                        self.ui.radio_internet_gps.setChecked(True)
                        self.igps_stop.clear()
                        self.internet_gps = threading.Thread(target=self.get_internet_gps_data)
                        self.internet_gps.start()
                    if setting_data['speed']['checked']:
                        self.ui.speed_limit.setChecked(True)
                        self.ui.speed_chw.setEnabled(True)
                    else:
                        self.ui.speed_limit.setChecked(False)
                        self.ui.speed_chw.setDisabled(True)
                    if setting_data['rssi']['checked']:
                        self.ui.rssi_limit.setChecked(True)
                        self.ui.rssi_chw.setEnabled(True)
                    else:
                        self.ui.rssi_limit.setChecked(False)
                        self.ui.rssi_chw.setDisabled(True)
                    if setting_data['tag_range']['checked']:
                        self.ui.tag_limit.setChecked(True)
                        self.ui.tag_chw.setEnabled(True)
                    else:
                        self.ui.tag_limit.setChecked(False)
                        self.ui.tag_chw.setDisabled(True)
                    if setting_data['use_database']:
                        self.ui.check_run_db.setChecked(True)
                    else:
                        self.ui.check_run_db.setChecked(False)
                    if setting_data['login']['checked']:
                        self.ui.login_chw.setChecked(True)
                        self.ui.login_chw.setEnabled(True)
                    else:
                        self.ui.login_chw.setChecked(False)
                        self.ui.login_chw.setDisabled(True)
                    self.ui.edit_gps_noti.setText(setting_data['gps']['notify'])
                    self.ui.edit_gps_hand.setText(setting_data['gps']['handshake'])
                    self.ui.edit_gps_dbits.setText(setting_data['gps']['data_bits'])
                    self.ui.edit_gps_sbits.setText(setting_data['gps']['stop_bits'])
                    self.ui.edit_gps_parity.setText(setting_data['gps']['parity'])
                    self.ui.edit_gps_baud.setText(setting_data['gps']['baud_rate'])

                    self.ui.setting_min_speed.setText(setting_data['speed']['min'])
                    self.ui.setting_max_speed.setText(setting_data['speed']['max'])
                    self.ui.setting_min_rssi.setText(setting_data['rssi']['min'])
                    self.ui.setting_max_rssi.setText(setting_data['rssi']['max'])
                    self.ui.setting_start_tag.setText(setting_data['tag_range']['min'])
                    self.ui.setting_end_tag.setText(setting_data['tag_range']['max'])
                    self.ui.setting_login_user.setText(setting_data['login']['username'])
                    self.ui.setting_login_pass.setText(setting_data['login']['password'])
            except Exception:
                pass
        if self.ui.setting_login_user.text() == "":
            self.ui.setting_login_user.setText(self.email)
        if self.ui.setting_login_pass.text() == "":
            self.ui.setting_login_pass.setText(self.password)

    def setting_save(self):
        setting_data = {
            'RFID': {'notify': self.ui.edit_rfid_noti.text(), 'host': self.ui.edit_rfid_host.text(),
                     'rsa1': self.ui.edit_rfid_rsa1.text(), 'rsa2': self.ui.edit_rfid_rsa2.text(),
                     'lsa1': self.ui.edit_rfid_lsa1.text(), 'lsa2': self.ui.edit_rfid_lsa2.text(),
                     'ra1': self.ui.edit_rfid_ra1.text(), 'ra2': self.ui.edit_rfid_ra2.text()},
            'gps': {'checked': self.ui.gps_checkBox.isChecked(), 'is_external': self.ui.radio_external_gps.isChecked(),
                    'notify': self.ui.edit_gps_noti.text(), 'handshake': self.ui.edit_gps_hand.text(),
                    'port': self.ui.edit_gps_port.text(), 'data_bits': self.ui.edit_gps_dbits.text(),
                    'stop_bits': self.ui.edit_gps_sbits.text(), 'parity': self.ui.edit_gps_parity.text(),
                    'baud_rate': self.ui.edit_gps_baud.text()},
            'speed': {'checked': self.ui.speed_limit.isChecked(), 'min': self.ui.setting_min_speed.text(),
                      'max': self.ui.setting_max_speed.text()},
            'rssi': {'checked': self.ui.rssi_limit.isChecked(), 'min': self.ui.setting_min_rssi.text(),
                     'max': self.ui.setting_max_rssi.text()},
            'tag_range': {'checked': self.ui.tag_limit.isChecked(), 'min': self.ui.setting_start_tag.text(),
                          'max': self.ui.setting_end_tag.text()},
            'use_database': self.ui.check_run_db.isChecked(),
            'login': {'checked': self.ui.login_cred.isChecked(), 'username': self.ui.setting_login_user.text(),
                      'password': self.ui.setting_login_pass.text()}
        }
        if not os.path.exists('setting'):
            os.makedirs('setting')
        with open('setting/module.setting', 'w') as save_file:
            json.dump(setting_data, save_file, indent=4)
        # logger.info("Reader and GPS configuration saved.")

    def api_save(self):
        api_data = {
            'login': {'username': self.ui.edit_username.text(), 'password': self.ui.edit_password.text(),
                      'token': self.ui.edit_token.text(), 'url': self.ui.edit_url.text()},
            'default': {'tag': self.ui.edit_api_tag.text(), 'ant': self.ui.edit_api_ant.text(),
                        'lat': self.ui.edit_gps_port.text(), 'lng': self.ui.edit_gps_dbits.text(),
                        'heading': self.ui.edit_gps_sbits.text(), 'speed': self.ui.edit_gps_parity.text()},
            'rssi': self.ui.edit_api_rssi.text()
        }
        if not os.path.exists('setting'):
            os.makedirs('setting')
        with open('setting/api_integration.setting', 'w') as save_file:
            json.dump(api_data, save_file, indent=4)
        # logger.info("API configuration saved.")

    def select_api_type(self):
        if self.ui.radio_api_default.isChecked():
            self.ui.custom_spacebar.show()
            self.ui.custom_widget.hide()
        elif self.ui.radio_api_custom.isChecked():
            self.ui.custom_spacebar.hide()
            self.ui.custom_widget.show()
        elif self.ui.radio_api_both.isChecked():
            self.ui.custom_spacebar.hide()
            self.ui.custom_widget.show()

    def select_login_type(self):
        if self.ui.radio_login_basic.isChecked():
            self.ui.basic_widget.show()
            self.ui.token_widget.hide()
        elif self.ui.radio_login_token.isChecked():
            self.ui.basic_widget.hide()
            self.ui.token_widget.show()

    def start_scheduler(self):
        schedule.clear()
        schedule.every(7).seconds.do(self.emit_upload_scanned_data)
        schedule.every(15).seconds.do(self.upload_health_data)
        schedule.every(25).days.do(self.regenerate_token)
        while not self._stop.is_set():
            schedule.run_pending()
            time.sleep(0.1)

    def regenerate_token(self):
        payload = {
            'email': self.email,
            'password': self.password
        }
        retry_strategy = Retry(
            total=1,  # Total number of retries
            backoff_factor=1,  # Backoff factor for retries
            status_forcelist=[429, 500, 502, 503, 504],  # HTTP statuses to retry on
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]  # Methods to retry
        )
        # Adapter for requests session
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        try:
            response = requests.Session().post(LOGIN_URL, json=payload, timeout=4)
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
                if data['metadata']['code'] == '200':
                    logger.debug('Received token successfully!')
                    self.token = data['result']['acessToken']
                    self.userName = data['result']['userNameId']
                else:
                    logger.error("Token reception failed.")
            else:
                logger.error("Token reception failed.")
        except Exception:
            logger.error("Token reception request error.")
        finally:
            http.close()

    def monitor_gps_status(self, status):
        if status:
            self.ui.gps_connection_status.setStyleSheet("""
                padding: 5px;
                border: 1px solid black;
                color: green;
                """)
            self.ui.gps_connection_status.setText("Connected")
        else:
            self.ui.gps_connection_status.setStyleSheet("""
                padding: 5px;
                border: 1px solid black;
                color: red;
                """)
            self.ui.gps_connection_status.setText("Disconnected")
        if self.ui.edit_gps_noti.text() == "1":
            self.notify_thread = threading.Thread(target=self.beep_sound)
            self.notify_thread.start()

    def monitor_rfid_status(self, status):
        if status == 1:
            self.ui.rfid_connection_status.setStyleSheet("""
                padding: 5px;
                border: 1px solid black;
                color: green;
                """)
            self.ui.rfid_connection_status.setText("Connected")
        elif status == 2:
            self.ui.rfid_connection_status.setStyleSheet("""
                padding: 5px;
                border: 1px solid black;
                color: red;
                """)
            self.ui.rfid_connection_status.setText("Disconnected")
        elif status == 3:
            tag = self.rfid.tag_data[0]
            lat, lon, speed, bearing = 0, 0, 0, 0
            if self.ui.radio_external_gps.isChecked():
                lat, lon = extract_from_gps(self.gps.get_data())
                if lat != 0 and lon != 0:
                    self.last_lat = lat
                    self.last_lon = lon
                    self.last_utctime = int(time.time() * 1_000_000)
                speed, bearing = self.gps.get_sdata()
            elif self.ui.radio_internet_gps.isChecked():
                lat, lon, speed, bearing = self.cur_lat, self.cur_lon, self.speed, self.bearing
            upload_flag = True
            if self.ui.speed_limit.isChecked():
                if (self.ui.setting_min_speed.text() != "" and self.ui.setting_max_speed.text() != "" and
                        (speed < int(self.ui.setting_min_speed.text()) or speed > int(
                            self.ui.setting_max_speed.text()))):
                    upload_flag = False
            if upload_flag and self.ui.rssi_limit.isChecked():
                if (self.ui.setting_min_rssi.text() != "" and self.ui.setting_max_rssi.text() != "" and
                        (tag['PeakRSSI'] < int(self.ui.setting_min_rssi.text()) or
                         tag['PeakRSSI'] > int(self.ui.setting_max_rssi.text()))):
                    upload_flag = False
            if upload_flag and self.ui.tag_limit.isChecked():
                if (self.ui.setting_start_tag.text() != "" and self.ui.setting_end_tag.text() != "" and
                        (int(tag['EPC-96']) < int(self.ui.setting_start_tag.text()) or
                         int(tag['EPC-96']) > int(self.ui.setting_end_tag.text()))):
                    upload_flag = False
            if upload_flag:
                if self.use_db:
                    self.db_cursor.execute('''
                        SELECT * FROM records
                        WHERE rfidTag = ?
                        AND ABS(timestamp - ?) < 10000000
                        ''', (tag['EPC-96'], tag['LastSeenTimestampUTC']))
                    rows = self.db_cursor.fetchall()
                    if rows:
                        upload_flag = False
                else:
                    for i in range(len(self.database) - 1, -1, -1):
                        if tag['LastSeenTimestampUTC'] - self.database[i][10] > 10_000_000:
                            break
                        if tag['EPC-96'] == self.database[i][1]:
                            upload_flag = False
                            break
            if upload_flag:
                if self.use_db:
                    self.db_cursor.execute('''
                        SELECT id FROM records
                        ORDER BY id ASC
                        ''')
                    used_ids = self.db_cursor.fetchall()
                    self.db_cursor.execute('''
                    INSERT INTO records
                    (id, rfidTag, antenna, RSSI, latitude, longitude, speed, heading, locationCode, username,
                    timestamp, tag1, value1, tag2, value2, tag3, value3, tag4, value4)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        find_smallest_available_id(used_ids), tag['EPC-96'], f"{tag['AntennaID']}",
                        f"{tag['PeakRSSI']}", lat, lon,
                        speed, bearing, "-", self.userName, tag['LastSeenTimestampUTC'],
                        self.ui.edit_api_ctag1.text(), self.ui.edit_api_cval1.text(),
                        self.ui.edit_api_ctag2.text(), self.ui.edit_api_cval2.text(),
                        self.ui.edit_api_ctag3.text(), self.ui.edit_api_cval3.text(),
                        self.ui.edit_api_ctag4.text(), self.ui.edit_api_cval4.text()
                    ))
                    self.db_connection.commit()
                else:
                    new_data = [upload_flag, tag['EPC-96'], f"{tag['AntennaID']}", f"{tag['PeakRSSI']}",
                                lat, lon,
                                speed, bearing, "-", self.userName, tag['LastSeenTimestampUTC'],
                                self.ui.edit_api_ctag1.text(), self.ui.edit_api_cval1.text(),
                                self.ui.edit_api_ctag2.text(), self.ui.edit_api_cval2.text(),
                                self.ui.edit_api_ctag3.text(), self.ui.edit_api_cval3.text(),
                                self.ui.edit_api_ctag4.text(), self.ui.edit_api_cval4.text()]
                    self.database.append(new_data)
            self.refresh_data_table([tag['EPC-96'], f"{tag['AntennaID']}", f"{tag['PeakRSSI']}",
                                     f"{lat:.4f}".rstrip('0').rstrip('.') + ", " + f"{lon:.4f}".rstrip('0').rstrip('.'),
                                     f"{speed}", f"{bearing}"])
            self.ui.last_rfid_read.setText(tag['EPC-96'])
            self.ui.last_rfid_time.setText(get_date_from_utc(tag['LastSeenTimestampUTC']))
            self.ui.last_gps_read.setText(f"{lat}, {lon}")
            self.ui.last_gps_time.setText(get_date_from_utc(tag['LastSeenTimestampUTC']))
            self.ui.edit_api_tag.setText(tag['EPC-96'])
            self.ui.edit_api_ant.setText(f"{tag['AntennaID']}")
            self.ui.edit_api_lat.setText(f"{lat}")
            self.ui.edit_api_lng.setText(f"{lon}")
            self.ui.edit_api_heading.setText(f"{bearing}")
            self.ui.edit_api_speed.setText(f"{speed}")
            self.ui.edit_api_rssi.setText(f"{tag['PeakRSSI']}")
        if status != 3 and self.ui.edit_rfid_noti.text() == "1":
            self.notify_thread = threading.Thread(target=self.beep_sound)
            self.notify_thread.start()

    def upload_to_default(self, payload):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"  # Ensure the payload is interpreted as JSON
        }
        retry_strategy = Retry(
            total=1,  # Total number of retries
            backoff_factor=1,  # Backoff factor for retries
            status_forcelist=[429, 500, 502, 503, 504],  # HTTP statuses to retry on
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]  # Methods to retry
        )
        # Adapter for requests session
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        try:
            # logger.debug(f"scanned:{headers}, {payload}")
            response = requests.post(RECORD_UPLOAD_URL, headers=headers, json=payload, timeout=4)
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
                # logger.debug(f"response:{data}")
                if data['metadata']['code'] == '200':
                    return True
        except Exception:
            pass
        finally:
            http.close()
        return False

    def upload_to_custom(self, payload):
        if self.ui.radio_login_basic.isChecked():
            pass
        elif self.ui.radio_login_token.isChecked():
            pass
        return True

    def upload_data(self, payload_default, payload_custom):
        delete = None
        if self.ui.radio_api_default.isChecked():
            delete = self.upload_to_default(payload_default)
        elif self.ui.radio_api_custom.isChecked():
            delete = self.upload_to_custom(payload_custom)
        elif self.ui.radio_api_both.isChecked():
            delete1 = self.upload_to_default(payload_default)
            delete2 = self.upload_to_custom(payload_custom)
            delete = delete1 or delete2
        return delete

    def upload_health_data(self):
        logger.info('Uploading health data initiated...')
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"  # Ensure the payload is interpreted as JSON
        }
        lat, lon = extract_from_gps(self.gps.get_data())
        payload = {
            "userName": self.userName,
            "rfidStatus": "Connected" if self.rfid.connectivity else "Disconnected",
            "gpsStatus": "Connected" if self.gps.connectivity else "Disconnected",
            "macAddress": '-'.join(('%012X' % uuid.getnode())[i:i + 2] for i in range(0, 12, 2)),
            "lat": lat,
            "lng": lon,
            "dateTime": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        }

        retry_strategy = Retry(
            total=1,  # Total number of retries
            backoff_factor=1,  # Backoff factor for retries
            status_forcelist=[429, 500, 502, 503, 504],  # HTTP statuses to retry on
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]  # Methods to retry
        )
        # Adapter for requests session
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        try:
            # logger.debug(f"health:{headers}, {payload}")
            response = http.post(HEALTH_UPLOAD_URL, headers=headers, json=payload, timeout=4)
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
                # logger.debug(f"response:{data}")
                if data['metadata']['code'] == '200':
                    logger.info('Uploading health data successfully finished.')
                else:
                    logger.error("Uploading health data failed.")
            else:
                logger.error("Uploading health data failed.")
        except Exception:
            logger.error("Error occurred while uploading health data.")
        finally:
            http.close()

    def emit_upload_scanned_data(self):
        self.upload_record.emit()

    def upload_scanned_data(self):
        logger.info('Uploading scanned data initiated...')
        if self.use_db:
            self.db_cursor.execute('''
                            SELECT id, rfidTag, antenna, RSSI, latitude, longitude, speed, heading,
                            locationCode, username, tag1, value1, tag2, value2, tag3, value3, tag4, value4
                            FROM records
                            ORDER BY timestamp ASC
                            ''')
            data = self.db_cursor.fetchall()
            chunk_size = 1000
            for i in range(0, len(data), chunk_size):
                chunk = data[i:i + chunk_size]
                payload_default, payload_custom = convert_formatted_payload(chunk)
                delete = self.upload_data(payload_default, payload_custom)
                if delete:
                    ids_to_delete = [row[0] for row in chunk]
                    self.db_cursor.execute('''
                                        DELETE FROM records
                                        WHERE id IN (%s)
                                        ''' % ','.join('?' * len(ids_to_delete)), ids_to_delete)
            logger.info("Uploading scanned data finished.")
            microsecond_timestamp = int(time.time() * 1_000_000)
            self.db_cursor.execute('''
                                    DELETE FROM records
                                    WHERE ABS(timestamp - ?) > 600000000
                                ''', [microsecond_timestamp])
            self.db_connection.commit()
        else:
            chunk_size = 1000
            start_index = 0
            while start_index < len(self.database):
                chunk = self.database[start_index:start_index + chunk_size]
                payload_default, payload_custom = convert_formatted_payload(chunk)
                delete = self.upload_data(payload_default, payload_custom)
                if delete:
                    self.database = self.database[:start_index] + self.database[start_index + chunk_size:]
                else:
                    start_index = start_index + chunk_size
            logger.info("Uploading scanned data finished.")
            microsecond_timestamp = int(time.time() * 1_000_000)
            i = 0
            for i in range(len(self.database)):
                if microsecond_timestamp - self.database[i][10] < 600_000_000:
                    break
            self.database = self.database[i:]
        logger.info('Deleted old data.')

    def refresh_data_table(self, new_data):
        for row in range(self.ui.tableWidget.rowCount() - 2, -1, -1):
            for column in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, column).text()
                self.ui.tableWidget.setItem(row + 1, column, QTableWidgetItem(item))
        for column in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.setItem(0, column, QTableWidgetItem(new_data[column]))

    def showEvent(self, event):
        self.resize_columns_to_fit()

    def resizeEvent(self, event):
        self.resize_columns_to_fit()

    def resize_columns_to_fit(self):
        width = self.ui.tableWidget.viewport().width()
        column_proportions = [0.38, 0.12, 0.08, 0.2, 0.09]
        wid = 0
        for i in range(self.ui.tableWidget.columnCount() - 1):
            self.ui.tableWidget.setColumnWidth(i, width * column_proportions[i])
            wid = wid + self.ui.tableWidget.columnWidth(i)
        self.ui.tableWidget.setColumnWidth(self.ui.tableWidget.columnCount() - 1, width - wid)
        height = self.ui.tableWidget.viewport().height()
        for i in range(self.ui.tableWidget.rowCount() - 1):
            self.ui.tableWidget.setRowHeight(i, height / self.ui.tableWidget.rowCount())
        self.ui.tableWidget.setRowHeight(self.ui.tableWidget.rowCount() - 1, height -
                                         int(height / self.ui.tableWidget.rowCount()) *
                                         (self.ui.tableWidget.rowCount() - 1))

    def closeEvent(self, event):
        self.setting_save()
        self.db_connection.close()
        self.gps.stop()
        self.scan_port_stop.set()
        if self.scan_port_thread.is_alive():
            self.scan_port_thread.join(.1)
        self.igps_stop.set()
        if self.internet_gps.is_alive():
            self.internet_gps.join(.1)
        self.rfid.stop()
        self._stop.set()
        schedule.clear()
        if self.scheduler_thread.is_alive():
            self.scheduler_thread.join(.1)
        return super().closeEvent(event)
