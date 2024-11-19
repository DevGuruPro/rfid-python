# RFID-PYTHON
Software for reading live tag and gps module.

# Set up environment.

- Install python.

  - Windows

    Download [python](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe) and run program(Select the option to add Python to the environment path).
  
  - Ubuntu / Raspberry pi
  
    ```shell
    sudo apt install python3.9
    ```

# Getting Started

- Clone this repository.

    ```shell
    cd ~
    git clone https://github.com/prosperinfotech/rfid-python
    ```
  
- Install python libraries.

    ```shell
    cd rfid-python
    pip install -r requirement.txt
    ```

  - Use this command in Raspberry Pi OS.

    ```shell
    cd rfid-python
    pip install -r requirement.txt --break-system-packages
    ```
    
- And start!

    ```shell
    python main.py
    ```

# Convert a project into an executable(.exe) file

- Install PyInstaller

    ```shell
    pip install pyinstaller
    ```
  
  - Use this command in Raspberry Pi OS.

      ```shell
      pip install pyinstaller --break-system-packages
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
      
  