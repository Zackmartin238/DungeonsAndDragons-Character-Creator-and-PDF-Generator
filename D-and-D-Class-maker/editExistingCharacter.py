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
    setup_scrollable_canvas()
    view_page(page)
    viewCharacter(1)
    pagemenu = OptionMenu(topframe, page, *x, command=viewCharacter)
    pagemenu.pack(in_=topframe, side=LEFT)
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
        print("Hello, it looks like your using a non-Windows os. You'll need to print this one through your browser")
        import webbrowser
        webbrowser.open_new(currentFile)
        

def view_page(page):
    global label
    label = Label(topframe, text="Page")
    label.pack(in_=topframe, side=LEFT)

def setup_scrollable_canvas():
    global canvas, scrollbar
    canvas = Canvas(mainWindow)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = Scrollbar(mainWindow, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

def viewCharacter(page):
    global midframe, changes, canvas, entry_vars

    changes = pdf.get_form_fields(currentFile, sort=True, page_number=page)
    if int(page) == 1:
        message.destroy()  # Assuming message is a global variable
        midframe = Frame(canvas)
        canvas.create_window((0, 0), window=midframe, anchor="nw")
        row_counter = 2
        entry_vars = {}  # Store entry_vars for each field
        for field, value in changes.items():
            label = Label(midframe, text=field)
            label.grid(row=row_counter, column=0, padx="10", sticky="e")  # Align labels to the right
            entry_var = StringVar(value=value)  # Initialize with the initial value
            entry = Entry(midframe, textvariable=entry_var, width=30)
            entry.grid(row=row_counter, column=1, padx="10", sticky="w")  # Align entry fields to the left
            # Store the StringVar object directly within the Entry widget
            entry.entry_var = entry_var
            entry_vars[field] = entry  # Store entry widget for each field
            row_counter += 1

        # Update canvas scroll region after changes
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set)
    if int(page) == 2:
        message.destroy()  # Assuming message is a global variable
        midframe = Frame(canvas)
        canvas.create_window((0, 0), window=midframe, anchor="nw")
        row_counter = 2
        entry_vars = {}  # Store entry_vars for each field
        for field, value in changes.items():
            label = Label(midframe, text=field)
            label.grid(row=row_counter, column=0, padx="10", sticky="e")  # Align labels to the right
            entry_var = StringVar(value=value)  # Initialize with the initial value
            entry = Entry(midframe, textvariable=entry_var, width=30)
            entry.grid(row=row_counter, column=1, padx="10", sticky="w")  # Align entry fields to the left
            # Store the StringVar object directly within the Entry widget
            entry.entry_var = entry_var
            entry_vars[field] = entry  # Store entry widget for each field
            row_counter += 1

        # Update canvas scroll region after changes
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set)
    if int(page) == 3:
        message.destroy()  # Assuming message is a global variable
        midframe = Frame(canvas)
        canvas.create_window((0, 0), window=midframe, anchor="nw")
        row_counter = 2
        entry_vars = {}  # Store entry_vars for each field
        for field, value in changes.items():
            label = Label(midframe, text=field)
            label.grid(row=row_counter, column=0, padx="10", sticky="e")  # Align labels to the right
            entry_var = StringVar(value=value)  # Initialize with the initial value
            entry = Entry(midframe, textvariable=entry_var, width=30)
            entry.grid(row=row_counter, column=1, padx="10", sticky="w")  # Align entry fields to the left
            # Store the StringVar object directly within the Entry widget
            entry.entry_var = entry_var
            entry_vars[field] = entry  # Store entry widget for each field
            row_counter += 1

        # Update canvas scroll region after changes
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set)



# Other functions and the main function remain unchanged



def save_and_quit():
    saveChanges()
    reset()
def save_and_exit():
    saveChanges()
    quit_program()


def saveChanges():
    global changes, entry_vars, currentFile
    for field, value in changes.items():
        changes[field] = entry_vars[field].entry_var.get()
    # Update the changes dictionary with the current values in entry_var


    # Write the updated changes dictionary to the PDF file
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



    global FileSelectButton
    FileSelectButton = Button(topframe, text="Select File to edit", command=select_file)
    FileSelectButton.pack(in_=topframe, side=LEFT)
    Save_changes_button = Button(topframe, text="Save Changes", command=saveChanges)
    Save_changes_button.pack(in_=topframe, side=RIGHT)

    saveAndQuitButton = Button(topframe, text="Save And Edit Another", command=save_and_quit)
    saveAndQuitButton.pack(in_=topframe, side=RIGHT)
    mainloop()

def install_module(module_name):
    print(f"Trying to install required module: {module_name}")
    os.system(f'{sys.executable} -m pip install {module_name}')

if __name__ == "__main__":
    from tkinter import *
    import tkinter.filedialog
    import os
    from fillpdf import fillpdfs as pdf
    import sys
    import BetterImports
    BetterImports.Import('PyPDF2')
    import PyPDF2
    main()
