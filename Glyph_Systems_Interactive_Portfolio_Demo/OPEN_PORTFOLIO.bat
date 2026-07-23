@echo off
setlocal
cd /d "%~dp0"
set PORT=8765
start "Glyph Systems Portfolio Server" /min py -m http.server %PORT% --bind 127.0.0.1
ping 127.0.0.1 -n 3 >nul
start "" "http://127.0.0.1:%PORT%/index.html"
exit /b
