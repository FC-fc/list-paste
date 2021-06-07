# Version 1.1
# iterates over input file typing line + pressing enter

from pynput.keyboard import Key, Controller
from pywinauto.application import Application
from datetime import datetime

def read_file(file_name):
    # read data 
    with open(file_name, 'r+') as file:
        data = file.read().split()
    return data


def get_settings():
    # get file names
    with open('settings.fc', 'r+') as file:
        names = file.read().split(',')
    return names[0], names[1]


def log(output):
    with open('log.fc', 'a+') as file:
        file.write(str(datetime.now()) + ': ' + str(output) + '\n')


if __name__ == "__main__":
    log("session start")

    # get filenames
    file_name, app_name = get_settings()

    # get data
    data = read_file(file_name)
    log(f"{len(data)} items loaded")

    # setup reference
    try:
        app = Application().connect(title=app_name)
    except:
        log('Error: app not found')
        print(f"Error: {app_name} not found")
        input("Enter to close...")
        exit()

    # select window
    app_dialog = app.top_window()
    app_dialog.set_focus()
    keyboard = Controller()

    # print output
    for line in data:
        for char in line:
            keyboard.press(char)
        keyboard.press(Key.enter)
        #keyboard.press(Key.down)
    log('session end')
    
