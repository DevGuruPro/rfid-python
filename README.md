# RFID-GPS-INVENTORY
Software for reading live rfid tag and gps module.

# Set up environment-Install python.

- Windows

  Download [python](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe) and run .exe file(Select the option to add Python to the environment path).
  
- Ubuntu / Raspberry pi
  
  ```shell
  sudo apt install python3.11
  ```

# Getting Started.

- Clone this repository.

    ```shell
    cd ~
    git clone https://github.com/prosperinfotech/rfid-python
    ```
  
- Install python libraries.

  - Windows / Ubuntu
  
    ```shell
    cd rfid-python
    pip install -r requirement.txt
    ```

  - Raspberry Pi OS

    ```shell
    cd rfid-python
    pip install -r requirement.txt --break-system-packages
    ```
    
- And start!

    ```shell
    python main.py
    ```

# Convert a project into an executable file.

- Install PyInstaller

  - Windows / Ubuntu

    ```shell
    pip install pyinstaller
    ```
  
  - Raspberry Pi OS.

      ```shell
      pip install pyinstaller --break-system-packages
      ```
  
- Navigate to project directory and run PyInstaller

  - Windows

    ```shell
    pyinstaller --onefile --windowed --icon=icon.ico --name=RFIDInventory main.py
    ```
    
    If icon doesn't change, run "script/clear_iconcache.bat" and restart to refresh the icon cache.
      
  - Ubuntu / Raspberry Pi OS
    
    ```shell
    pyinstaller --onefile --icon=icon.png --name=RFIDInventory main.py
    ```
    
    If icon doesn't change, run "script/clear_iconcache.sh" with sudo and restart to refresh the icon cache.
    
# Run the program at startup.

  - Windows
    
    - Place "script/setup.bat" in the same directory as "main.exe" and run batch script.

  - Ubuntu / Raspberry Pi
    
    - Place "script/setup.sh" in the same directory as "main" executable file and run shell script.