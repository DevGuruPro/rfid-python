# RFID-PYTHON
Software for reading live tag and gps module.

# Set up environment.

- Install python.

  - Windows

    Download [python](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe) and run .exe
  
  - Ubuntu / Raspberry pi
  
    ```shell
    sudo apt install python3.9
    ```
    
- Install python libraries.

    ```shell
    cd CCKC_EOL
    pip install -r requirement.txt
    ```

  - Use this command in Raspberry Pi OS.

    ```shell
    cd CCKC_EOL
    pip install -r requirement.txt --break-system-packages
    ```


# Getting Started

- Clone this repository.

    ```shell
    cd ~
    git clone https://github.com/prosperinfotech/rfid-python
    ```

- And start!

    ```shell
    cd rfid-python
    python main.py
    ```

# Convert a project into an executable(.exe) file

- Install PyInstaller

    ```shell
    pip install pyinstaller
    ```
  
- Navigate to Project Directory

  - Run PyInstaller

    - Windows

      ```shell
      pyinstaller --onefile --add-data "ui/alarm.wav*;ui/alarm.wav" main.py  
      ```
      
    - Ubuntu / MacOS / Raspberry Pi OS
    
      ```shell
      pyinstaller --onefile --add-data "ui/alarm.wav*:ui/alarm.wav" main.py  
      ```
      
  