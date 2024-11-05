import sys
import requests

from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from requests import Timeout, RequestException

from settings import LOGIN_URL
from ui.ui_login import Ui_LoginWindow

from utils.logger import logger


class LoginWnd(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.loginBtn.released.connect(self.login)

    def login(self):
        username = self.ui.user_edit.text()
        password = self.ui.pass_edit.text()
        payload = {
            'email': username,
            'password': password
        }
        try:
            response = requests.Session().post(LOGIN_URL, json=payload)
            data = response.json()
            if data['metadata']['code'] == '200':
                logger.debug('Login successful!')
                self.close()
            else:
                logger.error("Login failed")
                QMessageBox.critical(self, 'Login', "Login Failed. Please input correct credentials.",
                                     QMessageBox.StandardButton.Ok)
        except ConnectionError as ce:
            logger.error("Connection error occurred:", ce)
            QMessageBox.critical(self, 'Login', "Connection Error.", QMessageBox.StandardButton.Ok)
        except Timeout as te:
            logger.error("Request timed out:", te)
            QMessageBox.critical(self, 'Login', "Request timed out..",
                                 QMessageBox.StandardButton.Ok)
        except RequestException as re:
            logger.error("An error occurred:", re)
            QMessageBox.critical(self, 'Login', "Login Error.", QMessageBox.StandardButton.Ok)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(":/img/background.jpg")
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWnd()
    window.show()
    sys.exit(app.exec())
