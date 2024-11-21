import json
import os

_cur_dir = os.path.dirname(os.path.realpath(__file__))

ROOT_DIR = os.path.expanduser('~/.rfid')
os.makedirs(ROOT_DIR, exist_ok=True)

DEFAULT_CONFIG = {

}

CONFIG_FILE = os.path.join(ROOT_DIR, 'config.json')
if not os.path.exists(CONFIG_FILE):
    print("No config found! Creating the default one...")
    with open(CONFIG_FILE, 'w') as jp:
        json.dump(DEFAULT_CONFIG, jp, indent=2)

LOGIN_URL = "https://rfidngpsinventory.com/rfid/user/userLogin"
RECORD_UPLOAD_URL = "https://rfidngpsinventory.com/rfid/mobileApp/updateRfidScanning"
HEALTH_UPLOAD_URL = "https://rfidngpsinventory.com/rfid/dashBoard/rfidapphealth"

DEFAULT_SERIAL_PORT_GPS = 'COM4'
BAUD_RATE_GPS = 115200

RFID_CARD_READER = '169.254.216.147'

SOUND_FREQUENCY = 1000
SOUND_DURATION = 800

try:
    from local_settings import *
except ImportError:
    pass
