#!/bin/bash  

# Function to check if the script is run as root  
function check_root() {  
    if [ "$(id -u)" -ne 0 ]; then  
        echo "This script must be run as root. Attempting to restart with sudo..."  
        exec sudo bash "\$0" "$@"  
        exit  
    fi  
}  

# Check for root privileges  
check_root  

echo "This script will clear specific system caches."  
echo "You may need to restart your system for changes to take effect."  
echo  

# Example of clearing a specific cache directory  
echo "Clearing thumbnail cache..."  
rm -rf ~/.cache/thumbnails/*  

# Add more cache clearing or administrative tasks as needed  
echo "Clearing APT cache..."  
apt-get clean  

echo "Clearing systemd journal logs (keeping the last 100M)..."  
journalctl --vacuum-size=100M  

echo "Cache cleared. You can restart your computer if necessary."