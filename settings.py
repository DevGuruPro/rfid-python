import json
import os

_cur_dir = os.path.dirname(os.path.realpath(__file__))

ROOT_DIR = os.path.expanduser('~/.as')
os.makedirs(ROOT_DIR, exist_ok=True)

DEFAULT_CONFIG = {

}

CONFIG_FILE = os.path.join(ROOT_DIR, 'config.json')
if not os.path.exists(CONFIG_FILE):
    print("No config found! Creating the default one...")
    with open(CONFIG_FILE, 'w') as jp:
        json.dump(DEFAULT_CONFIG, jp, indent=2)

LOGIN_URL = "https://rfidngpsinventory.com/rfid/user/userLogin"

SERIAL_PORT_GPS = '/dev/ttyAMA0'
BAUD_RATE_GPS = 115200


try:
    from local_settings import *
except ImportError:
    pass
