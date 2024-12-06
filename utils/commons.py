import re
import time
from datetime import datetime
from geopy.distance import geodesic

from settings import BAUD_RATE_GPS, PORT_WRITE, PORT_READ
from geographiclib.geodesic import Geodesic

import serial
import serial.tools.list_ports
import uuid
from utils.logger import logger

def convert_to_decimal(coord, direction, is_latitude):
    try:
        sign = -1 if direction in ['S', 'W'] else 1
        if is_latitude:
            if len(coord) < 4:
                raise ValueError("Invalid latitude coordinate format")
            degrees = int(coord[:2])
            minutes = float(coord[2:])
        else:
            if len(coord) < 5:
                raise ValueError("Invalid longitude coordinate format")
            degrees = int(coord[:3])
            minutes = float(coord[3:])
        decimal_coord = sign * (degrees + minutes / 60)
        return decimal_coord
    except ValueError:
        # logger.error(f"Error converting coordinate: {e}")
        return 0


def extract_from_gps(gps_data):
    if gps_data == {}:
        return 0, 0
    try:
        # Extract and convert latitude and longitude
        latitude = convert_to_decimal(gps_data['lat'], gps_data['lat_dir'], is_latitude=True)
        longitude = convert_to_decimal(gps_data['lon'], gps_data['lon_dir'], is_latitude=False)
        return latitude, longitude
    except KeyError:
        # logger.error(f"Missing key in GPS data: {e}")
        return 0, 0
    except ValueError:
        # logger.error(f"Error: {e}")
        return 0, 0


def get_date_from_utc(timestamp_microseconds):
    timestamp_seconds = timestamp_microseconds / 1_000_000

    # Create a datetime object from the timestamp
    utc_datetime = datetime.utcfromtimestamp(timestamp_seconds)

    # Format the datetime object to the desired format
    # Using zero stripping manually for cross-platform compatibility
    formatted_date = "{}/{}/{} {}:{}:{} {}".format(
        utc_datetime.month,  # Month without leading zero
        utc_datetime.day,  # Day without leading zero
        utc_datetime.year,  # Full year
        utc_datetime.hour % 12 or 12,  # Hour in 12-hour format, ensuring 0 becomes 12
        f"{utc_datetime.minute:02}",  # Minute with leading zero
        f"{utc_datetime.second:02}",  # Second with leading zero
        "AM" if utc_datetime.hour < 12 else "PM"
    )
    return formatted_date


def calculate_speed_bearing(lat1, lon1, time1, lat2, lon2, time2):
    # Calculate the distance in meters
    distance = geodesic((lat1, lon1), (lat2, lon2)).meters

    # Calculate the time difference in seconds
    time_diff = (time2 - time1) / 1_000_000

    # Calculate speed in m/s
    if time_diff > 0:
        speed = distance / time_diff
    else:
        speed = 0  # If time difference is 0, speed is undefined or considered 0
    return speed * 2.23694, Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)['azi1']


def is_ipv4_address(ip):
    # Regular expression for validating an IPv4 address
    ipv4_regex = re.compile(r'^(?:\d{1,3}\.){3}\d{1,3}$')
    # Check if the input matches the IPv4 address pattern
    if ipv4_regex.match(ip):
        # Split the input into parts and check if each part is between 0 and 255
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False


def get_mac_address():
    mac_address = hex(uuid.getnode())

    # Format the MAC address to be more human-readable and uppercase
    mac_address = mac_address[2:]  # Remove the '0x' prefix
    formatted_mac_address = ':'.join(mac_address[i:i + 2] for i in range(0, len(mac_address), 2)).upper()
    return formatted_mac_address


def find_gps_port():
    serial_ports = [port.device for port in serial.tools.list_ports.comports()]
    logger.debug(f"Available ports:{serial_ports}")

    for port in serial_ports:
        try:
            with serial.Serial(port, baudrate=BAUD_RATE_GPS, timeout=1, rtscts=True, dsrdtr=True) as serw:
                serw.write('AT+QGPS=1\r'.encode())
                logger.debug(f"AT-{port}")
                serw.close()
                time.sleep(.5)
        except (OSError, serial.SerialException):
            pass  # Ignore if the port can't be opened

    for port in serial_ports:
        try:
            # Open each port
            with serial.Serial(port, baudrate=BAUD_RATE_GPS, timeout=1) as ser:
                buffer = ser.in_waiting
                if buffer < 80:
                    time.sleep(.2)
                # Try reading from the port
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                logger.debug(line)
                if line.startswith('$G'):
                    logger.info(f"GPS found on port: {port}")
                    return port
        except (OSError, serial.SerialException):
            pass  # Ignore if the port can't be opened

    logger.info("No GPS port found")
    return None


def find_smallest_available_id(used_ids):
    smallest_available_id = 1
    for record in used_ids:
        current_id = record[0]
        if current_id == smallest_available_id:
            smallest_available_id += 1
        else:
            break
    return smallest_available_id


def convert_formatted_payload(chunk):
    data_list_default = []
    data_list_custom = []
    for row in chunk:
        default_data = {
            "tag": row[1],
            "ant": row[2],
            "rssi": row[3],
            "lat": row[4],
            "lng": row[5],
            "speed": row[6],
            "heading": row[7],
            "locationCode": row[8],
            "userName": row[9],
            'macAddress': get_mac_address()
        }
        custom_data = {}
        for idx in range(10, 17, 2):
            key, value = row[idx], row[idx + 1]
            if key and value:
                custom_data[key] = value
        custom_data = default_data | custom_data
        data_list_default.append(default_data)
        data_list_custom.append(custom_data)
    return {"data": data_list_default}, {"data": data_list_custom}
