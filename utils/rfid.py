import threading
import time

from PySide6.QtCore import QThread, Signal
from sllurp.llrp import LLRP_DEFAULT_PORT, LLRPReaderConfig, LLRPReaderClient

from argparse import ArgumentParser

from settings import RFID_CARD_READER
from ping3 import ping
from utils.logger import logger


def convert_to_unicode(obj):
    """
    Tornado dict to json expects unicode strings in dict.
    """
    if isinstance(obj, dict):
        return {
            convert_to_unicode(key):
                convert_to_unicode(value) for key, value in obj.items()
        }
    elif isinstance(obj, list):
        return [convert_to_unicode(element) for element in obj]
    elif isinstance(obj, bytes):
        return obj.decode('utf-8')
    else:
        return obj


def parse_args(rfid_host):
    parser = ArgumentParser(description='Simple RFID Reader Inventory')
    parser.add_argument('host', help='hostname or IP address of RFID reader', default=[rfid_host],
                        nargs='*')
    parser.add_argument('-p', '--port', default=LLRP_DEFAULT_PORT, type=int,
                        help='port to connect to (default {})'
                        .format(LLRP_DEFAULT_PORT))
    parser.add_argument('-n', '--report-every-n-tags', default=1, type=int,
                        dest='every_n', metavar='N',
                        help='issue a TagReport every N tags')
    parser.add_argument('-a', '--antennas', default='1',
                        help='comma-separated list of antennas to enable')
    parser.add_argument('-X', '--tx-power', default=0, type=int,
                        dest='tx_power',
                        help='Transmit power (default 0=max power)')
    parser.add_argument('-M', '--modulation', default='M8',
                        help='modulation (default M8)')
    parser.add_argument('-T', '--tari', default=0, type=int,
                        help='Tari value (default 0=auto)')
    parser.add_argument('-s', '--session', type=int, default=1,
                        help='Gen2 session (default 2)')
    parser.add_argument('--mode-identifier', type=int,
                        help='ModeIdentifier value')
    parser.add_argument('-P', '--tag-population', type=int, default=4,
                        help="Tag Population value (default 4)")
    parser.add_argument('--impinj-search-mode', choices=['1', '2'],
                        help=('Impinj extension: inventory search mode '
                              '(1=single, 2=dual)'))
    parser.add_argument('--impinj-reports', type=bool, default=False,
                        help='Enable Impinj tag report content (Phase angle, '
                             'RSSI, Doppler)')
    return parser.parse_args()


class RFID(QThread):

    sig_msg = Signal(int)

    def __init__(self):
        super().__init__()
        self._b_stop = threading.Event()
        self.tag_data = None
        self.connectivity = None
        self.reader = None
        self.host = RFID_CARD_READER
        self.set_reader(RFID_CARD_READER, False)

    def set_reader(self, port, status):
        self.connectivity = status
        self.host = port
        args = parse_args(port)
        enabled_antennas = [int(x.strip()) for x in args.antennas.split(',')]
        factory_args = dict(
            report_every_n_tags=args.every_n,
            antennas=enabled_antennas,
            tx_power=args.tx_power,
            tari=args.tari,
            session=args.session,
            mode_identifier=args.mode_identifier,
            tag_population=args.tag_population,
            start_inventory=True,
            tag_content_selector={
                'EnableROSpecID': True,
                'EnableSpecIndex': True,
                'EnableInventoryParameterSpecID': True,
                'EnableAntennaID': True,
                'EnableChannelIndex': True,
                'EnablePeakRSSI': True,
                'EnableFirstSeenTimestamp': True,
                'EnableLastSeenTimestamp': True,
                'EnableTagSeenCount': True,
                'EnableAccessSpecID': True,
                'C1G2EPCMemorySelector': {
                    'EnableCRC': True,
                    'EnablePCBits': True,
                }
            },
            impinj_search_mode=args.impinj_search_mode,
            impinj_tag_content_selector=None,
        )

        host = args.host[0]
        if ':' in host:
            host, port = host.split(':', 1)
            port = int(port)
        else:
            port = args.port
        config = LLRPReaderConfig(factory_args)
        self.reader = LLRPReaderClient(host, port, config)
        self.reader.add_tag_report_callback(self.tag_seen_callback)
        logger.debug("RFID initialized.")

    # def _connect_reader(self):
    #     for reader in self.reader_clients:
    #         try:
    #             reader.connect()
    #             logger.debug("RFID connected.")
    #         except ReaderConfigurationError as e:
    #             if "Not connected" in str(e):
    #                 logger.error("Not connected")
    #                 if self.connectivity is True:
    #                     self.connectivity = False
    #                     self.sig_msg.emit(2)
    #             elif "Already connected" in str(e):
    #                 reader.disconnect()
    #                 logger.error("#####")
    #                 if self.connectivity is False:
    #                     self.connectivity = True
    #                     self.sig_msg.emit(1)
    #             else:
    #                 logger.error(f"rfid configuration error:{e}")
    #                 if self.connectivity is True:
    #                     self.connectivity = False
    #                     self.sig_msg.emit(2)
    #             return
    #         except Exception as e:
    #             logger.error(f"rfid connection error:{e}")
    #             if self.connectivity is True:
    #                 self.connectivity = False
    #                 self.sig_msg.emit(2)
    #             return
    #     if self.connectivity is False:
    #         self.connectivity = True
    #         self.sig_msg.emit(1)

    def tag_seen_callback(self, reader, tags):
        """Function to run each time the reader reports seeing tags."""
        if tags:
            self.tag_data = convert_to_unicode(tags)
            self.sig_msg.emit(3)

    def run(self):
        while not self._b_stop.is_set():
            try:
                self.reader.connect()
                break
            except Exception:
                if self.connectivity is True:
                    self.connectivity = False
                    self.sig_msg.emit(2)
            time.sleep(.1)

        if self.connectivity is False:
            self.connectivity = True
            self.sig_msg.emit(1)

        while not self._b_stop.is_set():
            try:
                response_time = ping(self.host, timeout=3)
                if response_time:
                    if self.connectivity is False:
                        self.reader = None
                        self.set_reader(self.host, True)
                        self.reader.connect()
                        self.sig_msg.emit(1)
                else:
                    if self.connectivity is True:
                        self.connectivity = False
                        self.sig_msg.emit(2)
            except Exception:
                if self.connectivity is True:
                    self.connectivity = False
                    self.sig_msg.emit(2)
            time.sleep(.1)

    def stop(self):
        self._b_stop.set()
        self.wait()
        LLRPReaderClient.disconnect_all_readers()
