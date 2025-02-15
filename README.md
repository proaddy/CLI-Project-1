## Introduction
Simple Notes CLI tool which stores notes along with current datetime.

```cmd
python main.py --help
```
```
Usage: main.py [OPTIONS] COMMAND [ARGS]...

    ********************************************************
    
    -   Notes CLI Tool: Add, retrieve, and manage notes.   -

    ********************************************************

Options:
  --help  Show this message and exit.

Commands:
  addnote    Enter the message that needs to be saved
  delete     Deletes notes
  latest     Returns the latest note made
  listnotes  Display list of all notes, can be filtered using options
```

## Commands
- addnote
- delete
- latest
- listnodes

Use the program to explore more. 

#### SN(Side Note): The data is stored in 'storage.csv' file, if it doesn't exist then it will create it.

## Using the GUI
To open the interactive/GUI of the application made using PySide6 you have to write 
```cmd
python main.py gui | GUI | interactive 
```
and it will open a GUI application with three buttons, 1 input field and 1 display field.
