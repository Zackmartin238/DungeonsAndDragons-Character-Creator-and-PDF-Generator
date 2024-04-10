
def quit_program():
    mainWindow.destroy()
    quit
def select_file():
    path = os.path.dirname(os.path.realpath(__file__)),
    currentFile = tkinter.filedialog.askopenfilename(
        parent=mainWindow,
        initialdir= str(path),
        title='Choose file',
        filetypes=[('PDF files', '*.pdf')],
    )

if __name__ == "__main__":
    from tkinter import *
    import tkinter.filedialog
    import os

    
    mainWindow = Tk()
    mainWindow.title("Edit Existing Character")

    topframe= Frame(mainWindow)
    topframe.pack(fill="x")

    exitButton = Button(topframe, text="Go Back to Main", command=quit_program)
    exitButton.pack(in_=topframe, side=LEFT)

    messageFrame = Frame(mainWindow)
    messageFrame.pack()

    message = Message(messageFrame, text= "Choose a file to edit", width="200")
    message.pack(pady="20") 

    buttonFrame = Frame(mainWindow)
    buttonFrame.pack()

    FileSelectButton = Button(topframe, text="Select File to edit", command=select_file)
    FileSelectButton.pack(in_=topframe, side=LEFT)

    mainloop()