#!/bin/bash

# Update package lists
sudo apt update

# Install development tools and libraries
sudo apt install -y build-essential
sudo apt install -y python3-dev
sudo apt install -y zlib1g-dev
sudo apt install -y libssl-dev
sudo apt install -y libffi-dev
sudo apt install -y libbz2-dev
sudo apt install -y libreadline-dev
sudo apt install -y libsqlite3-dev
sudo apt install -y libncursesw5-dev
sudo apt install -y libgdbm-dev
sudo apt install -y liblzma-dev
sudo apt install -y libc6-dev
sudo apt install -y libx11-dev libxrender-dev libxtst-dev libxi-dev libxt-dev
sudo apt install -y pkg-config
sudo apt install -y tk-dev

# Download and extract Python source
wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz
tar xf Python-3.9.0.tar.xz
cd Python-3.9.0

# Configure and compile Python
./configure --enable-optimizations --enable-shared
sudo make -j $(nproc)
sudo make altinstall

echo "/usr/local/lib" | sudo tee /etc/ld.so.conf.d/python3.9.conf
sudo ldconfig