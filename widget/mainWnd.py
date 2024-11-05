import os
import sys

from PySide6 import QtCore
from PySide6.QtGui import Qt, QPainter, QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidget, QTableWidgetItem

from ui.ui_main import Ui_MainWindow

import ui.res_rc


class MainWnd(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Qt.WindowType.Popup
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.ui.tableWidget.horizontalHeader().sectionResized.connect(
        #     lambda: self.resize_columns_to_fit()
        # )
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.ui.tableWidget.setSelectionMode(QTableWidget.SelectionMode.NoSelection)

        # Fill the table with some data and make items non-editable
        for row in range(self.ui.tableWidget.rowCount()):
            for column in range(self.ui.tableWidget.columnCount()):
                item = QTableWidgetItem("")
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEditable
                              & ~Qt.ItemFlag.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, column, item)

    def showEvent(self, event):
        self.resize_columns_to_fit()

    def resizeEvent(self, event):
        self.resize_columns_to_fit()

    def resize_columns_to_fit(self):
        width = self.ui.tableWidget.viewport().width()
        column_proportions = [0.45, 0.15]
        wid0 = width * column_proportions[0]
        wid1 = width * column_proportions[1]
        self.ui.tableWidget.setColumnWidth(0, wid0)
        self.ui.tableWidget.setColumnWidth(1, wid1)
        self.ui.tableWidget.setColumnWidth(2, width - wid0 - wid1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWnd()
    window.show()
    sys.exit(app.exec())
