import re
from datetime import datetime
from geopy.distance import geodesic

from settings import BAUD_RATE_GPS
from utils.logger import logger
from geographiclib.geodesic import Geodesic

import serial
import serial.tools.list_ports


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
    except ValueError as e:
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
    except KeyError as e:
        # logger.error(f"Missing key in GPS data: {e}")
        return 0, 0
    except ValueError as e:
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


def find_gps_port():
    serial_ports = [port.device for port in serial.tools.list_ports.comports()]
    for port in serial_ports:
        try:
            # Open each port
            with serial.Serial(port, baudrate=BAUD_RATE_GPS, timeout=1) as ser:
                # Try reading from the port
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line.startswith('$G'):
                    # logger.info(f"GPS found on port: {port}")
                    return port
        except (OSError, serial.SerialException):
            pass  # Ignore if the port can't be opened

    # logger.info("No GPS port found")
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
