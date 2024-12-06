#!/bin/bash  

PACKAGE_NAME=RFIDInventory

echo "Uninstalling ${PACKAGE_NAME}..."

# Remove the package using dpkg
sudo dpkg --remove ${PACKAGE_NAME}

# Remove configuration files if any exist
echo "Cleaning up configuration files..."
sudo apt-get purge ${PACKAGE_NAME}

# Remove specific directories and files created during installation
echo "Removing application files and directories..."
sudo rm -f /usr/local/bin/RFIDInventory
sudo rm -f /usr/local/bin/monitor_rfid.sh
sudo rm -f /usr/share/applications/${PACKAGE_NAME}.desktop
sudo rm -f /usr/share/icons/hicolor/512x512/apps/${PACKAGE_NAME}.png

# Remove any lingering data directories
RFID_DATA_DIR=/var/lib/rfidinventory
if [ -d "$RFID_DATA_DIR" ]; then
    sudo rm -rf "$RFID_DATA_DIR"
    echo "Removed data directory $RFID_DATA_DIR."
fi

# Clean up autostart entries
echo "Removing autostart entries..."
find /home/*/.config/autostart -name "monitor-rfid.desktop" -exec rm -f {} \;

echo "Cleanup complete. ${PACKAGE_NAME} has been uninstalled successfully."