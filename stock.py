# to do:
    # create setup file 
        # create hidden folder 
        # move files 
        # create shortcut and csv file

    # impliment filename and application txt files

    # finish draft for main file

    # create github and SHA verification


from pynput.keyboard import Key, Controller
from pywinauto.application import Application
import os


def read_file(file_name):
    with open(file_name, 'r+') as file:
        data = file.read().split()
    return data


def get_settings():
    # open file
    with open('settings.fc', 'r+') as file:
        names = file.read().split(',')
    return names[0], names[1]


def run(data, app_name):
    # setup reference
    app = Application().connect(title=app_name)
    # select window
    app_dialog = app.top_window()
    app_dialog.maximize()
    app_dialog.set_focus()
    keyboard = Controller()
    # print output
    for line in data:
        for char in line:
            keyboard.press(char)
        keyboard.press(Key.enter)
        #keyboard.press(Key.down)


if __name__ == "__main__":
    input("Enter to begin...")
    file_name, app_name = get_settings()
    data = read_file(file_name)
    run(data, app_name)

    
