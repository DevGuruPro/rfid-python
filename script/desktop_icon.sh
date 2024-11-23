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

# Define the location of the .desktop file
desktop_file_path="$HOME/.local/share/applications/$DESKTOP_FILE_NAME"

# Ensure the applications directory exists
mkdir -p "$HOME/.local/share/applications"

# Write the content to the .desktop file
echo "$desktop_file_content" > "$desktop_file_path"

# Make the .desktop file executable
chmod +x "$desktop_file_path"

echo "Desktop entry created: $desktop_file_path"
echo "Icon set to: $ICON_PATH"

# Inform the user that they might need to refresh their desktop environment
echo "You may need to refresh your desktop environment or log out and log back in to see the changes take effect."

