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
mkdir -p ${PACKAGE_NAME}-${PACKAGE_VERSION}/etc/xdg/autostart
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
Exec=RFIDInventory
Icon=${PACKAGE_NAME}
Terminal=false
Type=Application
Categories=Utility;
EOL

# Create .desktop file for autostart
echo "Creating autostart .desktop file..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/etc/xdg/autostart/${PACKAGE_NAME}.desktop <<EOL
[Desktop Entry]
Version=1.0
Name=RFID Inventory Autostart
Comment=Automatically start RFID Inventory application at login
Exec=RFIDInventory
Icon=${PACKAGE_NAME}
Terminal=false
Type=Application
EOL

# Create systemd service file
echo "Creating systemd service file..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/etc/systemd/system/${PACKAGE_NAME}.service <<EOL
[Unit]
Description=RFID Inventory Management Service
After=network.target
After=graphical.target

[Service]
User=rfidinv
ExecStart=/usr/local/bin/RFIDInventory
Environment=QT_DEBUG_PLUGINS=1
Environment=DISPLAY=:0
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=rfidinventory

[Install]
WantedBy=multi-user.target
WantedBy=graphical.target
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
Description: ${DESCRIPTION}
EOL

# Create postinst script for adding rfidinv
echo "Creating postinst script..."
cat > ${PACKAGE_NAME}-${PACKAGE_VERSION}/DEBIAN/postinst <<EOL
#!/bin/bash

# Create rfidinv user if it doesn't exist
if ! id -u "rfidinv" >/dev/null 2>&1; then
    useradd --system --create-home --home-dir /home/rfidinv --shell /usr/sbin/nologin rfidinv
    echo "rfidinv has been added with a home directory."
fi

USER_HOME=$(getent passwd $(logname) | cut -d: -f6)
sudo -u $(logname) xhost +SI:localuser:rfidinv

# Enable and start the service
systemctl daemon-reload
systemctl enable ${PACKAGE_NAME}.service
systemctl start ${PACKAGE_NAME}.service
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