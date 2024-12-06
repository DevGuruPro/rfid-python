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
mkdir -p ${PACKAGE_NAME}-${PACKAGE_VERSION}/etc/systemd/system

# Copy files to package
echo "Copying files..."
cp RFIDInventory ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/local/bin/
cp icon.png ${PACKAGE_NAME}-${PACKAGE_VERSION}/usr/share/icons/hicolor/512x512/apps/${PACKAGE_NAME}.png

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

# Create systemd service file
echo "Creating systemd service file..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/etc/systemd/system/${PACKAGE_NAME}.service <<EOL
[Unit]
Description=RFID Inventory Management Service
After=network.target

[Service]
User=%i
WorkingDirectory=/var/lib/rfidinventory
ExecStart=/usr/local/bin/RFIDInventory
Environment=QT_DEBUG_PLUGINS=1
Environment=DISPLAY=:0
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal
SyslogIdentifier=rfidinventory

[Install]
WantedBy=multi-user.target
EOL

# Create DEBIAN control file
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

# Create the postinst script to configure system
echo "Creating postinst script..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/DEBIAN/postinst <<'EOL'
#!/bin/bash

set -e

# Debugging: Print the package name
echo "Package Name: RFIDInventory"

# Get the username of the person who installed the package
INSTALL_USER=$(logname)

# Create data directory for RFIDInventory
RFID_DATA_DIR=/var/lib/rfidinventory
if [ ! -d "$RFID_DATA_DIR" ]; then
    mkdir -p "$RFID_DATA_DIR"
    chown -R "$INSTALL_USER":"$INSTALL_USER" "$RFID_DATA_DIR"
    chmod -R 750 "$RFID_DATA_DIR"
    echo "Created writable directory at $RFID_DATA_DIR for RFIDInventory data."
fi

# Create autostart directory if not exist
mkdir -p /etc/skel/.config/autostart
cat > /etc/skel/.config/autostart/xhost-grant.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=xhost +SI:localuser:$INSTALL_USER
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Grant X Access to $INSTALL_USER
EOF

# Ensure that existing users receive this setting
for user in /home/*; do
    if [ -d "$user" ]; then
        mkdir -p "$user/.config/autostart"
        cp /etc/skel/.config/autostart/xhost-grant.desktop "$user/.config/autostart/"
        chown $(basename "$user"):$(basename "$user") "$user/.config/autostart/xhost-grant.desktop"
    fi
done

# Enable systemd services
echo "Enabling service: RFIDInventory.service"
systemctl daemon-reload
systemctl enable RFIDInventory.service
systemctl start RFIDInventory.service
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