# Installation
1. Download the current build __paste-help__ folder.
2. Create desktop shortcuts for __paste-help.exe__ and __data.txt__.


## How to create a desktop shortcut
1. Click the Windows key or open File Explorer and browse to the program for which you want to create a desktop shortcut.

2. Left-click the name of the program, and drag it onto your desktop.

3. Select create shortcut in the dropdown.


# How to use
The aim of the program is to simulate a user typing a list where it is not possible to copy-paste. It works by typing a line from data.txt then simulating an 'Enter' key press. 

1. Paste list in data.txt in the format:
```
item 1
item 2
etc.
```


2. Open output program and select first position to print to.
3. Run paste-help program.

# Default Settings
### settings.fc
*input file* , *application name*

    data.txt,Untitled - Notepad
### data.txt:
    1
    2
    3


# Verification
'Auto Py to Exe' is used to create a folder and build an executable and copy the required modules into the __Current build__ folder.

Version: 1.1

Current build Folder:
* SHA256 (data): CB1E8E7008A5C25C2E213CF54DC07CBBE464C5053F4B0E71619953B37DD621D5
* SHA256 (data + names): 10721AB69C71894F8488431434EE1B088F3B9455C54DBD407250732322EE050B

paste-help.exe:
* SHA256: CE0F3AC72D831BD9CBB602CBC3ADA60F8363E70A91AC4CD71F0E3AB774066049
* MD5: 3C5CB0E1194122AFF54C75BCEA089001

Hashes generated with default settings and empty log file.
