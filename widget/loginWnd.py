import os
import sys

from PySide6 import QtCore, QtGui
from PySide6.QtGui import Qt, QPixmap, QBrush, QPalette, QPainter
from PySide6.QtWidgets import QMainWindow, QApplication

from ui.ui_login import Ui_LoginWindow

import ui.res_rc


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

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(":/img/background.jpg")
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWnd()
    window.show()
    sys.exit(app.exec())