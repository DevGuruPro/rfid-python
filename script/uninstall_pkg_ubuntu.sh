#!/bin/bash  

# Set variables
PACKAGE_NAME="RFIDInventory"
SERVICE_NAME="${PACKAGE_NAME}.service"
SYSTEM_USER="rfidinv"
DATA_DIR="/var/lib/rfidinventory"
AUTOSTART_FILE="xhost-grant.desktop"

# Stop and disable the systemd service
echo "Stopping and disabling systemd service..."
sudo systemctl stop ${SERVICE_NAME}
sudo systemctl disable ${SERVICE_NAME}

# Remove the systemd service file
if [ -f "/etc/systemd/system/${SERVICE_NAME}" ]; then
    echo "Removing systemd service file..."
    sudo rm /etc/systemd/system/${SERVICE_NAME}
fi

# Reload systemd daemon
echo "Reloading systemd daemon..."
sudo systemctl daemon-reload

# Remove the system user and its home directory
if id "${SYSTEM_USER}" >/dev/null 2>&1; then
    echo "Removing system user and its home directory..."
    sudo userdel -r ${SYSTEM_USER}
fi

# Remove the data directory
if [ -d "${DATA_DIR}" ]; then
    echo "Removing data directory..."
    sudo rm -rf ${DATA_DIR}
fi

# Remove autostart entries
echo "Removing autostart entries..."
sudo rm -f /etc/skel/.config/autostart/${AUTOSTART_FILE}
for user in /home/*; do
    if [ -d "$user/.config/autostart" ] && [ -f "$user/.config/autostart/${AUTOSTART_FILE}" ]; then
        rm -f "$user/.config/autostart/${AUTOSTART_FILE}"
    fi
done

# Uninstall the package
echo "Removing package..."
sudo apt purge -y ${PACKAGE_NAME}

echo "Cleanup completed."