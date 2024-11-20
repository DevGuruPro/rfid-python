# RFID-PYTHON
Software for reading live tag and gps module.

# Set up environment-Install python.

- Windows

  Download [python](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe) and run program(Select the option to add Python to the environment path).
  
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
    pyinstaller --onefile --add-data "ui/alarm.wav;ui/alarm.wav" --windowed --icon=icon.ico main.py
    ```
    
    If the icon remains unchanged, ensure "script/clear_iconcache.bat" is in the same directory as the executable file, run it and restart to refresh the icon cache.
      
  - Ubuntu / Raspberry Pi OS
    
    ```shell
    pyinstaller --onefile --add-data "ui/alarm.wav*:ui/alarm.wav" --windowed --icon=icon.ico main.py  
    ```
    
    If the icon remains unchanged, ensure "script/clear_iconcache.sh" is in the same directory as the executable file, run it with sudo and restart to refresh the icon cache.
 
    - Install/Update libc6 package.
    
      ```shell
      sudo apt-get update
      sudo apt-get install libc6
      ```
      
    
# Run the program at startup.

  - Windows
    
    - Place "setup.bat" in the same directory as "main.exe" and run batch script.

  - Ubuntu / Raspberry Pi
    
    - Place "setup.sh" in the same directory as "main" and run shell script with sudo.