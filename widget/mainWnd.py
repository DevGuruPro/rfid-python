import os
import sys
import threading
import time
import uuid
from datetime import datetime

import requests
import schedule
import winsound
import json

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidget, QTableWidgetItem

from settings import SOUND_FREQUENCY, SOUND_DURATION, HEALTH_UPLOAD_URL, RECORD_UPLOAD_URL
from ui.ui_main import Ui_MainWindow
from utils.commons import extract_from_gps, get_date_from_utc, calculate_speed_bearing, find_gps_port

from utils.gps import GPS
from utils.logger import logger
from utils.rfid import RFID


def beep_sound():
    winsound.Beep(SOUND_FREQUENCY, SOUND_DURATION)


class MainWnd(QMainWindow):

    def __init__(self, user_name, token):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.ui.tableWidget.setSelectionMode(QTableWidget.SelectionMode.NoSelection)

        # Fill the table with some data and make items non-editable
        for row in range(self.ui.tableWidget.rowCount()):
            for column in range(self.ui.tableWidget.columnCount()):
                item = QTableWidgetItem("")
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEditable &
                              ~Qt.ItemFlag.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, column, item)
        # self.ui.tableWidget.item(0, 0).setText("004837065827700000000333 - 1")
        # self.ui.tableWidget.item(0, 4).setText("5/20/2024 11:09:35 PM")
        self._stop = threading.Event()

        self.gps = GPS(find_gps_port())
        self.gps.sig_msg.connect(self.monitor_gps_status)
        # self.gps.start()

        self.rfid = RFID()
        self.rfid.sig_msg.connect(self.monitor_rfid_status)
        # self.rfid.start()

        self.scheduler_thread = threading.Thread(target=self.start_scheduler)
        self.scheduler_thread.start()

        self.notify_thread = threading.Thread(target=beep_sound)

        self.database = []
        self.notify_rfid = False
        self.notify_gps = False
        self.userName = user_name
        self.token = token

        self.ui.radio_api_default.clicked.connect(self.select_api_type)
        self.ui.radio_api_custom.clicked.connect(self.select_api_type)
        self.ui.radio_api_both.clicked.connect(self.select_api_type)

        self.ui.radio_login_basic.clicked.connect(self.select_login_type)
        self.ui.radio_login_token.clicked.connect(self.select_login_type)
        self.ui.token_widget.hide()
        self.ui.custom_widget.hide()

        self.ui.edit_rfid_noti.textChanged.connect(self.on_rfid_text_changed)
        self.ui.edit_gps_noti.textChanged.connect(self.on_gps_text_changed)
        self.ui.setting_save_btn.released.connect(self.setting_save)
        self.ui.api_save_btn.released.connect(self.api_save)

    def on_rfid_text_changed(self, text):
        if text == "1":
            self.notify_rfid = True
        else:
            self.notify_rfid = False

    def on_gps_text_changed(self, text):
        if text == "1":
            self.notify_gps = True
        else:
            self.notify_gps = False

    def setting_save(self):
        setting_data = {
            'RFID': {'notify': self.ui.edit_rfid_noti.text(), 'host': self.ui.edit_rfid_host.text(),
                     'rsa1': self.ui.edit_rfid_rsa1.text(), 'rsa2': self.ui.edit_rfid_rsa2.text(),
                     'lsa1': self.ui.edit_rfid_lsa1.text(), 'lsa2': self.ui.edit_rfid_lsa2.text(),
                     'ra1': self.ui.edit_rfid_ra1.text(), 'ra2': self.ui.edit_rfid_ra2.text()},
            'gps': {'notify': self.ui.edit_gps_noti.text(), 'handshake': self.ui.edit_gps_hand.text(),
                    'port': self.ui.edit_gps_port.text(), 'data_bits': self.ui.edit_gps_dbits.text(),
                    'stop_bits': self.ui.edit_gps_sbits.text(), 'parity': self.ui.edit_gps_parity.text(),
                    'baud_rate': self.ui.edit_gps_baud.text()},
            'speed': {'min': self.ui.setting_min_speed.text(), 'max': self.ui.setting_max_speed.text()},
            'rssi': {'min': self.ui.setting_min_rssi.text(), 'max': self.ui.setting_max_rssi.text()},
            'tag_range': {'min': self.ui.setting_start_tag.text(), 'max': self.ui.setting_end_tag.text()}
        }
        if not os.path.exists('setting'):
            os.makedirs('setting')
        with open('setting/module.setting', 'w') as save_file:
            json.dump(setting_data, save_file, indent=4)
        logger.info("Reader and GPS configuration saved.")

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
        logger.info("API configuration saved.")

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
        schedule.every(10).seconds.do(self.upload_scanned_data)
        schedule.every(10).minutes.do(self.upload_health_data)
        while not self._stop.is_set():
            schedule.run_pending()
            time.sleep(0.1)

    def monitor_gps_status(self, status):
        if status:
            self.ui.gps_connection_status.setText("Connected")
        else:
            self.ui.gps_connection_status.setText("Disconnected")
        if self.notify_gps:
            self.notify_thread.start()

    def monitor_rfid_status(self, status):
        if status == 1:
            self.ui.rfid_connection_status.setText("Connected")
        elif status == 2:
            self.ui.rfid_connection_status.setText("Disconnected")
        elif status == 3:
            tag = self.rfid.tag_data[0]
            lat, lon = extract_from_gps(self.gps.get_data())
            last_lat, last_lon = self.database[len(self.database)-1][4]
            speed, bearing = calculate_speed_bearing(last_lat, last_lon, self.database[len(self.database)-1][5],
                                                     lat, lon, tag['LastSeenTimestampUTC'])
            upload_flag = True
            if self.ui.speed_limit.isChecked():
                if speed < int(self.ui.setting_min_speed.text()) or speed > int(self.ui.setting_max_speed.text()):
                    upload_flag = False
            if upload_flag and self.ui.rssi_limit.isChecked():
                if (tag['PeakRSSI'] < int(self.ui.setting_min_rssi.text()) or
                        tag['PeakRSSI'] > int(self.ui.setting_min_rssi.text())):
                    upload_flag = False
            if upload_flag and self.ui.tag_limit.isChecked():
                if (int(tag['EPC-96']) < int(self.ui.setting_start_tag.text()) or
                        int(tag['EPC-96']) > int(self.ui.setting_end_tag.text())):
                    upload_flag = False
            new_data = [upload_flag, tag['EPC-96'], tag['AntennaID'], tag['PeakRSSI'], (lat, lon),
                        tag['LastSeenTimestampUTC'], speed, bearing]
            self.database.append(new_data)
            self.ui.last_rfid_read.setText(tag['EPC-96'])
            self.ui.last_rfid_time.setText(get_date_from_utc(tag['LastSeenTimestampUTC']))
            self.ui.last_gps_read.setText(f"{lat}, {lon}")
            self.ui.last_gps_time.setText(get_date_from_utc(tag['LastSeenTimestampUTC']))
        if self.notify_rfid:
            self.notify_thread.start()

    def upload_to_default(self):
        logger.info('Uploading scanned data initiated...')
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"  # Ensure the payload is interpreted as JSON
        }
        start_index = 0
        batch_index = 0
        while start_index < len(self.database):
            db = []
            index = start_index
            while len(db) < 1000 and index < len(self.database):
                item = self.database[index]
                if not item[0]:
                    continue
                data = {
                    "rfidTag": item[1],
                    "antenna": f"{item[2]}",
                    "latitude": item[4][0],
                    "longitude": item[4][1],
                    "heading": item[7],
                    "speed": item[6],
                    "locationCode": "-",
                    "username": self.userName
                }
                db.append(data)
                index = index+1
            payload = {
                "data": db
            }
            i = 0
            for i in range(3):
                try:
                    response = requests.post(RECORD_UPLOAD_URL, headers=headers, json=payload)
                    data = response.json()
                    if data['metadata']['code'] == '200':
                        logger.info(f'Uploading scanned data successfully finished-batch{batch_index}.')
                        self.database = self.database[:start_index]+self.database[index:]
                        logger.info(f'Uploaded record removed.')
                        break
                except requests.exceptions.RequestException as e:
                    pass
            if i != 3:
                logger.info(f'Uploading scanned data failed-batch{batch_index}.')
                start_index = index
            batch_index = batch_index + 1

    def upload_to_custom(self):
        if self.ui.radio_login_basic.isChecked():
            pass
        elif self.ui.radio_login_token.isChecked():
            pass

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
            "macAddress": '-'.join(('%012X' % uuid.getnode())[i:i+2] for i in range(0, 12, 2)),
            "lat": lat,
            "lng": lon,
            "dateTime": datetime.now().strftime("%Y-%m-%d")
        }
        try:
            response = requests.post(HEALTH_UPLOAD_URL, headers=headers, json=payload)
            data = response.json()
            if data['metadata']['code'] == '200':
                logger.info('Uploading health data successfully finished.')
            else:
                logger.error("Uploading health data failed.")
        except requests.exceptions.RequestException as e:
            logger.error("Error occurred while uploading health data, ", e)

    def upload_scanned_data(self):
        if self.ui.radio_api_default.isChecked():
            self.upload_to_default()
        elif self.ui.radio_api_custom.isChecked():
            self.upload_to_custom()
        elif self.ui.radio_api_both.isChecked():
            self.upload_to_default()
            self.upload_to_custom()
        microsecond_timestamp = int(time.time() * 1_000_000)
        while len(self.database):
            if microsecond_timestamp - self.database[0][5] < 600_000_000:
                break
            self.database.pop(0)
        logger.info('Deleted old data.')

    def refresh_data_table(self):
        rc = min(len(self.database), 8)
        for row in range(rc):
            for column in range(self.ui.tableWidget.columnCount()):
                d = self.database[len(self.database) - rc + row][column + 1]
                if column == 3:
                    item = QTableWidgetItem(f"{d[0]}, {d[1]}")
                elif column == 4:
                    item = QTableWidgetItem(get_date_from_utc(d))
                else:
                    item = QTableWidgetItem(d)
                # item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEditable
                #               & ~Qt.ItemFlag.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, column, item)

    def show_rfid_status(self, status):
        if status:
            self.ui.rfid_connection_status.setText("Connected")
        else:
            self.ui.rfid_connection_status.setText("Disconnected")

    def showEvent(self, event):
        self.resize_columns_to_fit()

    def resizeEvent(self, event):
        self.resize_columns_to_fit()

    def resize_columns_to_fit(self):
        width = self.ui.tableWidget.viewport().width()
        column_proportions = [0.36, 0.1, 0.1, 0.1]
        wid = 0
        for i in range(4):
            self.ui.tableWidget.setColumnWidth(i, width * column_proportions[i])
            wid = wid + self.ui.tableWidget.columnWidth(i)
        self.ui.tableWidget.setColumnWidth(4, width - wid)
        height = self.ui.tableWidget.viewport().height()
        for i in range(5):
            self.ui.tableWidget.setRowHeight(i, height / 6)
        self.ui.tableWidget.setRowHeight(5, height - int(height / 6) * 5)

    def closeEvent(self, event):
        self.gps.stop()
        self.rfid.stop()
        self._stop.set()
        schedule.clear()
        if self.scheduler_thread.is_alive():
            self.scheduler_thread.join(.1)
        return super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainWnd("aa")
    window.show()
    sys.exit(app.exec())
