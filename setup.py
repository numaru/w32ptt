import itertools
import subprocess
import sys
from pathlib import Path

from cx_Freeze import Executable, setup

icon_path = str(Path("mic-hq.ico").resolve())


packages = ["keyboard", "pycaw", "comtypes", "psutil", "future"]
excludes = (
    subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
    .decode("utf-8")
    .split("\r\n")
)
excludes = map(lambda x: x.split("==")[0], excludes)
excludes = itertools.chain(excludes, ["tkinter"])
excludes = filter(lambda x: x not in packages, excludes)
excludes = filter(lambda x: x != "", excludes)
excludes = filter(lambda x: x != "pywin32", excludes)
excludes = list(excludes)


setup(
    name="w32ptt",
    version="0.1.0",
    author="Kin Numaru",
    description="A push-to-talk app for windows",
    long_description="A small app to get global push-to-talk on windows because it is not yet supported by ms-teams",
    executables=[Executable("w32ptt.pyw", base="Win32GUI", icon=icon_path)],
    options={
        "build_exe": {
            "packages": packages,
            "excludes": excludes,
            "include_files": ["mic-error.ico", "mic-muted.ico", "mic-speaking.ico"],
        },
        "bdist_msi": {
            "install_icon": icon_path,
            "data": {
                "Shortcut": [
                    (
                        "DesktopShortcut",  # Shortcut
                        "DesktopFolder",  # Directory_
                        "Push-to-talk",  # Name
                        "TARGETDIR",  # Component_
                        "[TARGETDIR]w32ptt.exe",  # Target
                        None,  # Arguments
                        None,  # Description
                        None,  # Hotkey
                        icon_path,  # Icon
                        None,  # IconIndex
                        None,  # ShowCmd
                        "TARGETDIR",  # WkDir
                    ),
                    (
                        "StartupShortcut",  # Shortcut
                        "StartupFolder",  # Directory_
                        "Push-to-talk",  # Name
                        "TARGETDIR",  # Component_
                        "[TARGETDIR]w32ptt.exe",  # Target
                        None,  # Arguments
                        None,  # Description
                        None,  # Hotkey
                        icon_path,  # Icon
                        None,  # IconIndex
                        None,  # ShowCmd
                        "TARGETDIR",  # WkDir
                    ),
                    (
                        "StartMenuShortcut",  # Shortcut
                        "StartMenuFolder",  # Directory_
                        "Push-to-talk",  # Name
                        "TARGETDIR",  # Component_
                        "[TARGETDIR]w32ptt.exe",  # Target
                        None,  # Arguments
                        None,  # Description
                        None,  # Hotkey
                        icon_path,  # Icon
                        None,  # IconIndex
                        None,  # ShowCmd
                        "TARGETDIR",  # WkDir
                    ),
                    (
                        "ProgramMenuShortcut",  # Shortcut
                        "ProgramMenuFolder",  # Directory_
                        "Push-to-talk",  # Name
                        "TARGETDIR",  # Component_
                        "[TARGETDIR]w32ptt.exe",  # Target
                        None,  # Arguments
                        None,  # Description
                        None,  # Hotkey
                        icon_path,  # Icon
                        None,  # IconIndex
                        None,  # ShowCmd
                        "TARGETDIR",  # WkDir
                    ),
                ],
            },
        },
    },
)
