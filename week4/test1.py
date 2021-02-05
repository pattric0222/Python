import os
choice = ''
filename = ''

def menu():
    global choice
    print('Menu\n 1.Open Paint\n 2.Open notepad\n 3.Exit ')
    choice = input('Select Menu : ')


def opennotepad():
    filename = 'C:\\Windows\\SysWOW64\\notepad.exe'

    os.system(filename)

def openpaint():
    filename = 'C:\\Windows\\SysWOW64\\mspaint.exe'
    print('Calculate Number %s' %filename)
    os.system(filename)

while True:
    menu()
    if choice.lower() =='y':
        openpaint()
    elif choice =='n':
        opennotepad()
    else:
        break