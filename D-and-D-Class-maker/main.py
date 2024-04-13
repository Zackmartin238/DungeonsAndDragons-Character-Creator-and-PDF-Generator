import os
import sys
import subprocess
# Define a function to install missing modules
def install_module(module_name):
    print(f"Trying to install required module: {module_name}")
    os.system(f'{sys.executable} -m pip install {module_name}')

# Try to import modules, and if they are not found, install them
try:
    import random
except ImportError or ModuleNotFoundError:
    install_module("random")
    import random

try:
    import datetime
except ImportError or ModuleNotFoundError:
    install_module("datetime")
    import datetime

try:
    from tkinter import *
except ImportError or ModuleNotFoundError:
    install_module("python3-tk")
    from tkinter import *

try:
    from fillpdf import fillpdfs
except ImportError or ModuleNotFoundError:
    install_module("fillpdf")
    from fillpdf import fillpdfs

try:
    import shutil
except ImportError or ModuleNotFoundError:
    install_module("shutil")
    import shutil

try:
    import _tkinter
except ImportError or ModuleNotFoundError:
    install_module("_tkinter")
    import _tkinter

try:
    import tkinter.font as font
except ImportError or ModuleNotFoundError:
    install_module("tkinter.font")
    import tkinter.font as font





def start_to_make_new_character():
    try:
        path = os.getcwd()
        createNewCharacterFileLocation = os.path.join(path, "createNewCharacter.py")
        main_window.withdraw()

        # Determine which Python command to use
        python_command = "python3" if subprocess.run(["which", "python3"], capture_output=True, text=True).stdout.strip() else "python"

        check = subprocess.run([python_command, createNewCharacterFileLocation], capture_output=True, text=True)
        check
    except FileNotFoundError:
        print("Script not found")
        # Handle the case where the script is not found
    finally:
        main_window.deiconify()



        

def existing_character():
    try: 
        os.system()
    except:
        None

def exit_program():
    main_window.withdraw()
    warningWindow = Tk()
    warningWindow.title("Are you sure?")
    warningFrame = Frame(warningWindow)
    warningFrame.pack(padx="20", pady="20")
    warningMessage = Label(warningFrame, text="Are you REALLY sure you want to quit?")
    warningMessage.pack()
    def continue_program():
        warningWindow.destroy()
        main_window.deiconify()
    def quit_program():
        main_window.destroy()
        warningWindow.destroy()
        quit
    yesButton = Button(warningFrame, text="Yes", command = quit_program, fg="white", bg="red", font=helvFont)
    noButton = Button(warningFrame, text="No", command = continue_program, bg="black", fg="white", font=helvFont)
    yesButton.pack(side="left", padx="5", pady="20")
    noButton.pack(side="right", padx="5", pady="20")

def edit_existing():
    try:
        path = os.getcwd()

        createNewCharacterFileLocation = os.path.join(path, "editExistingCharacter.py")
        main_window.withdraw()

        # Determine which Python command to use
        python_command = "python3" if subprocess.run(["which", "python3"], capture_output=True, text=True).stdout.strip() else "python"

        check = subprocess.run([python_command, createNewCharacterFileLocation], capture_output=True, text=True)
        check
    except FileNotFoundError:
        print("Script not found")
        # Handle the case where the script is not found
    finally:
        main_window.deiconify()


if __name__ =="__main__":
    main_window = Tk()
    main_window.title("Main page: D&D Class Creator")
    main_window.configure(bg="white")

    first_frame = Frame(main_window)

    first_frame.pack()
    helvFont = font.Font(family='Helvetica', size=23, weight='bold')
    defaultFont = font.Font(family="sans serif", size=18)

    message = Message(first_frame, text="Welcome! What would you like to work on?", width="250", font=defaultFont, bg="white")
    message.pack()

    buttonFrame = Frame(main_window)
    buttonFrame.pack(side="bottom", padx="20", pady="20")

    newCharacterButton = Button(buttonFrame, text="New Character", bg="black", fg="white", command=start_to_make_new_character)
    newCharacterButton.pack(side="left", padx="10", pady="20")

    quitButton = Button(buttonFrame, text="Exit Program", bg="white", fg="red", command=exit_program)
    quitButton.pack(side="right", padx="10", pady="20")

    oldCharacterButton = Button(buttonFrame, text="Existing Character", bg="black", fg="white", command = edit_existing)
    oldCharacterButton.pack( padx="10", pady="20")



    mainloop()