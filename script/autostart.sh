#!/bin/bash

# Variables
APP_NAME="RFIDInventory"  # Name of your application
CURRENT_DIR=$(pwd)  # Current directory
EXECUTABLE_PATH="$CURRENT_DIR/RFIDInventory"  # Executable in the current directory
ICON_PATH="$CURRENT_DIR/icon.png"  # Icon file in the current directory
DESKTOP_FILE_NAME="${APP_NAME}.desktop"  # Name for the .desktop file

# Create the .desktop file content
desktop_file_content="[Desktop Entry]
Version=1.0
Name=${APP_NAME}
Exec=${EXECUTABLE_PATH}
Icon=${ICON_PATH}
Type=Application
Terminal=false
"

# Define the location of the .desktop file in the applications directory
desktop_applications_path="$HOME/.local/share/applications/$DESKTOP_FILE_NAME"

# Define the location of the .desktop file in the autostart directory
desktop_autostart_path="$HOME/.config/autostart/$DESKTOP_FILE_NAME"

# Ensure the applications directory exists
mkdir -p "$HOME/.local/share/applications"

# Write the content to the .desktop file for applications
echo "$desktop_file_content" > "$desktop_applications_path"

# Make the .desktop file executable for applications
chmod +x "$desktop_applications_path"

echo "Desktop entry created for application list: $desktop_applications_path"

# Ensure the autostart directory exists
mkdir -p "$HOME/.config/autostart"

# Write the content to the .desktop file for autostart
echo "$desktop_file_content" > "$desktop_autostart_path"

# Make the .desktop file executable for autostart
chmod +x "$desktop_autostart_path"

echo "Startup entry created: $desktop_autostart_path"
echo "Icon set to: $ICON_PATH"

# Inform the user that they might need to log out and log back in to see changes
echo "You may need to log out and log back in for the startup change to take effect."