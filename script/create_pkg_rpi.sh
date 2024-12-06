#!/bin/bash

# Define package variables
PACKAGE_NAME=RFIDInventory
PACKAGE_VERSION=1.0
ARCHITECTURE=$(dpkg --print-architecture)
DESCRIPTION="RFID Inventory management software."
MAINTAINER="User"

# Create directory structure
echo "Creating directory structure..."
mkdir -p ${PACKAGE_NAME}-${PACKAGE_VERSION}/DEBIAN
mkdir -p ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/local/bin
mkdir -p ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/share/applications
mkdir -p ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/share/icons/hicolor/512x512/apps
mkdir -p ${PACKAGE_NAME}-${PACKAGE_VERSION}/etc/skel/.config/autostart

# Copy files to package
echo "Copying files..."
cp RFIDInventory ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/local/bin/
cp icon.png ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/share/icons/hicolor/512x512/apps/${PACKAGE_NAME}.png

# Create the monitoring script
echo "Creating monitoring script..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/local/bin/monitor_rfid.sh <<'EOL'
#!/bin/bash

APP_NAME="RFIDInventory"
APP_PATH="/usr/local/bin/RFIDInventory"

while true; do
    if ! pgrep -x "$APP_NAME" > /dev/null; then
        echo "$APP_NAME is not running. Starting..."
        $APP_PATH &
    else
        echo "$APP_NAME is running."
    fi
    sleep 5
done
EOL

chmod +x ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/local/bin/monitor_rfid.sh

# Create .desktop file for application menu
echo "Creating application .desktop file..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/share/applications/${PACKAGE_NAME}.desktop <<EOL
[Desktop Entry]
Version=1.0
Name=RFID Inventory
Comment=Manage RFID inventory system
Exec=/usr/local/bin/RFIDInventory
Icon=${PACKAGE_NAME}
Terminal=false
Type=Application
Categories=Utility;
EOL

# Create autostart entry to run the monitoring script on login
echo "Creating autostart entry..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/etc/skel/.config/autostart/monitor-rfid.desktop <<EOL
[Desktop Entry]
Type=Application
Exec=/usr/local/bin/monitor_rfid.sh
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Monitor RFID Inventory
EOL

# Create control file
echo "Creating DEBIAN control file..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/DEBIAN/control <<EOL
Package: ${PACKAGE_NAME}
Version: ${PACKAGE_VERSION}
Section: utils
Priority: optional
Architecture: ${ARCHITECTURE}
Maintainer: ${MAINTAINER}
Depends: libxcb-xinerama0, libxcb-cursor0, libx11-xcb1, libxcb1, libxfixes3, libxi6, libxrender1, libxcb-render0, libxcb-shape0, libxcb-xfixes0, x11-xserver-utils
Description: ${DESCRIPTION}
EOL

# Create postinst script to set up the environment
echo "Creating postinst script..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/DEBIAN/postinst <<'EOL'
#!/bin/bash

set -e

# Create rfidinv user if it doesn't exist
if ! id -u "rfidinv" >/dev/null 2>&1; then
    useradd --system --create-home --home-dir /home/rfidinv --shell /usr/sbin/nologin rfidinv
    echo "rfidinv user has been added with a home directory."
fi

# Create data directory for RFIDInventory
RFID_DATA_DIR=/var/lib/rfidinventory
if [ ! -d "$RFID_DATA_DIR" ]; then
    mkdir -p "$RFID_DATA_DIR"
    chown -R rfidinv:rfidinv "$RFID_DATA_DIR"
    chmod -R 750 "$RFID_DATA_DIR"
    echo "Created writable directory at $RFID_DATA_DIR for RFIDInventory data."
fi

# Grant X11 access to the rfidinv user
mkdir -p /etc/skel/.config/autostart
cat > /etc/skel/.config/autostart/xhost-grant.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=xhost +SI:localuser:rfidinv
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Grant X Access to rfidinv
EOF

# Ensure existing users receive this setting
for user in /home/*; do
    if [ -d "$user" ]; then
        mkdir -p "$user/.config/autostart"
        cp /etc/skel/.config/autostart/xhost-grant.desktop "$user/.config/autostart/"
        cp /etc/skel/.config/autostart/monitor-rfid.desktop "$user/.config/autostart/"
        chown $(basename "$user"):$(basename "$user") "$user/.config/autostart/"*
    fi
done
EOL

# Make the postinst script executable
chmod 0755 ${PACKAGE_NAME}-${PACKAGE_VERSION}/DEBIAN/postinst

# Build the .deb package
echo "Building the .deb package..."
dpkg-deb --build ${PACKAGE_NAME}-${PACKAGE_VERSION}

# Clean up the build directory
echo "Cleaning up..."
rm -rf ${PACKAGE_NAME}-${PACKAGE_VERSION}

echo "Package ${PACKAGE_NAME}-${PACKAGE_VERSION}.deb has been created successfully."