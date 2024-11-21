#!/bin/bash

# Update package lists
sudo apt update

# Install prerequisites
sudo apt install -y software-properties-common

# Add deadsnakes PPA (contains newer Python versions)
sudo add-apt-repository ppa:deadsnakes/ppa

# Update package lists again after adding new PPA
sudo apt update

# Install Python 3.11
sudo apt install -y python3.11

# Optionally, update alternatives to set Python 3.11 as default
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

echo "Python 3.11 installation completed."

python3 --version