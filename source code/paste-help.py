# Version 1.1
# iterates over input file typing line + pressing enter

from pynput.keyboard import Key, Controller
from pywinauto.application import Application
from datetime import datetime
import sys
import time

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
    if len(sys.argv) > 1:
        try:
            wait = float(sys.argv[-1])
        except:
            print(f"Error: Invalid wait time {sys.argv[-1]}")
            log(f"Error: Invalid wait time {sys.argv[-1]}")
            exit()
    else:
        wait = 0

    log("session start")

    # get filenames
    file_name, app_name = get_settings()

    # get data
    data = read_file(file_name)
    log(f"{len(data)} items loaded")

    # setup reference
    try:
        app = Application().connect(title='Book1 - Excel')
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
        keyboard.type(line)
        if wait: time.sleep(wait)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        if wait: time.sleep(wait)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        if wait: time.sleep(wait)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        if wait: time.sleep(wait)

    log('session end')
    
