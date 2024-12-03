#!/bin/bash

# Variables
PACKAGE_NAME="RFIDInventory"
VERSION="1.0"
ARCHITECTURE="amd64"
DESCRIPTION="RFID Inventory management software."
MAINTAINER="Your Name <youremail@example.com>"
BUILD_DIR="${PACKAGE_NAME}-${VERSION}"
INSTALL_DIR="${BUILD_DIR}/usr/local/bin"
ICON_DIR="${BUILD_DIR}/usr/share/icons/hicolor/512x512/apps"
DESKTOP_DIR="${BUILD_DIR}/usr/share/applications"
SYSTEMD_DIR="${BUILD_DIR}/etc/systemd/system"
AUTOSTART_DIR="${BUILD_DIR}/etc/xdg/autostart"
CONFIG_DIR="${BUILD_DIR}/opt/${PACKAGE_NAME}/config/systemd/user"
DEBIAN_DIR="${BUILD_DIR}/DEBIAN"

# Clean up previous builds
rm -rf "${BUILD_DIR}"
mkdir -p "${INSTALL_DIR}" "${ICON_DIR}" "${DESKTOP_DIR}" "${SYSTEMD_DIR}" "${AUTOSTART_DIR}" "${CONFIG_DIR}" "${DEBIAN_DIR}"

# Copy application files
echo "Copying application files..."
cp RFIDInventory "${INSTALL_DIR}/"
cp icon.png "${ICON_DIR}/${PACKAGE_NAME}.png"

# Create .desktop file for the application menu
echo "Creating .desktop file..."
cat > "${DESKTOP_DIR}/${PACKAGE_NAME}.desktop" <<EOL
[Desktop Entry]
Version=1.0
Name=RFID Inventory
Comment=Manage RFID inventory system
Exec=${INSTALL_DIR}/RFIDInventory
Icon=${ICON_DIR}/${PACKAGE_NAME}.png
Terminal=false
Type=Application
Categories=Utility;
EOL

# Create autostart .desktop file
echo "Creating autostart .desktop file..."
cat > "${AUTOSTART_DIR}/${PACKAGE_NAME}.desktop" <<EOL
[Desktop Entry]
Version=1.0
Name=RFID Inventory Autostart
Comment=Automatically start RFID Inventory application at login
Exec=${INSTALL_DIR}/RFIDInventory
Icon=${ICON_DIR}/${PACKAGE_NAME}.png
Terminal=false
Type=Application
EOL

# Create systemd service file
echo "Creating systemd service file..."
cat > "${SYSTEMD_DIR}/${PACKAGE_NAME}.service" <<EOL
[Unit]
Description=RFID Inventory Management Service
After=network.target
Wants=display-manager.service

[Service]
User=rfidinv
ExecStart=${INSTALL_DIR}/RFIDInventory
Environment=DISPLAY=:0
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOL

# Create systemd user service file for xhost
echo "Creating systemd user service for xhost..."
cat > "${CONFIG_DIR}/xhost-grant.service" <<EOL
[Unit]
Description=Grant rfidinv user access to X Server

[Service]
Type=oneshot
ExecStart=/usr/bin/xhost +SI:localuser:rfidinv

[Install]
WantedBy=default.target
EOL

# Create DEBIAN control file
echo "Creating DEBIAN control file..."
cat > "${DEBIAN_DIR}/control" <<EOL
Package: ${PACKAGE_NAME}
Version: ${VERSION}
Section: utils
Priority: optional
Architecture: ${ARCHITECTURE}
Maintainer: ${MAINTAINER}
Depends:
Description: ${DESCRIPTION}
EOL

# Create postinst script to configure the system after package installation
echo "Creating postinst script..."
cat > "${DEBIAN_DIR}/postinst" <<'EOL'
#!/bin/bash
set -e

# Create rfidinv user if it doesn't exist
if ! id -u "rfidinv" >/dev/null 2>&1; then
    useradd --system --create-home --home-dir /home/rfidinv --shell /usr/sbin/nologin rfidinv
    echo "rfidinv user has been added with a home directory."
fi

# Setup systemd user service for rfidinv user
USER_HOME=/home/rfidinv
SYSTEMD_USER_DIR=${USER_HOME}/.config/systemd/user
mkdir -p ${SYSTEMD_USER_DIR}
cp /opt/RFIDInventory/config/systemd/user/xhost-grant.service ${SYSTEMD_USER_DIR}/
chown -R rfidinv:rfidinv ${SYSTEMD_USER_DIR}

# Grant X Server access
if [ -n "$DISPLAY" ] && pgrep Xorg > /dev/null; then
    echo "Granting X Server access for the rfidinv user"
    su - rfidinv -s /bin/bash -c "xhost +SI:localuser:rfidinv" || true
else
    echo "X server not accessible. Skipping xhost configuration."
fi

# Enable and start the system service
systemctl daemon-reload
systemctl enable RFIDInventory.service
systemctl start RFIDInventory.service
EOL

# Make the postinst script executable
chmod 0755 "${DEBIAN_DIR}/postinst"

# Build the Debian package
echo "Building the Debian package..."
dpkg-deb --build "${BUILD_DIR}"

# Clean up
echo "Cleaning up..."
rm -rf "${BUILD_DIR}"

echo "Package ${PACKAGE_NAME}-${VERSION}.deb has been created successfully."