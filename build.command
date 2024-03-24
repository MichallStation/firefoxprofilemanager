#! /bin/sh
w="$(cd "$(dirname "$0")" && pwd)"

./.venv/bin/pyinstaller firefoxprofilemanager.py --windowed --icon ./assets/firefox.icns --onefile --distpath ./dist/darwin
# ./.venv/bin/pyinstaller makeshortcut.py --name shortcut --windowed --icon ./assets/shortcut.icns --onefile --distpath ./dist/darwin
