@echo off
REM startserverandtunnelscript.bat
REM Version: 1.0

REM Activate the virtual environment
call venv\Scripts\activate

REM Start the Flask server in a new terminal tab
start "Flask Server" cmd /k "python actions_server.py"

REM Wait for 5 seconds to ensure the server starts before LocalTunnel
timeout /t 5

REM Start LocalTunnel in a new terminal tab
start "LocalTunnel" cmd /k "lt --port 5000 --subdomain changethistoyourcustomurl"

REM Print a message indicating the scripts have started
echo The virtual environment, server, and LocalTunnel have been started in separate terminal tabs.