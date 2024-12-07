#!/bin/bash

# Update package lists
sudo apt update

# Install development tools and libraries
sudo apt install -y build-essential python3-dev zlib1g-dev libssl-dev libffi-dev libbz2-dev libreadline-dev libncursesw5-dev libsqlite3-dev libgdbm-dev liblzma-dev libc6-dev libx11-dev libxrender-dev libxtst-dev libxi-dev libxt-dev libxcb-xinerama0 libxcb-cursor0 libx11-xcb1 libxcb1 libxfixes3 libxi6 libxrender1 libxcb-render0 libxcb-shape0 libxcb-xfixes0 x11-xserver-utils pkg-config tk-dev

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
