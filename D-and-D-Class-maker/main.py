import os
try:
    import random
except ImportError or ModuleNotFoundError:
    os.system('python3 -m pip install random')
    # Import the required module again for global access
    import random
try:
    import datetime
except ImportError or ModuleNotFoundError:
    print("Trying to install required module: datetime")
    os.system('python3 -m pip install datetime')
    # Import the required module again for global access
    import datetime
try:
    from tkinter import *
except ImportError or ModuleNotFoundError:
    print("Trying to install required module: tkinter")
    os.system('sudo apt install python3-tk')
    # Import the required module again for global access
    from tkinter import *
try:
    from fillpdf import fillpdfs
except ImportError or ModuleNotFoundError:
    print("Trying to install required module: fillpdfs")
    os.system('python3 -m pip install fillpdf')
    # Import the required module again for global access
    from fillpdf import fillpdfs
try:
    import shutil
except ImportError or ModuleNotFoundError:
    print("Trying to install required module: shutil")
    os.system('python3 -m pip install shutil')
    # Import the required module again for global access
    import shutil
try:
    import _tkinter
except ImportError or ModuleNotFoundError:
    print("Trying to install required module: tkinter")
    os.system('python3 -m pip install _tkinter')
    # Import the required module again for global access
    import _tkinter

try: 
    import tkinter.font as font
except ImportError or ModuleNotFoundError:
    print("Trying to install tkinter fonts...")
    os.system("python3 -m pip install tkinter.font")
    import tkinter.font as font

def start_to_make_new_character():
    path = os.path.dirname(os.path.realpath(__file__))

    if 'D and D Class maker' in path:
        print(path)
        print("it works now...")
    else:
        import sys
        print(sys.path())
        path = sys.path
        if 'Dungeons' in path:
            print("ig it worked on the second try?")
        else:
            quit
        
    createNewCharacterFileLocation = str(path)+"\createNewCharacter.py"
    try: 
        main_window.withdraw()
        os.system(f'python "{createNewCharacterFileLocation}"')
        main_window.deiconify()
    except:
        os.system(f'python3 "{createNewCharacterFileLocation}"')

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
    path = os.path.dirname(os.path.realpath(__file__))

    if 'D and D Class maker' in path:
        None
    else:
        import sys
        print(sys.path())
        path = sys.path
        if 'Dungeons' in path:
            print("ig it worked on the second try?")
        else:
            quit
    createNewCharacterFileLocation = str(path)+"/editExistingCharacter.py"
    try: 
        main_window.withdraw()
        os.system(f'python "{createNewCharacterFileLocation}"')
        main_window.deiconify()
    except:
        os.system(f'python3 "{createNewCharacterFileLocation}"')


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
