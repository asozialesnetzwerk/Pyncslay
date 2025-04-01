"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
from glob import glob
import syncplay

APP = ["syncplayClient.py"]
DATA_FILES = [
    (
        "resources",
        glob("syncplay/resources/*.png")
        + glob("syncplay/resources/*.rtf")
        + glob("syncplay/resources/*.txt")
        + glob("syncplay/resources/*.lua"),
    ),
    ("resources/lua/intf", glob("syncplay/resources/lua/intf/*.lua")),
]
OPTIONS = {
    "iconfile": "syncplay/resources/icon.icns",
    "extra_scripts": "syncplayServer.py",
    "includes": {
        "PySide2.QtCore",
        "PySide2.QtUiTools",
        "PySide2.QtGui",
        "PySide2.QtWidgets",
        "certifi",
        "cffi",
        "pem",
        "charset_normalizer.md__mypyc",
    },
    "excludes": {
        "PySide",
        "PySide.QtCore",
        "PySide.QtUiTools",
        "PySide.QtGui",
        "tkinter",
    },
    "qt_plugins": [
        "platforms/libqcocoa.dylib",
        "platforms/libqminimal.dylib",
        "platforms/libqoffscreen.dylib",
        "styles/libqmacstyle.dylib",
    ],
    "plist": {
        "CFBundleName": "Syncplay",
        "CFBundleShortVersionString": syncplay.version,
        "CFBundleIdentifier": "pl.syncplay.Syncplay",
        "LSMinimumSystemVersion": "10.12.0",
        "NSHumanReadableCopyright": "Copyright © 2019 Syncplay All Rights Reserved",
    },
}

setup(
    app=APP,
    name="Syncplay",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
