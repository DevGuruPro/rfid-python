import sched
import sys
import threading
import time

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidget, QTableWidgetItem, QLabel

from settings import SERIAL_PORT_GPS, BAUD_RATE_GPS
from ui.ui_main import Ui_MainWindow
from utils.commons import extract_from_gps

from utils.gps import GPS


class MainWnd(QMainWindow):

    def __init__(self):
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
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable & ~Qt.ItemFlag.ItemIsEditable
                              & ~Qt.ItemFlag.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, column, item)
        # self.ui.tableWidget.item(0, 0).setText("004837065827700000000333 - 1")
        # self.ui.tableWidget.item(0, 4).setText("5/20/2024 11:09:35 PM")
        self.gps = GPS(port=SERIAL_PORT_GPS, baud_rate=BAUD_RATE_GPS)
        self.gps.sig_msg.connect(self.show_gps_status)
        self.gps.start()

        self.scheduler_thread = threading.Thread(target=self.start_scheduler)
        self.scheduler_thread.start()
        self._stop = threading.Event()

    def start_scheduler(self):
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(0, 1, self.schedule_function, (scheduler,))

    def schedule_function(self, scheduler):
        if not self._stop.is_set():
            self.read_data()
            scheduler.enter(0.1, 1, self.scheduler_thread, (scheduler,))

    def read_data(self):
        lat, lon = extract_from_gps(self.gps.get_data())

    def show_gps_status(self, status):
        if status:
            self.ui.gps_connection_status.setText("Connected")
        else:
            self.ui.gps_connection_status.setText("Disconnected")

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
        self.ui.tableWidget.setColumnWidth(4, width-wid)
        height = self.ui.tableWidget.viewport().height()
        for i in range(5):
            self.ui.tableWidget.setRowHeight(i, height/6)
        self.ui.tableWidget.setRowHeight(5, height-int(height/6)*5)

    def closeEvent(self, event):
        self.gps.stop()
        self._stop.set()
        self.scheduler_thread.join(.1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWnd()
    window.show()
    sys.exit(app.exec())
