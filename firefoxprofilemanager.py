import subprocess
import sys
from os import getcwd, environ
from os.path import (
    exists as exist,
    dirname,
)

platform = sys.platform
isWindows = platform == "win32"
isMacos = platform == "darwin"
PWD = getcwd()
__dirname__ = dirname(__file__)
APP_EXT = ".exe" if isWindows else ".app" if isMacos else ""


def crossApp(name: str):
    return f"{name}{APP_EXT}"


firefoxName = crossApp("firefox")
firefoxPath = (
    r"C:\Program Files\Mozilla Firefox\firefox.exe"
    if isWindows
    else r"/usr/local/bin/firefox" if isMacos else r"/usr/bin/firefox"
)
if exist(f"./{firefoxName}"):
    firefoxPath = f"./{firefoxName}"


def branch(cmd, cwd=PWD):
    return subprocess.call(cmd, cwd=cwd, env=environ)


if __name__ == "__main__":
    MAIN, *args = sys.argv
    if not exist(firefoxPath):
        if len(args) > 0:
            a = " ".join(args)
            if not exist(a):
                raise Exception("Firefox path not valid!")
            else:
                branch([a, "-P"])
    else:
        try:
            if isWindows:
                branch(f"{firefoxPath} -P")
            else:
                branch([firefoxPath,'-P'])
        except Exception:
            raise Exception(
                f"Firefox not installed default! If you installed Firefox other default path, please use:\n{crossApp('firefoxprofile')} PATH"
            )
