#!/bin/bash  

# Define package and service variables  
PACKAGE_NAME=RFIDInventory  
SERVICE_NAME=${PACKAGE_NAME}.service  
AUTOSTART_DESKTOP=${PACKAGE_NAME}.desktop  
SYSTEM_USER=rfidinv  

# Check if the package is installed  
if dpkg -l | grep $PACKAGE_NAME; then  
    echo "Removing the package $PACKAGE_NAME..."  
    sudo dpkg --remove $PACKAGE_NAME  
else  
    echo "Package $PACKAGE_NAME is not installed."  
fi  

# Stop the service if running  
echo "Stopping the systemd service..."  
sudo systemctl stop $SERVICE_NAME  

# Disable the service  
echo "Disabling the systemd service..."  
sudo systemctl disable $SERVICE_NAME  

# Remove the systemd service file  
SERVICE_FILE_PATH=/etc/systemd/system/$SERVICE_NAME  
if [ -f $SERVICE_FILE_PATH ]; then  
    echo "Removing the systemd service file..."  
    sudo rm $SERVICE_FILE_PATH  
else  
    echo "Service file $SERVICE_FILE_PATH not found."  
fi  

# Reload systemd daemon to reflect changes  
echo "Reloading systemd configurations..."  
sudo systemctl daemon-reload  

# Remove autostart entry  
AUTOSTART_PATH=/etc/xdg/autostart/$AUTOSTART_DESKTOP  
if [ -f $AUTOSTART_PATH ]; then  
    echo "Removing autostart entry..."  
    sudo rm $AUTOSTART_PATH  
else  
    echo "Autostart file $AUTOSTART_PATH not found."  
fi  

# Remove the system user if it exists  
if id $SYSTEM_USER &>/dev/null; then  
    echo "Removing the system user $SYSTEM_USER and its home directory..."  
    sudo userdel -r $SYSTEM_USER  
else  
    echo "User $SYSTEM_USER does not exist."  
fi  

echo "Uninstallation completed."