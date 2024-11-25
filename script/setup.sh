#!/bin/bash

# Update package lists
sudo apt update
echo "Package lists updated."

# Install prerequisites
sudo apt install -y software-properties-common
echo "Prerequisite packages installed."

# Add deadsnakes PPA (contains newer Python versions)
sudo add-apt-repository -y ppa:deadsnakes/ppa

# Update package lists after adding new PPA
sudo apt update

# Install Python 3.11
sudo apt install -y python3.11
echo "Python 3.11 installed."

# Install python3.11-apt for Python 3.11
sudo apt install -y python3.11-apt
echo "python3.11-apt installed."

# Optionally, update alternatives to set Python 3.11 as default
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
echo "Python 3.11 set as default Python 3 interpreter."

# Verify Python version
python3 --version

# Clean up unnecessary packages and caches
sudo apt-get autoremove -y
sudo apt-get clean

# Final package update
sudo apt update
sudo apt install -y libc6
echo "Final updates and libc6 package installed."

echo "Python 3.11 installation and configuration complete."

# Verifying apt_pkg module
echo "Testing apt_pkg import..."
python3.11 -c "import apt_pkg; print('apt_pkg module is available.')"