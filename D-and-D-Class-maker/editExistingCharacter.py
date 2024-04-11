def quit_program():
    mainWindow.destroy()
    quit

def reset():
    mainWindow.destroy()
    main()

def select_file():
    global FileSelectButton
    FileSelectButton.destroy()

    FileSelectButton = Button(topframe, text="Edit New File", command=reset)
    FileSelectButton.pack(in_=topframe, side=LEFT)
    path = os.path.dirname(os.path.realpath(__file__))
    global currentFile
    global fileSelected
    currentFile = tkinter.filedialog.askopenfilename(
        parent=mainWindow,
        initialdir=str(path),
        title='Choose file',
        filetypes=[('PDF files', '*.pdf')],
    )
    file = open(currentFile, "rb")
    pdfReader = PyPDF2.PdfReader(file)

    # Count the number of pages
    total_pages = len(pdfReader.pages)
    x = []
    for i in range(total_pages):
        x.append(i + 1)  # Adding 1 to start page numbering from 1 instead of 0
    global page
    global able_to_print_char
    able_to_print_char = True
    page = StringVar(topframe)
    page.set('1')
    view_page(page)
    viewCharacter(1)
    page = OptionMenu(topframe, page, *x, command=viewCharacter)
    page.pack(in_=topframe, side=LEFT)
    if able_to_print_char == True:
        printButton = Button(topframe, text="Print file to Printer", command=print_using_printer)
        printButton.pack(in_=topframe, side=LEFT)
    else:
        None
    able_to_print_char = False

def print_using_printer():
    if os.name == "nt":
        os.startfile(currentFile)
    if os.name != "nt":
        lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
        lpr.stdin.write(currentFile)

def view_page(page):
    global label
    label = Label(topframe, text="Page")
    label.pack(in_=topframe, side=LEFT)

def viewCharacter(page):
    global able_to_print_char
    global label
    global changes
    changes = pdf.get_form_fields(currentFile, sort=True, page_number=int(page))
    if int(page) == 1:
        message.destroy()
        midframe = Frame(canvas)
        canvas.create_window((0, 0), window=midframe, anchor="nw")
        global player_name_var
        global char_name_var
        # Adding Player Name and Character Name fields
        label_player_name = Label(midframe, text="Player Name")
        label_player_name.grid(row=0, column=0, padx="8")
        player_name_var = StringVar(value=changes.get('PlayerName', ''))
        entry_player_name = Entry(midframe, textvariable=player_name_var, width=30)
        entry_player_name.grid(row=0, column=1, padx="8")

        label_char_name = Label(midframe, text="Character Name")
        label_char_name.grid(row=1, column=0, padx="8")
        char_name_var = StringVar(value=changes.get('CharacterName', ''))
        entry_char_name = Entry(midframe, textvariable=char_name_var, width=30)
        entry_char_name.grid(row=1, column=1, padx="8")

        # Populating other fields based on the provided dictionary
        row_counter = 2
        for field, value in changes.items():
            if field not in ['PlayerName', 'CharacterName']:
                label = Label(midframe, text=field)
                label.grid(row=row_counter, column=0, padx="8")

                entry_var = StringVar(value=value)
                entry = Entry(midframe, textvariable=entry_var, width=30)
                entry.grid(row=row_counter, column=1, padx="8")

                row_counter += 1

        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set)



def save_and_quit():
    saveChanges()
    reset()


def saveChanges():
    global changes
    changes["PlayerName"] = player_name_var.get()
    changes["CharacterName"] = char_name_var.get()
    writeChangesToFile()


def writeChangesToFile():
    pdf.write_fillable_pdf(currentFile, currentFile, changes)
    return


def main():
    global currentFile
    global topframe
    global page
    global mainWindow
    global changes
    mainWindow = Tk()
    mainWindow.title("Edit Existing Character")

    topframe = Frame(mainWindow)
    topframe.pack(fill="x")

    exitButton = Button(topframe, text="Go Back to Main", command=quit_program)
    exitButton.pack(in_=topframe, side=LEFT)

    messageFrame = Frame(mainWindow)
    messageFrame.pack()

    global message
    message = Message(messageFrame, text="Choose a file to edit", width="200")
    message.pack(pady="20")

    global canvas
    canvas = Canvas(mainWindow)
    canvas.pack(side="left", fill="both", expand=True)

    global scrollbar
    scrollbar = Scrollbar(mainWindow, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    global midframe
    midframe = Frame(canvas)
    canvas.create_window((0, 0), window=midframe, anchor="nw")

    global FileSelectButton
    FileSelectButton = Button(topframe, text="Select File to edit", command=select_file)
    FileSelectButton.pack(in_=topframe, side=LEFT)
    mainloop()




if __name__ == "__main__":
    from tkinter import *
    import tkinter.filedialog
    import os
    import subprocess
    from fillpdf import fillpdfs as pdf
    try:
        import PyPDF2
    except:
        print("installing PyPDF2")
        os.system("pip install PyPDF2")
        import PyPDF2
    import sys
    import threading

    main()
