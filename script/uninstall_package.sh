#!/bin/bash  

# Variables  
APP_NAME="RFIDInventory"  # Name of your application  
DESKTOP_FILE_NAME="${APP_NAME}.desktop"  # Name for the .desktop file  

# Define the location of the .desktop file in the applications directory  
desktop_applications_path="$HOME/.local/share/applications/$DESKTOP_FILE_NAME"  

# Define the location of the .desktop file in the autostart directory  
desktop_autostart_path="$HOME/.config/autostart/$DESKTOP_FILE_NAME"  

# Remove the .desktop file for applications  
if [ -f "$desktop_applications_path" ]; then  
    rm "$desktop_applications_path"  
    echo "Removed application list entry: $desktop_applications_path"  
else  
    echo "No application list entry found at: $desktop_applications_path"  
fi  

# Remove the .desktop file for autostart  
if [ -f "$desktop_autostart_path" ]; then  
    rm "$desktop_autostart_path"  
    echo "Removed startup entry: $desktop_autostart_path"  
else  
    echo "No startup entry found at: $desktop_autostart_path"  
fi

# Inform the user that they might need to log out and log back in to see changes  
echo "The application and startup entries have been removed."

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

sudo apt remove rfidinventory

# Remove the system user if desired
echo "Removing system user..."
if id -u "${SYSTEM_USER}" >/dev/null 2>&1; then
    sudo userdel -r ${SYSTEM_USER}
    echo "System user ${SYSTEM_USER} removed."
else
    echo "System user ${SYSTEM_USER} does not exist."
fi

echo "Uninstallation of ${PACKAGE_NAME} completed."