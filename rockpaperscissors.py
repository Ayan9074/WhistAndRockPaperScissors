from tkinter import *
import random
import tkinter
import os

top = tkinter.Tk()
top.wm_title("ROCKPAPERSCISSORS")
top.geometry("300x200")

userchoice = int
compchoice = int
win = 0

def checkwinner(win, userchoice):
    compchoice = random.randint(1,3)
    if userchoice == compchoice:
        var.set("It's a draw. \n No Points")  
    elif userchoice == 1 and compchoice == 3:
        var.set("You chose Rock, Computer chose Scissors. \nYou win")
        wins.set(wins.get() + 1)
            
    elif userchoice == 1 and compchoice == 2:
        var.set("You chose Rock, Computer chose Paper. \nYou lose")
        wins.set(wins.get() - 1)    
    elif userchoice == 2 and compchoice == 1:
        var.set("You chose Paper, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
        wins.set(wins.get() - 1)    
    elif userchoice == 2 and compchoice == 3:
        var.set("You chose Paper, I chose Scissors. \nYou lose")
        wins.set(wins.get() - 1)   
    elif userchoice == 3 and compchoice == 1:
        var.set("You chose Scissors, I chose Rock. \nYou lose")
        wins.set(wins.get() - 1)    
    elif userchoice == 3 and compchoice == 2:
        var.set("You chose Scissors, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
    else:
        var.set("Error Play again")

def Home():
    top.destroy()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'runfile.py')
    os.system(f'py {file_path}')
def Help():
    top.destroy()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'help2.py')
    os.system(f'py {file_path}')

Button1 = tkinter.Button(text ="Rock", command = lambda: checkwinner(win, 1))
Button2 = tkinter.Button(text ="Paper", command = lambda: checkwinner(win, 2))
Button3 = tkinter.Button(text ="Scissors", command = lambda: checkwinner(win, 3))
var = StringVar()
var.set('Welcome!')
restext = Label(top, textvariable = var)
wins = IntVar()
wins.set(win)
score = Label(top, textvariable = wins)
scorelabel = Label(top, text = "Score:")

button_a = tkinter.Button(text="Go To Homepage", command=Home)
button_b = tkinter.Button(text="Help", command=Help)



def grid():
    Button1.grid(row=0, column=1)
    Button2.grid(row=0, column=2)
    Button3.grid(row=0, column=3)
    restext.grid(row=2, column=2)
    score.grid(row=4, column=2)
    scorelabel.grid(row=3, column=2)
    button_a.grid(row=5, column=2)
    button_b.grid(row=6, column=2)

grid()
top.mainloop()
