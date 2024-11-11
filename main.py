import sys

from PySide6.QtWidgets import QApplication

from widget.loginWnd import LoginWnd
from widget.mainWnd import MainWnd


class InventorySystem(object):
    def __init__(self):
        self.login = LoginWnd()
        self.login.login_closed.connect(self.close_login)
        self.login.show()
        self.main = None

    def close_login(self):
        self.main = MainWnd(self.login.userName, self.login.token)
        self.main.main_closed.connect(self.close_main)
        self.main.show()

    def close_main(self):
        self.login = LoginWnd()
        self.login.login_closed.connect(self.close_login)
        self.login.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    IS = InventorySystem()
    sys.exit(app.exec())
