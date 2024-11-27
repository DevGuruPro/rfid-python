# RFID-GPS-INVENTORY
Software for reading live rfid tag and gps module.

# Set up environment-Install python.

- Windows

  Download [python](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe) and run .exe file(Select the option to add Python to the environment path).
  
- Ubuntu / Raspberry pi
  
  ```shell
  bash script/install_python.sh
  ```

# Getting Started.

- Clone this repository.

    ```shell
    cd ~
    git clone https://github.com/prosperinfotech/rfid-python
    ```
  
- Install python libraries.

  - Windows
  
    ```shell
    cd rfid-python
    pip install -r requirements.txt
    ```

  - Ubuntu / Raspberry Pi OS

    ```shell
    cd rfid-python
    python3.9 -m venv .venv
    source .venv/bin/activate
    python3.9 -m pip install --upgrade pip
    pip3.9 install -r requirements.txt
    ```
    
- And start!
  
  - Windows
  
    ```shell
    python main.py
    ```
    
  - Ubuntu / Raspberry Pi OS

    ```shell
    python3.9 main.py
    ```

# Convert a project into an executable file.

- Install PyInstaller

  - Windows
  
    ```shell
    pip install pyinstaller
    ```
    
  - Ubuntu / Raspberry Pi OS

    ```shell
    pip3.9 install pyinstaller
    ```
    
- Navigate to project directory and run PyInstaller

  - Windows

    ```shell
    pyinstaller --clean --onefile --windowed --icon=icon.ico --name=RFIDInventory main.py
    ```
    
    If icon doesn't change, run "script/clear_iconcache.bat" and restart to refresh the icon cache.
      
  - Ubuntu / Raspberry Pi OS (must build on lowest glibc version.)

    ```shell
    sudo apt update
    sudo apt upgrade
    pyinstaller --clean --onefile --icon=icon.png --name=RFIDInventory main.py
    ```
    
    If icon doesn't change
    - Ensure script/desktop_icon.sh, the RFIDInventory executable and icon.png are in the same directory.
    - Run "bash desktop_icon.sh".
    - Reboot and check your application list.
    
# Run the program at startup.

  - Windows
    
    - Place "script/setup.bat" in the same directory as "main.exe" and run batch script.

  - Ubuntu / Raspberry Pi
    
    - Ensure script/autostart.sh, the RFIDInventory executable and icon.png are in the same directory.
    - Run "bash autostart.sh".
    - Reboot!

# Generate package on ubuntu.

  - Ensure script/create_package.sh, the RFIDInventory executable and icon.png are in the same directory.
  - Run "bash create_package.sh".
  - Run "sudo dpkg -i RFIDInventory-1.0.deb" to install the package.
  - Reboot!