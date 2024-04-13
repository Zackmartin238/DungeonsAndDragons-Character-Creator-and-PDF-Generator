import sys, os

def install(module_name):
    os.system(f'{sys.executable} -m pip install {module_name}')

def check(module_name):
    try: 
        __import__(module_name)
        installed = True
        return installed
    except ImportError or ModuleNotFoundError:
        installed = False
        return installed
def Import(module):
    checked = check(module)
    if module == 'tkinter':
        if checked == False:
            print("ah, a special case")
            os.system("sudo apt install python-tk")
            return
        else:
            print(f"Module {module} is installed")
    if checked == True:
        __import__(module)
        print(f"Module {module} is installed")
    if checked == False:
        print(f"{module} not found. Attempting to install")
        install(module)
        __import__(module)