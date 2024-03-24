#! /bin/sh
w="$(cd "$(dirname "$0")" && pwd)"

pyinstaller firefoxprofilemanager.py --windowed --icon ./assets/firefox.ico --onefile --distpath ./dist/linux
# pyinstaller makeshortcut.py --name shortcut --windowed --icon ./assets/shortcut.png --onefile --distpath ./dist/linux
