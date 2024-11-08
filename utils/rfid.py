import threading
import time

# import serial

from PySide6.QtCore import Signal, QThread

from utils.logger import logger


class RFID(QThread):

    sig_msg = Signal(bool)

    def __init__(self, port='/dev/ttyAMA0', baud_rate=9600):
        super().__init__()
        self.port = port
        self.baud_rate = baud_rate
        self._ser = None
        self._b_stop = threading.Event()
        self._data = {}

    def _connect(self):
        """Attempts to connect to the GPS module."""
        try:
            _ser = serial.Serial(port=self.port, baudrate=self.baud_rate, timeout=1, write_timeout=1)
            self.sig_msg.emit(True)
            logger.info("Connected to simplertk2b module.")
            return _ser
        except serial.SerialException as e:
            self.sig_msg.emit(False)
            logger.error(f"Failed to connect to simplertk2b module: {e}")
            return None

    def read_serial_data(self):
        buffer = self._ser.in_waiting
        if buffer < 80:
            time.sleep(.2)
        line = self._ser.readline().decode('utf-8', errors='ignore').strip()
        print(line)

    def run(self):
        self._ser = self._connect()
        while self._ser is None:
            self._connect()

        while not self._b_stop.is_set():
            try:
                self.read_serial_data()
            except Exception as er:
                logger.error(f"Serial reading error : {er}")
                self._ser.close()
                time.sleep(.1)
                self._ser.open()

    def stop(self):
        self._b_stop.set()
        self.wait()
        self._close_serial()

    def _close_serial(self):
        """Closes the serial connection."""
        if self._ser and self._ser.is_open:
            self._ser.close()
            logger.info("Serial connection closed.")
        self._ser = None

    def get_data(self):
        """Returns the latest parsed data."""
        return self._data


if __name__ == "__main__":
    rfid = RFID()
    rfid.start()
