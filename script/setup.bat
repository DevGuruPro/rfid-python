@echo off
:: Check if the script is running with administrative privileges
net session >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process -FilePath '%0' -Verb RunAs"
    exit /b
)

:: Get the directory of the running script
set "SCRIPT_DIR=%~dp0"
set "EXECUTABLE_NAME=main.exe"
set "TASK_NAME=RFID-GPS"

:: Verify if the executable exists
if not exist "%SCRIPT_DIR%\%EXECUTABLE_NAME%" (
    echo Executable "%EXECUTABLE_NAME%" not found in "%SCRIPT_DIR%".
    pause
    exit /b 1
)

:: Create a scheduled task to run at logon with highest privileges
schtasks /create /tn "%TASK_NAME%" /tr "\"%SCRIPT_DIR%%EXECUTABLE_NAME%\"" /sc onlogon /rl highest /f /ru %username%

:: Check if the task was created successfully
if %ERRORLEVEL% EQU 0 (
    echo Task "%TASK_NAME%" created successfully.
) else (
    echo ERROR: Failed to create task. Make sure you're running this script with administrative privileges.
)

pause