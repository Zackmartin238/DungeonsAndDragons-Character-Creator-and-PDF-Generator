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
name = 'none'
with open('logs.txt', 'a') as file:
    file.write("["+str(datetime.datetime.now())+"] "+"Welcome to the Ultimate D&D Character creator. We've been initialized, and everything has been imported without error. \n")

path = os.path.dirname(os.path.realpath(__file__))

if 'D and D Class maker' in path:
    print(path)
    print("it works now...")
else:
    print("Didn't work :(")
    exit
    
pathToCharacter=str(str(path)+"/character.pdf")

pathToCurrent=str(str(path)+"/characters/TemporaryCharacter.pdf")

logfile = str(str(path)+"/logs.txt")


isTemp = os.path.isfile(pathToCurrent)

if isTemp == False:
    newfile = shutil.copyfile(pathToCharacter, pathToCurrent)
    with open('logs.txt', "a") as file:
        file.write(f"Temporary File created. Can be found at {pathToCharacter} \n")
if isTemp == True:
    with open(logfile, "a") as file:
        file.write("Temp file Already Exists \n")
#create the original screen:
root = Tk()
root.title("Welcome to your D&D class Creator!")
try: 
    root.state("zoomed")
except _tkinter.TclError:
    None

with open('logs.txt', "a") as file:
    file.write("Tkinter initialized \n")
# gotta call the variables
health_die = 0
health = 0
frameDICE = Frame(root)
refreshedFRAME = Frame(root)
CONframe = Frame(root)
WISframe = Frame(root)
INTframe = Frame(root)
CHAframe = Frame(root)

number_of_choices = 6

dice_1 = 0
dice_2 = 0
dice_3 = 0
dice_4 = 0
dice_5 = 0
dice_6 = 0

health = 0
extra_hp_per_level = 0
currentvariant = "none"
race_CHA_bonus = 0
race_CON_bonus = 0
race_INT_bonus = 0
race_DEX_bonus = 0 
race_STR_bonus = 0
race_WIS_bonus = 0
health_die = 0

STR_choice = 0
DEX_choice = 0
CON_choice = 0
INT_choice = 0
WIS_choice = 0
CHA_choice = 0

levelisgood = False
classisgood = False
raceisgood = False


level_attempts = 0
class_attempts = 0
race_attempts = 0

STR_choice = False
DEX_choice = False
CON_choice = False
INT_choice = False
WIS_choice = False
CHA_choice = False

STR_score = int
WIS_score = int
CHA_score = int
INT_score = int
DEX_score = int
CON_score = int

error_codes_fun = ["nope", "nice try", "really?", "cmon now", "is there something else you should be doing?", "try again", "got it wrong", "go back and try again"]

# this pre-rolls the dice, sorts them, and deletes the lowest one. 

dice_set1 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6),]
dice_set1.sort()
dice_set1.pop(0)
    
    

dice_set2 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6),]
dice_set2.sort()
dice_set2.pop(0)
    

dice_set3 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6),]
dice_set3.sort()
dice_set3.pop(0)
    

dice_set4 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6),]
dice_set4.sort()
dice_set4.pop(0)
    

dice_set5 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6),]
dice_set5.sort()
dice_set5.pop(0)
    

dice_set6 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6),]
dice_set6.sort()
dice_set6.pop(0)
    

    
dice_sets = [
        sum(dice_set1), sum(dice_set2), sum(dice_set3), sum(dice_set4), sum(dice_set5), sum(dice_set6)
    ]

dice_sets.sort(reverse=True)


cLass = "n/a"
race = "n/a"
level = IntVar()
chosenlevel = int

choices= [1, 2, 3, 4, 5, 6]

#this registers the modifier for the dice, changing allowing for less complicated score decisions 

dice1modval = round((dice_sets[0]-10)/2)
dice2modval = round((dice_sets[1]-10)/2)
dice3modval = round((dice_sets[2]-10)/2)
dice4modval = round((dice_sets[3]-10)/2)
dice5modval = round((dice_sets[4]-10)/2)
dice6modval = round((dice_sets[5]-10)/2)

if round((dice_sets[0]-10)/2) >= 0:
    dice1mod= "+"
else:
    dice1mod = "-"
    dice1modval = round((dice_sets[0]-10)/2)*-1
if round((dice_sets[1]-10)/2) >= 0:
    dice2mod= "+"
else:
    dice2mod = "-"
    dice2modval = round((dice_sets[1]-10)/2)*-1
if round((dice_sets[2]-10)/2) >= 0:
    dice3mod= "+"
else:
    dice3mod = "-"
    dice3modval = round((dice_sets[2]-10)/2)*-1
if round((dice_sets[3]-10)/2) >= 0:
    dice4mod= "+"
else:
    dice4mod = "-"
    dice4modval = round((dice_sets[3]-10)/2)*-1
if round((dice_sets[4]-10)/2) >= 0:
    dice5mod= "+"
else:
    dice5mod = "-"
    dice5modval = round((dice_sets[4]-10)/2)*-1
if round((dice_sets[5]-10)/2) >= 0:
    dice6mod= "+"
else:
    dice6mod = "-"
    dice6modval = round(((dice_sets[5]-10)/2)*-1)
dice_1 = [(dice_sets[0]), "(", dice1mod, dice1modval, ")"]
dice_2 = [(dice_sets[1]), "(", dice2mod, dice2modval, ")"]
dice_3 = [(dice_sets[2]), "(", dice3mod, dice3modval, ")"]
dice_4 = [(dice_sets[3]), "(", dice4mod, dice4modval, ")"]
dice_5 = [(dice_sets[4]), "(", dice5mod, dice5modval, ")"]
dice_6 = [(dice_sets[5]), "(", dice6mod, dice6modval, ")"]
# dice functions, to be called later


 
var4 = IntVar()

decision = None



classes = ["fighter", "wizard", "barbarian", "warlock", "sorcerer", "monk", "bard", "cleric", "paladin", "ranger", "rogue"]
levels = ["1", 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
races = ["dwarf", "elf", "gnome", "halfling", "human", "dragonborn", "half-elf", "half-orc", "tiefling"]

# functions that submit decisions... beautiful
def submit_DEX_decision(decisio):
        global decision
        global DEX_score
        decision = decisio
        refreshedFRAME.destroy()
        DEX_score = dice_sets[decision-1] + race_DEX_bonus 
        
        dice_sets.pop(decision-1)
        chooseCON()
        return DEX_score, CON_score, WIS_score, INT_score, CHA_score
def submit_CON_decision(decisio):
        global decision
        global CON_score
        decision = decisio
        CON_score = dice_sets[decision-1] + race_CON_bonus 
        
        dice_sets.pop(decision-1)
        chooseINT()
        return CON_score, WIS_score, INT_score, CHA_score
def submit_WIS_decision(decisio):
        global decision
        global WIS_score
        decision = decisio
        WIS_score = dice_sets[decision-1] + race_WIS_bonus 
        
        dice_sets.pop(decision-1)
        chooseCHA()
        return WIS_score, INT_score, CHA_score
def submit_INT_decision(INT_decision):
        global INT_score
        INT_score = dice_sets[INT_decision-1] + race_INT_bonus 
        
        dice_sets.pop(INT_decision-1)
        chooseWIS()
        return INT_score, CHA_score
def submit_CHA_decision(CHA_decision):
        global CHA_score
        CHA_score = dice_sets[CHA_decision-1] + race_CHA_bonus 
        
        dice_sets.pop(CHA_decision-1)
        refreshedFRAME.destroy()
        printscores()
        return CHA_score

def chooseDEX(currentframe):
        currentframe.destroy()
        refreshedFRAME.pack()
        global var5
        global decision
        dice1modval = round((dice_sets[0]-10)/2)
        dice2modval = round((dice_sets[1]-10)/2)
        dice3modval = round((dice_sets[2]-10)/2)
        dice4modval = round((dice_sets[3]-10)/2)
        dice5modval = round((dice_sets[4]-10)/2)
        if round((dice_sets[0]-10)/2) >= 0:
            dice1mod= "+"
        else:
            dice1mod = "-"
            dice1modval = round((dice_sets[0]-10)/2)*-1
        if round((dice_sets[1]-10)/2) >= 0:
            dice2mod= "+"
        else:
            dice2mod = "-"
            dice2modval = round((dice_sets[1]-10)/2)*-1
        if round((dice_sets[2]-10)/2) >= 0:
            dice3mod= "+"
        else:
            dice3mod = "-"
            dice3modval = round((dice_sets[2]-10)/2)*-1
        if round((dice_sets[3]-10)/2) >= 0:
            dice4mod= "+"
        else:
            dice4mod = "-"
            dice4modval = round((dice_sets[3]-10)/2)*-1
        if round((dice_sets[4]-10)/2) >= 0:
            dice5mod= "+"
        else:
            dice5mod = "-"
            dice5modval = round((dice_sets[4]-10)/2)*-1
        dice_1 = [(dice_sets[0]), "(", dice1mod, dice1modval, ")"]
        dice_2 = [(dice_sets[1]), "(", dice2mod, dice2modval, ")"]
        dice_3 = [(dice_sets[2]), "(", dice3mod, dice3modval, ")"]
        dice_4 = [(dice_sets[3]), "(", dice4mod, dice4modval, ")"]
        dice_5 = [(dice_sets[4]), "(", dice5mod, dice5modval, ")"]  
        
        var5 = IntVar()
        msg = Message( refreshedFRAME, text = "Let's Pick Your Stats")
        msg.pack()
        main_msg1= Message(refreshedFRAME, text="Choose Your DEX modifier")
        main_msg1.pack()
        Radiobutton(refreshedFRAME, text= dice_1, variable=var5,command= setdecision1(1), value=1).pack(side="left")
        Radiobutton(refreshedFRAME, text= dice_2, variable=var5,command= setdecision2(2), value=2).pack(side="left")
        Radiobutton(refreshedFRAME, text= dice_3, variable=var5,command= setdecision3(3), value=3).pack(side="left")
        Radiobutton(refreshedFRAME, text= dice_4, variable=var5,command= setdecision4(4), value=4).pack(side="left")
        Radiobutton(refreshedFRAME, text= dice_5, variable=var5,command= setdecision5(5), value=5).pack(side="left")
        
        Button(refreshedFRAME, text="Submit", command= lambda: submit_DEX_decision(var5.get()), bg="black", fg='white', activebackground='black', activeforeground='grey').pack()
        return var5, decision
def chooseCON():
        global refreshedFRAME
        refreshedFRAME.destroy()
        refreshedFRAME = Frame(root)
        refreshedFRAME.pack()
        global var5
        global decision
        dice1modval = round((dice_sets[0]-10)/2)
        dice2modval = round((dice_sets[1]-10)/2)
        dice3modval = round((dice_sets[2]-10)/2)
        dice4modval = round((dice_sets[3]-10)/2)
        if round((dice_sets[0]-10)/2) >= 0:
            dice1mod= "+"
        else:
            dice1mod = "-"
            dice1modval = round((dice_sets[0]-10)/2)*-1
        if round((dice_sets[1]-10)/2) >= 0:
            dice2mod= "+"
        else:
            dice2mod = "-"
            dice2modval = round((dice_sets[1]-10)/2)*-1
        if round((dice_sets[2]-10)/2) >= 0:
            dice3mod= "+"
        else:
            dice3mod = "-"
            dice3modval = round((dice_sets[2]-10)/2)*-1
        if round((dice_sets[3]-10)/2) >= 0:
            dice4mod= "+"
        else:
            dice4mod = "-"
            dice4modval = round((dice_sets[3]-10)/2)*-1
        dice_1 = [(dice_sets[0]), "(", dice1mod, dice1modval, ")"]
        dice_2 = [(dice_sets[1]), "(", dice2mod, dice2modval, ")"]
        dice_3 = [(dice_sets[2]), "(", dice3mod, dice3modval, ")"]
        dice_4 = [(dice_sets[3]), "(", dice4mod, dice4modval, ")"]
        
        var5 = IntVar()
        msg = Message( refreshedFRAME, text = "Let's Pick Your Stats")
        msg.pack()
        main_msg1= Message(refreshedFRAME, text="Choose Your CON modifier")
        main_msg1.pack()
        Radiobutton(refreshedFRAME, text= dice_1, variable=var5,command= setdecision1(1), value=1).pack(side="left")
        Radiobutton(refreshedFRAME, text= dice_2, variable=var5,command= setdecision2(2), value=2).pack(side="left")
        Radiobutton(refreshedFRAME, text= dice_3, variable=var5,command= setdecision3(3), value=3).pack(side="left")
        Radiobutton(refreshedFRAME, text= dice_4, variable=var5,command= setdecision4(4), value=4).pack(side="left")
        Button(refreshedFRAME, text="Submit", command= lambda: submit_CON_decision(var5.get()), bg="black", fg='white', activebackground='black', activeforeground='grey').pack()
        return var5, decision
def chooseINT():
        global refreshedFRAME
        refreshedFRAME.destroy()
        refreshedFRAME = Frame(root)
        dice1modval = round((dice_sets[0]-10)/2)
        dice2modval = round((dice_sets[1]-10)/2)
        dice3modval = round((dice_sets[2]-10)/2)
        if round((dice_sets[0]-10)/2) >= 0:
            dice1mod= "+"
        else:
            dice1mod = "-"
            dice1modval = round((dice_sets[0]-10)/2)*-1
        if round((dice_sets[1]-10)/2) >= 0:
            dice2mod= "+"
        else:
            dice2mod = "-"
            dice2modval = round((dice_sets[1]-10)/2)*-1
        if round((dice_sets[2]-10)/2) >= 0:
            dice3mod= "+"
        else:
            dice3mod = "-"
            dice3modval = round((dice_sets[2]-10)/2)*-1
        dice_1 = [(dice_sets[0]), "(", dice1mod, dice1modval, ")"]
        dice_2 = [(dice_sets[1]), "(", dice2mod, dice2modval, ")"]
        dice_3 = [(dice_sets[2]), "(", dice3mod, dice3modval, ")"]
        refreshedFRAME.pack()
        global var5
        var5 = IntVar()
        msg = Message( refreshedFRAME, text = "Let's Pick Your Stats!")
        msg.pack()
        main_msg1= Message(refreshedFRAME, text="Choose Your INT modifier")
        main_msg1.pack()
        Radiobutton(refreshedFRAME, text= dice_1, variable=var5,command= setdecision1(1), value=1).pack(side="left")
        Radiobutton(refreshedFRAME, text= dice_2, variable=var5,command= setdecision2(2), value=2).pack(side="left")
        Radiobutton(refreshedFRAME, text= dice_3, variable=var5,command= setdecision3(3), value=3).pack(side="left")
        Button(refreshedFRAME, text="Submit", command= lambda: submit_INT_decision(var5.get()), bg="black", fg='white', activebackground='black', activeforeground='grey').pack()
        return number_of_choices, var4
def chooseWIS():
        global number_of_choices
        global refreshedFRAME
        refreshedFRAME.destroy()
        refreshedFRAME = Frame(root)
        dice1modval = round((dice_sets[0]-10)/2)
        dice2modval = round((dice_sets[1]-10)/2)
        if round((dice_sets[0]-10)/2) >= 0:
            dice1mod= "+"
        else:
            dice1mod = "-"
            dice1modval = round((dice_sets[0]-10)/2)*-1
        if round((dice_sets[1]-10)/2) >= 0:
            dice2mod= "+"
        else:
            dice2mod = "-"
            dice2modval = round((dice_sets[1]-10)/2)*-1
        dice_1 = [(dice_sets[0]), "(", dice1mod, dice1modval, ")"]
        dice_2 = [(dice_sets[1]), "(", dice2mod, dice2modval, ")"]        
        refreshedFRAME.pack()
        number_of_choices -= 1
        global var5
        WIS_decision = IntVar()
        var5 = IntVar()
        msg = Message( refreshedFRAME, text = "Let's Pick Your Stats!")
        msg.pack()
        main_msg1= Message(refreshedFRAME, text="Choose Your WIS modifier")
        main_msg1.pack()
        Radiobutton(refreshedFRAME, text= dice_1, variable=var5,command= setdecision1(1), value=1).pack(side="left")    
        Radiobutton(refreshedFRAME, text= dice_2, variable=var5,command= setdecision2(2), value=2).pack(side="left")
        Button(refreshedFRAME, text="Submit", command= lambda: submit_WIS_decision(var5.get()), bg="black", fg='white', activebackground='black', activeforeground='grey').pack()
        return number_of_choices, var4
def chooseCHA():
        global number_of_choices
        global refreshedFRAME
        refreshedFRAME.destroy()
        refreshedFRAME = Frame(root)
        dice1modval = round((dice_sets[0]-10)/2)
        if round((dice_sets[0]-10)/2) >= 0:
            dice1mod= "+"
        else:
            dice1mod = "-"
            dice1modval = round((dice_sets[0]-10)/2)*-1
        dice_1 = [(dice_sets[0]), "(", dice1mod, dice1modval, ")"]
        refreshedFRAME.pack()
        number_of_choices -= 1
        global var5
        var5 = IntVar()
        msg = Message( refreshedFRAME, text = "Let's Pick Your Stats")
        msg.pack()
        main_msg1= Message(refreshedFRAME, text="Choose Your CHA modifier")
        main_msg1.pack()
        Radiobutton(refreshedFRAME, text= dice_1, variable=var5,command= setdecision1(1), value=1).pack(side="left")
        
        Button(refreshedFRAME, text="Submit", command= lambda: submit_CHA_decision(var5.get()), bg="black", fg='white', activebackground='black', activeforeground='grey').pack()
        return number_of_choices, var4

def setdecision1(decisio):
        global decision
        decisio = 1
        decision = decisio
        return decision
def setdecision2(decisio):
        global decision
        decisio = 2
        decision = decisio
        return decision
def setdecision3(decisio):
        global decision
        decisio = 3
        decision = decisio
        return decision
def setdecision4(decisio):
        global decision
        decisio = 4
        decision = decisio
        return decision
def setdecision5(decisio):
        global decision
        decisio = 5
        decision = decisio
        return decision
def setdecision6(decisio):
    global decision
    decisio = 6
    decision = decisio
    return decision
     

#assign cLass depending on button pressed
ws = root
def selection():
    choice = var.get()
    global cLass
    if choice == 1:
        cLass = "barbarian"
    elif choice == 2:
        cLass = "bard"
    elif choice == 3:
        cLass = "cleric"
    elif choice == 4:
        cLass = "fighter"
    elif choice == 5:
        cLass = "monk"
    elif choice == 6:
        cLass = "paladin"
    elif choice == 7:
        cLass = "ranger"
    elif choice == 8:
        cLass = "rogue"
    elif choice == 9:
        cLass = "sorcerer"
    elif choice == 10:
        cLass = "warlock"
    elif choice == 11:
        cLass = "wizard"
    try: 
        return cLass
    finally:
        None
# same thing for race

def selectionrace():
    global race
    choice2 = var2.get()
    if choice2 == 1:
        race = "dragonborn"
    elif choice2 == 2:
        race = "dwarf"
    elif choice2 == 3:
        race = "elf"
    elif choice2 == 4:
        race = "half-elf"
    elif choice2 == 5:
        race = "halfling"
    elif choice2 == 6:
        race = "half-orc"
    elif choice2 == 7:
        race = "human"
    elif choice2 == 8:
        race = "gnome"
    elif choice2 == 9:
        race = "tiefling"
    try: 
        return race
    finally:
        None

def submit():
    choice = var.get()
    global cLass
    global race
    if choice == 1:
        cLass = "barbarian"
    elif choice == 2:
        cLass = "bard"
    elif choice == 3:
        cLass = "cleric"
    elif choice == 4:
        cLass = "fighter"
    elif choice == 5:
        cLass = "monk"
    elif choice == 6:
        cLass = "paladin"
    elif choice == 7:
        cLass = "ranger"
    elif choice == 8:
        cLass = "rogue"
    elif choice == 9:
        cLass = "sorcerer"
    elif choice == 10:
        cLass = "warlock"
    elif choice == 11:
        cLass = "wizard"
    elif choice == "n/a":
        print("nice try. Pick a class")
        return
    choice2 = var2.get()
    if choice2 == 1:
        race = "dragonborn"
    elif choice2 == 2:
        race = "dwarf"
    elif choice2 == 3:
        race = "elf"
    elif choice2 == 4:
        race = "half-elf"
    elif choice2 == 5:
        race = "halfling"
    elif choice2 == 6:
        race = "half-orc"
    elif choice2 == 7:
        race = "human"
    elif choice2 == 8:
        race = "gnome"
    elif choice2 == 9:
        race = "tiefling"
    elif choice2 == None:
        return
    global name
    name = name_Tf.get()
    cLass = selection()
    global level
    global frameDICE
    level = sp.get()
    if race == "n/a":
        return
    if cLass == "n/a":
        return
    if int(level) >=1 and int(level) <= 20:
        frame1.destroy()
        frame2.destroy()
        frame3.destroy()
        frame4.destroy()
        if cLass in classes:
            if int(level) >=1 and int(level) <= 20:
                create_dnd_character(cLass, race, level)
            else:
                return

frame1 = Label(ws)
frame1.pack()
frame2 = LabelFrame(frame1, text='Class', padx=30, pady=10)
frame2.grid(row=3, columnspan=3,padx=30)
frame3 = LabelFrame(frame1, text='Race', padx=30, pady=10)
frame4 = LabelFrame(frame1, text='Level', padx=30, pady=10)
var =IntVar()
var2 =IntVar()
# buttons buttons buttons and more buttons
Label(frame1, text="Your Character's Name:").grid(row=0, column=0, padx=5, pady=5)

Radiobutton(frame2, text='Barbarian', variable=var, value=1,command=selection).pack()

Radiobutton(frame2, text='Bard', variable=var, value=2,command=selection).pack()

Radiobutton(frame2, text='Cleric', variable=var, value=3,command=selection).pack(anchor=W)

Radiobutton(frame2, text='Fighter', variable=var, value=4,command=selection).pack()

Radiobutton(frame2, text='Monk', variable=var, value=5,command=selection).pack()

Radiobutton(frame2, text='Paladin', variable=var, value=6,command=selection).pack()

Radiobutton(frame2, text='Ranger', variable=var, value=7,command=selection).pack()

Radiobutton(frame2, text='Rogue', variable=var, value=8,command=selection).pack(anchor=W)

Radiobutton(frame2, text='Sorcerer', variable=var, value=9,command=selection).pack(anchor=W)

Radiobutton(frame2, text='Warlock', variable=var, value=10,command=selection).pack()

Radiobutton(frame2, text='Wizard', variable=var, value=11,command=selection).pack(anchor=W)
name_Tf = Entry(frame1)
frame3.grid(row=5, columnspan=6, padx=30 )
frame4.grid(row=6, columnspan=7, padx=30 )
name_Tf.grid(row=0, column=2)


Radiobutton(frame3, text='Dragonborn - +2 STR +1 CON', variable=var2, value=1,command=selectionrace()).pack()

Radiobutton(frame3, text='Dwarf - +2 CON and subrace', variable=var2, value=2,command=selectionrace()).pack()

Radiobutton(frame3, text='Elf - +2 DEX and subrace', variable=var2, value=3,command=selectionrace()).pack(anchor=W)

Radiobutton(frame3, text='Half-Elf - +2 CHA', variable=var2, value=4,command=selectionrace()).pack()

Radiobutton(frame3, text='Halfling - +2 DEX', variable=var2, value=5,command=selectionrace()).pack()

Radiobutton(frame3, text='Half-Orc - +2 STR +1 CON', variable=var2, value=6,command=selectionrace()).pack()

Radiobutton(frame3, text='Human +1 TO ALL', variable=var2, value=7,command=selectionrace()).pack()

Radiobutton(frame3, text='Gnome +2 INT', variable=var2, value=8,command=selectionrace()).pack(anchor=W)

Radiobutton(frame3, text='Tiefling +1 INT +2 CHA', variable=var2, value=9,command=selectionrace()).pack(anchor=W)

sp = Spinbox(frame4, from_= 1, to = 20, text="level", textvariable=level)
sp.pack()

Button(frame1, text="Submit", command=lambda : submit(), bg="black", fg='white', activebackground='black', activeforeground='grey').grid(row=8, columnspan=8, pady=5)


    
def startassignSTR():
        global frameDICE
        global STR_score
        frameDICE.pack()
        msg = Message( frameDICE, text = "Let's Roll Some Dice!")
        msg.pack()

        main_msg1= Message(frameDICE, text="Choose one to be your Strength score")
        main_msg1.pack()
        def submit_STR_decision(STR_decision):
            global STR_score
            STR_decision = var4.get()
            STR_score = dice_sets[STR_decision-1] + race_STR_bonus 
            dice_sets.pop(STR_decision-1)
            chooseDEX(frameDICE)
            return STR_score

        var4 = IntVar()
            
        if choices[0] == 1:
            Radiobutton(frameDICE, text= dice_1, variable=var4,command= setdecision1(1), value=1).pack(side="left")
        if choices[1] == 2:
            Radiobutton(frameDICE, text= dice_2, variable=var4,command= setdecision2(2), value=2).pack(side="left")
        if choices[2] == 3:
            Radiobutton(frameDICE, text= dice_3, variable=var4,command= setdecision3(3), value=3).pack(side="left")
        if choices[3] == 4:
            Radiobutton(frameDICE, text= dice_4, variable=var4,command= setdecision4(4), value=4).pack(side="left")
        if choices[4] == 5:
            Radiobutton(frameDICE, text= dice_5, variable=var4,command= setdecision5(5), value=5).pack(side="left")
        if choices[5] == 6:
            Radiobutton(frameDICE, text= dice_6, variable=var4, command= setdecision6(6), value=6).pack(side="left")

        Button(frameDICE, text="Submit", command= lambda: submit_STR_decision(decision), bg="black", fg="white", activebackground="white", activeforeground="black").pack()





    
    


     


def create_dnd_character(yourclass, yourrace, level=int()): 
    newframe = Frame(root)
    newframe.pack()
    displaytext= StringVar()
    displaytext.set("")
    var3 = IntVar()
    global race_CHA_bonus
    global race_CON_bonus
    global race_INT_bonus
    global race_DEX_bonus 
    global race_STR_bonus 
    global race_WIS_bonus
    global frameDICE
    global refreshedFRAME
    global CONframe
    global WISframe
    global INTframe
    global CHAframe
    global STR_score 
    global WIS_score
    global CHA_score
    global INT_score
    global DEX_score
    global CON_score

    global dice_1 
    global dice_2 
    global dice_3 
    global dice_4 
    global dice_5
    global dice_6
    global health_die

    # set classes health die
    if yourclass=="fighter":
        health_die = 10
        
    
    if yourclass=="wizard":
        health_die = 6
    
    if yourclass=="barbarian":
        health_die = 12
    
    if yourclass=="bard":
        health_die = 8
    
    if yourclass=="cleric":
        health_die = 8
    
    if yourclass=="druid":
        health_die = 8

    if yourclass=="monk":
        health_die = 8

    if yourclass=="paladin":
        health_die = 10

    if yourclass=="ranger":
        health_die = 10

    if yourclass=="rogue":
        health_die = 8

    if yourclass=="sorcerer":
        health_die = 6
    
    if yourclass=="warlock":
        health_die = 8

    # set races health die

    if yourrace == "dwarf":
        race_CON_bonus = 2
        def variant():
            global currentvariant
            global race_WIS_bonus
            global extra_hp_per_level
            global race_STR_bonus
            varchoice = var3.get()
            if varchoice == 1:
                currentvariant = "Hill Dwarf"
                race_WIS_bonus = 1
                extra_hp_per_level = 1
                newframe.destroy()
                startassignSTR()
                return currentvariant, race_WIS_bonus, extra_hp_per_level
            elif varchoice == 2:
                currentvariant = 'Mountain Dwarf'
                race_STR_bonus = 2
                newframe.destroy()
                startassignSTR()
                return currentvariant, race_STR_bonus
        displaytext.set("What kind of dwarf are you?")
        Radiobutton(newframe, text='Hill Dwarf - +1 WIS, and extra 1 hit point per level', variable=var3, value=1, command = variant()).pack()
        Radiobutton(newframe, text='Mountain Dwarf - +2 STR', variable=var3, value=2, command=variant()).pack()
        Button(newframe, text="Submit", command= lambda : variant(), padx=50, pady=5, bg="black", fg='white', activebackground='black', activeforeground='grey').pack(anchor="center")
    if yourrace == "elf":
        global race_DEX_bonus
        race_DEX_bonus = 2
        race = "Elf"
        
        def variant():
            global currentvariant
            global race_INT_bonus
            global extra_hp_per_level
            global race_WIS_bonus
            global race_CHA_bonus
            global race
            varchoice = var3.get()
            if varchoice == 1:
                currentvariant = "High Elf"
                race_INT_bonus = 1
                extra_hp_per_level = 0
                newframe.destroy()
                startassignSTR()
                
                return currentvariant, race_INT_bonus
            if varchoice == 2:
                currentvariant = 'Wood Elf'
                race_WIS_bonus = 1
                newframe.destroy()
                startassignSTR()
                
                return currentvariant, race_WIS_bonus
            if varchoice == 3:
                currentvariant = 'Drow'
                race_CHA_bonus = 1
                newframe.destroy()
                startassignSTR()
                
                return currentvariant, race_CHA_bonus
        displaytext.set("What kind of ELF are you?")
        Radiobutton(newframe, text='High Elf - +1 INT', variable=var3, value=1, command= variant()).pack()
        Radiobutton(newframe, text='Wood Elf - +1 WIS', variable=var3, value=2, command= variant()).pack()
        Radiobutton(newframe, text='Drow - +1 CHA', variable=var3, value=3, command= variant()).pack()
        Button(newframe, text="Submit", command= lambda: variant(), padx=50, pady=5, bg="black", fg='white', activebackground='black', activeforeground='grey').pack(anchor="center")
        
        
    if yourrace =="halfling":
        race_DEX_bonus = 2
        startassignSTR()
    if yourrace == "human":
        race_CON_bonus = 1
        race_DEX_bonus = 1
        race_INT_bonus = 1
        race_CHA_bonus = 1
        race_STR_bonus = 1
        startassignSTR()
    if yourrace == "dragonborn":
        race_STR_bonus = 2
        race_CHA_bonus = 1
        startassignSTR()
    if yourrace == "gnome": 
        race_INT_bonus = 2 
        startassignSTR()
    if yourrace == "half-elf":
        race_CHA_bonus = 2
        startassignSTR()
    if yourrace == "half-orc":
        race_STR_bonus = 2
        race_CON_bonus = 1
        startassignSTR()
    if yourrace == "tiefling":
        race_INT_bonus = 1
        race_CHA_bonus = 2
        startassignSTR()
    
frameRESULTS = Frame(root)
    
    


# modifier section

def printscores():
    global health_die
    global CON_modifier
    global STR_score
    global STR_modifier
    global health
    global level
    global CON_score
    global frameRESULTS
    global INT_score
    global WIS_score
    global CHA_score
    global currentvariant
    global pathToCharacter
    global pathToCurrent
    level = int(level)
    leve= level
    frameRESULTS.pack()
    for x in range(leve):
        health_die = int(health_die)
        health = int(health)
        randomnumber = random.randint(1,health_die)
        health += randomnumber
        
        CON_modifier = round((CON_score-10)/2)
        STR_modifier = round((STR_score-10)/2)
        DEX_modifier = round((DEX_score-10)/2)
        INT_modifier = round((INT_score-10)/2)
        WIS_modifier = round((WIS_score-10)/2)
        CHA_modifier = round((CHA_score-10)/2)
        
        health += (CON_modifier)
        health += extra_hp_per_level
        global message_content
        global message
        randomnumber = str(randomnumber)
        health_die = str(health_die)
        health = str(health)
        message_content = ('You rolled a(n) ' + randomnumber +  ' out of ' + health_die + " You're current health is: " + health)
        message = Label(frameRESULTS, text=message_content)
        message.pack(side="top", padx="10", anchor="n")
    if round((STR_score-10)/2) >= 0:
        STR_mod= "+"
    else:
        STR_mod = "-"
        STR_modifier = round((STR_score-10)/2)*-1
    if round((DEX_score-10)/2) >= 0:
        DEX_mod= "+"
    else:
        DEX_mod = "-"
        DEX_modifier = round((DEX_score-10)/2)*-1
    if round((CON_score-10)/2) >= 0:
        CON_mod= "+"
    else:
        CON_mod = "-"
        CON_modifier= round((CON_score-10)/2)*-1
    if round((INT_score-10)/2) >= 0:
        INT_mod= "+"
    else:
        INT_mod = "-"
        INT_modifier = round((INT_score-10)/2)*-1
    if round((WIS_score-10)/2) >= 0:
        WIS_mod= "+"
    else:
        WIS_mod = "-"
        WIS_modifier = round((WIS_score-10)/2)*-1
    if round((CHA_score-10)/2) >= 0:
        CHA_mod= "+"
    else:
        CHA_mod = "-"
        CHA_modifier = round(((CHA_score-10)/2)*-1)
    total_health = Label(frameRESULTS, text="Your total health is: "+health)
    total_health.pack(side="top", padx="10", pady="10")
    # save it all to the character
    global name
    if currentvariant != "none":
        variant=" ("+currentvariant+")"
    else:
        variant = ""
    if name != "":
        pathToPlayerCharacter=str(str(path)+f"/{name}.pdf")
        pathToCurrent = pathToPlayerCharacter
    else:
        with open(logfile, "r") as file:
            length = file.readlines()
            truelength = len(length)
            pathToCurrent=str(str(path)+f"/characters/CharacterNum{truelength}.pdf")
    scores={
            'STR': str(STR_mod)+str(STR_modifier),
            'CON': str(CON_mod)+str(CON_modifier),
            'DEX': str(DEX_mod)+str(DEX_modifier),
            'WIS': str(WIS_mod)+str(WIS_modifier),
            'INT': str(INT_mod)+str(INT_modifier),
            'CHA' : str(CHA_mod)+str(CHA_modifier),
            'STRmod': STR_score,
            'CONmod': CON_score,
            'DEXmod ': DEX_score,
            'WISmod': WIS_score,
            'INTmod': INT_score,
            'CHamod': CHA_score,
            'Initiative': str(DEX_mod)+str(DEX_modifier),
            'HPMax' : health,
            'Race ': race.capitalize()+variant,
            'CharacterName' : name,
            'CharacterName2': name,
            'ClassLevel': str(cLass).capitalize()+" "+str(level)


        }
    
    try:
        fillpdfs.write_fillable_pdf(pathToCharacter, pathToCurrent, scores)
        with open(logfile, "a") as file:
            file.write("Wrote changes to temp file \n")
    except:
        with open(logfile, "a") as file:
            file.write("Error Saving file. Saving data to data.txt \n")
        with open("data.txt", "a") as data:
            data.write(scores)
        

    st = "Strength:"
    global STR_content
    STR_content = (st, STR_score, "(", STR_mod, STR_modifier,")")
    STR_message = Label(frameRESULTS, text=STR_content)
    STR_message.pack(padx="10", side="top")
    de = "Dexterity:"
    DEX_content = (de, DEX_score, "(",DEX_mod, DEX_modifier, ")",)
    DEX_message = Label(frameRESULTS, text=DEX_content)
    DEX_message.pack(side="top", padx="10", anchor="n")
    co = "Constitution:"
    CON_content = (co, CON_score, "(",CON_mod, CON_modifier,")")
    CON_message = Label(frameRESULTS, text=CON_content)
    CON_message.pack(side="top", padx="10", anchor="n")
    intel = "Inteligence:"
    INT_content = (intel, INT_score, "(",INT_mod, INT_modifier,")")
    INT_message = Label(frameRESULTS, text=INT_content)
    INT_message.pack(side="top", padx="10", anchor="n")
    wis = "Wisdom:"
    WIS_content = (wis, WIS_score,"(",WIS_mod, WIS_modifier, ")")
    WIS_message = Label(frameRESULTS, text=WIS_content)
    WIS_message.pack(side="top", padx="10", anchor="n")
    cha = "Charisma:"
    CHA_content = (cha, CHA_score,"(",CHA_mod, CHA_modifier,")")
    CHA_message = Label(frameRESULTS, text=CHA_content)
    CHA_message.pack(side="top", padx="10", anchor="n")

    savedFileLocation = Label(frameRESULTS, text=f"Your character's file was save to:")
    savedFileLocation.pack(side="top", padx="20", pady="20", anchor="center" )
    fileLocationSaved=Label(frameRESULTS, text=pathToCurrent)
    fileLocationSaved.pack(side="top", padx="20", pady="20", anchor="center" )


        
        
        
        


 


root.mainloop()
