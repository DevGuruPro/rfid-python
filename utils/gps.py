import threading
import time

import serial
import pynmea2

from PySide6.QtCore import Signal, QThread

from settings import BAUD_RATE_GPS
from utils.logger import logger


class GPS(QThread):

    sig_msg = Signal(bool)

    def __init__(self, port, baud_rate=BAUD_RATE_GPS, current_status=False):
        super().__init__()
        self.port = port
        self.baud_rate = baud_rate
        self._ser = None
        self._b_stop = threading.Event()
        self._data = {}
        self._sdata = [0, 0]
        self.connectivity = current_status

    def _connect(self):
        """Attempts to connect to the GPS module."""
        try:
            _ser = serial.Serial(port=self.port, baudrate=self.baud_rate, timeout=1, write_timeout=1)
            if self.connectivity is False:
                self.connectivity = True
                self.sig_msg.emit(True)
            # logger.info(f"Connected to gps module-{self.port}.")
            return _ser
        except serial.SerialException:
            if self.connectivity is True:
                self.connectivity = False
                self.sig_msg.emit(False)
            # logger.error(f"Failed to connect to gps module-{self.port}: {e}")
            return None

    def read_serial_data(self):
        buffer = self._ser.in_waiting
        if buffer < 80:
            time.sleep(.2)
        line = self._ser.readline().decode('utf-8', errors='ignore').strip()
        if line.startswith('$GNGGA'):
            try:
                msg = pynmea2.parse(line)
                for field in msg.fields:
                    label, attr = field[:2]
                    value = getattr(msg, attr)
                    self._data[attr] = value
            except pynmea2.ParseError:
                self._data = {}
        elif line.startswith('$GPRMC') or line.startswith('$GNRMC'):
            try:
                msg = pynmea2.parse(line)
                speed_knots = msg.spd_over_grnd if msg.spd_over_grnd is not None else 0
                course_degrees = msg.true_course if msg.true_course is not None else 0
                self._sdata = [speed_knots * 1.15078, course_degrees]
            except pynmea2.ParseError:
                # logger.error(f"Parse error: {e}")
                self._sdata = [0, 0]

    def run(self):
        self._ser = self._connect()
        while self._ser is None and not self._b_stop.is_set():
            self._ser = self._connect()

        while not self._b_stop.is_set():
            if self._ser is None:
                self._ser = self._connect()
                time.sleep(.1)
            else:
                try:
                    self.read_serial_data()
                    if self.connectivity is False:
                        self.connectivity = True
                        self.sig_msg.emit(True)
                except Exception:
                    self._data = {}
                    self._sdata = [0, 0]
                    self._ser = None
                    if self.connectivity is True:
                        self.connectivity = False
                        self.sig_msg.emit(False)
                    # logger.error(f"Serial reading error : {er}")

    def stop(self):
        self._b_stop.set()
        self.wait(1)
        self._close_serial()

    def _close_serial(self):
        """Closes the serial connection."""
        if self._ser and self._ser.is_open:
            self._ser.close()
            # logger.info("Serial connection closed.")
        self._ser = None

    def get_data(self):
        """Returns the latest parsed data."""
        return self._data

    def get_sdata(self):
        return self._sdata
