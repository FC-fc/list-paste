from genericpath import getctime
import os
import winshell
dir_path = os.path.dirname(os.path.realpath(__file__))
winshell.CreateShortcut (
Path=os.path.join(winshell.desktop (), "GuruHelp.lnk"),
Target=dir_path + "\stock.py"
)