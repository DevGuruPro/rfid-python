import os

from PySide6 import QtCore
from PySide6.QtGui import Qt, QMovie
from PySide6.QtWidgets import QDialog

from ui.dialog.ui_loadingDlg import Ui_LoadingDialog

import ui.res_rc


class LoadingDlg(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoadingDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.movie = QMovie(u":/img/loading.gif")
        self.ui.videoLabel.setMovie(self.movie)
        self.movie.start()
