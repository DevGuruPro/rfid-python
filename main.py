import json
import os
import sys

import requests
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from settings import LOGIN_URL
from utils.logger import logger
from widget.loginWnd import LoginWnd
from widget.mainWnd import MainWnd
from widget.loadingDlg import LoadingDlg

import ui.res_rc


class InventorySystem(object):
    def __init__(self):
        self.login = LoginWnd()
        self.login.login_closed.connect(self.close_login)
        self.main = None
        self.load_credential()

    def load_credential(self):
        if os.path.isfile('setting/module.setting'):
            try:
                with open('setting/module.setting', 'r') as load_file:
                    credential = json.load(load_file)
                    if credential['login']['username'] != "" and credential['login']['password'] != "":
                        self.login_server(credential['login']['username'], credential['login']['password'])
                        return
            except Exception:
                pass
        self.login_server("a@a.com", "123")

    def login_server(self, username, password):
        payload = {
            'email': username,
            'password': password
        }
        try:
            print(payload)
            response = requests.Session().post(LOGIN_URL, json=payload, timeout=4)
            print('1')
            if response.status_code == 200:
                data = response.json()
                if data['metadata']['code'] == '200':
                    logger.debug('Login successful!')
                    # credential = {
                    #     'username': username,
                    #     'password': password
                    # }
                    # if not os.path.exists('setting'):
                    #     os.makedirs('setting')
                    # with open('setting/login.cre', 'w') as save_file:
                    #     json.dump(credential, save_file, indent=4)
                    # logger.info("Credentials saved.")
                    self.login.userName = data['result']['userNameId']
                    self.login.token = data['result']['acessToken']
                    self.login.email = username
                    self.login.password = password
                else:
                    logger.error("Login failed")
                    self.login.show()
                    return
            else:
                logger.error("Login failed")
                self.login.show()
                return
        except Exception as e:
            logger.error(f"Login Error{e}")
            self.login.show()
            return
        self.close_login()

    def close_login(self):
        self.main = MainWnd(self.login.userName, self.login.token, self.login.email, self.login.password)
        self.main.main_closed.connect(self.close_main)
        self.main.show()

    def close_main(self):
        self.login = LoginWnd()
        self.login.login_closed.connect(self.close_login)
        self.login.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_icon = QIcon(u":/img/icon.ico")
    app.setWindowIcon(app_icon)
    IS = InventorySystem()
    sys.exit(app.exec())
