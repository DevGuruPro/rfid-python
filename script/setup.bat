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
set "EXECUTABLE_NAME=RFIDInventory.exe"  
set "MONITOR_SCRIPT=monitor_rfid.bat"  
set "TASK_NAME=RFIDInventoryMonitor"  

:: Verify if the executable exists  
if not exist "%SCRIPT_DIR%\%EXECUTABLE_NAME%" (  
    echo Executable "%EXECUTABLE_NAME%" not found in "%SCRIPT_DIR%".  
    pause  
    exit /b 1  
)  

:: Create the monitoring script  
echo @echo off > "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo set APP_PATH="%SCRIPT_DIR%\\%EXECUTABLE_NAME%" >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo set APP_NAME=%EXECUTABLE_NAME% >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo :loop >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo tasklist /fi "imagename eq %%APP_NAME%%" 2^> NUL ^| find /I /N "%%APP_NAME%%" ^> NUL >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo if %%ERRORLEVEL%% == 1 ( >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo    echo %%APP_NAME%% is not running, starting... >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo    start "" %%APP_PATH%% >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo ) else ( >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo    echo %%APP_NAME%% is already running. >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo ) >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo timeout /t 10 > NUL >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  
echo goto loop >> "%SCRIPT_DIR%\%MONITOR_SCRIPT%"  

:: Create a scheduled task to run the monitoring script at logon with highest privileges  
schtasks /create /tn "%TASK_NAME%" /tr "\"%SCRIPT_DIR%%MONITOR_SCRIPT%\"" /sc onlogon /rl highest /f /ru %username%  

:: Check if the task was created successfully  
if %ERRORLEVEL% EQU 0 (  
    echo Task "%TASK_NAME%" created successfully, to monitor and restart "%EXECUTABLE_NAME%".  
) else (  
    echo ERROR: Failed to create task. Make sure you're running this script with administrative privileges.  
)  

pause