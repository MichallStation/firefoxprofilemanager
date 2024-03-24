@echo off
setlocal
set "w=%~dp0"
set "w=%w:~0,-1%"
%w%\.venv\Scripts\pyinstaller.exe firefoxprofilemanager.py --windowed --icon ./assets/firefox.ico --onefile --distpath ./dist/win32
%w%\.venv\Scripts\pyinstaller.exe makeshortcut.py --name shortcut --windowed --icon ./assets/shortcut.ico --onefile --distpath ./dist/win32
endlocal
