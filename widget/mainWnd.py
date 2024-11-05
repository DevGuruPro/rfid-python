import os
import sys

from PySide6 import QtCore
from PySide6.QtGui import Qt, QPainter, QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication

from ui.ui_main import Ui_MainWindow

import ui.res_rc


class MainWnd(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWnd()
    window.show()
    sys.exit(app.exec())