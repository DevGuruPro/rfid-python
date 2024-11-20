#!/bin/bash

# Determine the directory the script is run from
PROJECT_DIR=$(dirname "$(realpath "\$0")")

# Get the path of the executable
EXECUTABLE_PATH="$PROJECT_DIR/main" # Replace 'your_executable' with the actual name of your executable

# Define the systemd service name
SERVICE_NAME="RFID-GPS"

# Create the systemd service file content
SERVICE_CONTENT="[Unit]
Description=Live RFID and GPS data reading Application
After=network.target

[Service]
ExecStart=$EXECUTABLE_PATH
WorkingDirectory=$PROJECT_DIR
Restart=on-failure
User=$(whoami)
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
"

# Save service file
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"

# Request sudo permissions upfront
if [ "$EUID" -ne 0 ]; then
    echo "This script requires administrative privileges. Please run as root or use sudo."
    exit 1
fi

echo "$SERVICE_CONTENT" > "$SERVICE_FILE"
# Set permissions
chmod 644 "$SERVICE_FILE"
# Reload systemd to register the new service
systemctl daemon-reload
# Enable the service to start on boot
systemctl enable "$SERVICE_NAME"
# Start the service immediately
systemctl start "$SERVICE_NAME"
# Check the status of the service
systemctl status "$SERVICE_NAME"