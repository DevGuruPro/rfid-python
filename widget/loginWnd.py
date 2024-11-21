import json
import os
import sys
import requests
from PySide6.QtCore import Signal

from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from settings import LOGIN_URL
from ui.ui_login import Ui_LoginWindow

from utils.logger import logger


class LoginWnd(QMainWindow):

    login_closed = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.loginBtn.released.connect(self.on_login_btn_clicked)
        self.token = None
        self.userName = None
        self.email = None
        self.password = None

    def load_credential(self):
        if not os.path.isfile('setting/login.cre'):
            logger.debug("Credential file does not exist.")
            return
        with open('setting/login.cre', 'r') as load_file:
            credential = json.load(load_file)
            if credential['username'] != "" and credential['password'] != "":
                self.login(credential['username'], credential['password'])

    def on_login_btn_clicked(self):
        self.login(self.ui.user_edit.text(), self.ui.pass_edit.text())

    def login(self, username, password):
        payload = {
            'email': username,
            'password': password
        }
        try:
            response = requests.Session().post(LOGIN_URL, json=payload, timeout=4)
            if response.status_code == 200:
                data = response.json()
                if data['metadata']['code'] == '200':
                    logger.debug('Login successful!')
                    credential = {
                        'username': username,
                        'password': password
                    }
                    if not os.path.exists('setting'):
                        os.makedirs('setting')
                    with open('setting/login.cre', 'w') as save_file:
                        json.dump(credential, save_file, indent=4)
                    logger.info("Credentials saved.")
                    self.token = data['result']['acessToken']
                    self.userName = data['result']['userNameId']
                    self.email = username
                    self.password = password
                    self.close()
                    self.login_closed.emit()
                else:
                    logger.error("Login failed")
                    QMessageBox.critical(self, 'Login', "Input correct credentials.", QMessageBox.StandardButton.Ok)
            else:
                logger.error("Login failed")
                QMessageBox.critical(self, 'Login', "Login Failed.", QMessageBox.StandardButton.Ok)
        except requests.exceptions.RequestException as e:
            logger.error("Login Error, ", e)
            QMessageBox.critical(self, 'Login', "Login Error.", QMessageBox.StandardButton.Ok)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(":/img/login_background.png")
        painter.drawPixmap(self.rect(), pixmap)
