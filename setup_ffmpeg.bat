@echo off  
setlocal  

:: Define the URL for downloading FFmpeg  
set "ffmpeg_url=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"  

:: Define the destination directory  
set "install_dir=C:\ffmpeg"  

:: Download FFmpeg using PowerShell  
echo Downloading FFmpeg...  
powershell -Command "Invoke-WebRequest -Uri %ffmpeg_url% -OutFile ffmpeg.zip"  

:: Create install directory if it doesn't exist  
if not exist "%install_dir%" mkdir "%install_dir%"  

:: Extract FFmpeg  
echo Extracting FFmpeg...  
powershell -Command "Expand-Archive -Path ffmpeg.zip -DestinationPath %install_dir% -Force"  

:: Find the extracted directory name dynamically  
for /d %%d in ("%install_dir%\*") do (  
    set "extracted_dir=%%d"  
)  

:: Add FFmpeg to PATH  
echo Setting environment path...  
setx PATH "%extracted_dir%\bin;%PATH%"  

:: Clean up  
del ffmpeg.zip  

echo FFmpeg installation and setup complete.  
endlocal