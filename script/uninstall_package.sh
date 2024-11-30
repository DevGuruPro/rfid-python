#!/bin/bash  

# Define package variables
PACKAGE_NAME="RFIDInventory"
SYSTEM_USER="rfidinv"

# Stop and disable the systemd service
echo "Stopping and disabling the systemd service..."
if systemctl is-active --quiet ${PACKAGE_NAME}.service; then
    sudo systemctl stop ${PACKAGE_NAME}.service
fi
sudo systemctl disable ${PACKAGE_NAME}.service
sudo systemctl daemon-reload

# Remove systemd service file
echo "Removing systemd service file..."
sudo rm -f /etc/systemd/system/${PACKAGE_NAME}.service

# Remove autostart .desktop file
echo "Removing autostart .desktop file..."
sudo rm -f /etc/xdg/autostart/${PACKAGE_NAME}.desktop

# Remove application .desktop file
echo "Removing application .desktop file..."
sudo rm -f /usr/share/applications/${PACKAGE_NAME}.desktop

# Remove icon file
echo "Removing icon file..."
sudo rm -f /usr/share/icons/hicolor/512x512/apps/${PACKAGE_NAME}.png

# Remove the executable
echo "Removing executable..."
sudo rm -f /usr/local/bin/${PACKAGE_NAME}

# Remove the system user if desired
echo "Removing system user..."
if id -u "${SYSTEM_USER}" >/dev/null 2>&1; then
    sudo userdel -r ${SYSTEM_USER}
    echo "System user ${SYSTEM_USER} removed."
else
    echo "System user ${SYSTEM_USER} does not exist."
fi

echo "Uninstallation of ${PACKAGE_NAME} completed."