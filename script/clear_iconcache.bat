@echo off  
:: Check for administrative privileges  
net session >nul 2>&1  
if not %errorLevel% == 0 (  
    echo.  
    echo Requesting administrative privileges...  
    echo.  
    :: Relaunch the script with administrative privileges  
    powershell -Command "Start-Process '%~f0' -Verb RunAs"  
    exit  
)  

echo This script will clear the Windows icon cache.  
echo You may need to restart your computer for changes to take effect.  
echo.  

echo Stopping Explorer...  
taskkill /f /im explorer.exe  

echo Deleting icon cache files...  
del /a /q "%localappdata%\IconCache.db"  
del /a /f /q "%localappdata%\Microsoft\Windows\Explorer\iconcache*"  

echo Starting Explorer...  
start explorer.exe  

echo.  
echo Icon cache cleared. Please restart your computer if you don't see the expected changes.  
pause