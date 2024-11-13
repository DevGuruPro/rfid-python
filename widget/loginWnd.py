import sys
import requests
from PySide6.QtCore import Signal

from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from requests import Timeout, RequestException

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
        self.ui.loginBtn.released.connect(self.login)
        self.token = None
        self.userName = None

    def login(self):
        username = self.ui.user_edit.text()
        password = self.ui.pass_edit.text()
        payload = {
            'email': username,
            'password': password
        }
        try:
            response = requests.Session().post(LOGIN_URL, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data['metadata']['code'] == '200':
                    logger.debug('Login successful!')
                    self.token = data['result']['acessToken']
                    self.userName = data['result']['userNameId']
                    self.close()
                    self.login_closed.emit()
                else:
                    logger.error("Login failed")
                    QMessageBox.critical(self, 'Login', "Login Failed.", QMessageBox.StandardButton.Ok)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWnd()
    window.show()
    sys.exit(app.exec())
