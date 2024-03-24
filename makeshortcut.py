import sys

from os.path import splitext as _splitext, dirname, join, abspath, isdir
from shutil import move as _move, copyfile, copytree
from shortcut import ShortCutter


platform = sys.platform
isWindows = platform == "win32"
isMacos = platform == "darwin"
APP_EXT = ".exe" if isWindows else ".app" if isMacos else ""
NAME = "Firefox Profile Manager"
__dirname__ = dirname(__file__)

def copy(sourcePath: str, targetPath: str):
    if isdir(sourcePath):
        return copytree(sourcePath, targetPath)
    return copyfile(sourcePath, targetPath)


def crossApp(name: str):
    return f"{name}{APP_EXT}"


def move(sourcePath: str, targetPath: str):
    return _move(sourcePath, targetPath)


def extname(path: str):
    return _splitext(path)[-1]


FIREFOX_PATH = abspath(join(__dirname__, crossApp('firefoxprofilemanager')))
# FIREFOX_PATH = crossApp('firefoxprofilemanager')
s = ShortCutter()
try:
    # if isWindows:
    _, __, shk = s.create_desktop_shortcut(FIREFOX_PATH)
    move(shk, abspath(join(dirname(shk), f"{NAME}{extname(shk)}")))
    _, __, shk = s.create_menu_shortcut(FIREFOX_PATH)
    move(shk, abspath(join(dirname(shk), f"{NAME}{extname(shk)}")))
    # elif isMacos:
    #     copy(FIREFOX_PATH, f'/Applications/{crossApp(NAME)}') 
    # else:
        # ...
except Exception:
    raise Exception("Not exist firefoxprofilemanager!")
