# importing modules
import tkinter as tk
from tkinter import ACTIVE
import random
import re
import os

# initialize modules
Root = tk.Tk()
Root.title("Whist")
Root.configure(bg='#ff1234')

# initialize the card system and hand out cards to player and computer
usedcards = []
cardvals = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
cardssuits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [[cs,cv] for cs in cardssuits for cv in cardvals]
trumpsuitv = random.choice(cardssuits)

def check():
    x = random.choice(deck)
    while x in usedcards:
        x = random.choice(deck)
    usedcards.append(x)
    return x

computercardslist = [check() for i in range(0,7)]
playercardslist = [check() for i in range(0,7)]
temp = []

# initializing GUI items and define variables
trumpsuit = tk.Label(text='Trump Suit: {}'.format(trumpsuitv))
title1 = tk.Label(text='Whist')
usercards = tk.Label(text='Your Cards')
compcards = tk.Label(text='Computer cards')
enterkeep= tk.Label()
compcardsavailable= tk.Listbox(Root)
usercardsavailable = tk.Listbox(Root)
compcard = tk.Listbox(Root, height=1)
usercard = tk.Listbox(Root, height=1)
scorel = tk.Label(text='Tricks: ')
score = tk.Listbox(Root, height=2)

# add player cards to GUI
for card in computercardslist:
    compcardsavailable.insert("end", card)
for card in playercardslist:
    usercardsavailable.insert("end", card)


def HomePage():
    Root.destroy()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'runfile.py')
    os.system(f'py {file_path}')

def Help():
    Root.destroy()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'help.py')
    os.system(f'py {file_path}')



# moves that are in the game
def chooseaction():
    bad_chars = ['[',']','"',"'", ',','(',')']
    if compcard.size() == 0:
        tempstring = str(usercardsavailable.get(ACTIVE)).split()[:1]
        tempstring2 = str(usercardsavailable.get(ACTIVE)).split()[1:]
        for i in bad_chars:
            tempstring = str(tempstring).replace(i,'')
        for i in bad_chars:
            tempstring2 = str(tempstring2).replace(i,'')
        x = usercardsavailable.curselection()
        if not x:
            return None
        # THEORY FOR WHAT CARD TO USE
        for i in range(0,compcardsavailable.size()+1):
            if ' '.join(re.sub("[(|)|,|'|]", "", str(compcardsavailable.get(int(i)))).split()[:1]) == tempstring and cardvals.index(' '.join(re.sub("[(|)|,|'|]", "", str(compcardsavailable.get(int(i)))).split()[1:])) > cardvals.index(tempstring2):
                todel = compcardsavailable.get(int(i))
                break
        if 'todel' not in locals():
            print('hi1')
            for i in range(0,compcardsavailable.size()+1):
                if ' '.join(re.sub("[(|)|,|'|]", "", str(compcardsavailable.get(int(i)))).split()[:1]) == tempstring and cardvals.index(' '.join(re.sub("[(|)|,|'|]", "", str(compcardsavailable.get(int(i)))).split()[1:])) < 6:
                    todel = compcardsavailable.get(int(i))
                    break
        if 'todel' not in locals():
            print('hi2')
            for i in range(0,compcardsavailable.size()+1):
                if ' '.join(re.sub("[(|)|,|'|]", "", str(compcardsavailable.get(int(i)))).split()[:1]) == tempstring:
                    todel = compcardsavailable.get(int(i))
                    break
        if 'todel' not in locals():
            print('hi3')
            for i in range(0,compcardsavailable.size()+1):
                if cardvals.index(' '.join(re.sub("[(|)|,|'|]", "", str(compcardsavailable.get(int(i)))).split()[1:])) < 6:
                    todel = compcardsavailable.get(int(i))
                    break
        if 'todel' not in locals():
            print('hi4')
            todel = compcardsavailable.get(int(random.randint(0, compcardsavailable.size() - 1)))
        print('Card Being Deleted from compcards:' , todel)
        compcardsavailable.delete(compcardsavailable.get(0, "end").index(todel))
        try:
            usercard.delete(0)
            usercard.insert("end", usercardsavailable.get(ACTIVE))
            cardsinplay['state'] = 'normal'
            compcard.delete(0)
            compcard.insert("end", todel)
            usercardsavailable.delete(usercardsavailable.curselection())
        except:
            usercard.insert("end", usercardsavailable.get(ACTIVE))
            usercardsavailable.delete(usercardsavailable.curselection())
            cardsinplay['state'] = 'normal'
            compcard.insert("end", compcardsavailable.delete(int(random.randint(0, compcardsavailable.size() - 1))))
        choose['state'] = 'disabled'
        temp.clear()
        temp.append(usercard.get(0))
        temp.append(compcard.get(0))
    else:
        x = usercardsavailable.curselection()
        if not x:
            return None
        try:
            usercard.delete(0)
            usercard.insert("end", usercardsavailable.get(ACTIVE))
            cardsinplay['state'] = 'normal'
            usercardsavailable.delete(usercardsavailable.curselection())
        except:
            usercard.insert("end", usercardsavailable.get(ACTIVE))
            usercardsavailable.delete(usercardsavailable.curselection())
            cardsinplay['state'] = 'normal'
        print('bruv')
        choose['state'] = 'disabled'
        temp.clear()
        temp.append(compcard.get(0))
        temp.append(usercard.get(0))
# simulate game (winning card decided here)
def simulate():
    print(temp)
    if True:
        if trumpsuitv == ' '.join(re.sub("[(|)|,|'|]", "", str(temp[0])).split()[:1]):
            if trumpsuitv == ' '.join(re.sub("[(|)|,|'|]", "", str(temp[1])).split()[:1]):
                if cardvals.index(' '.join(re.sub("[(|)|,|'|]", "", str(temp[0])).split()[1:])) > cardvals.index(' '.join(re.sub("[(|)|,|'|]", "", str(temp[1])).split()[1:])):
                    userpoint = True
                    print('end1')
                else:
                    userpoint = False
                    print('end2')
            else:
                userpoint = True
                print('end3')
        elif trumpsuitv == ' '.join(re.sub("[(|)|,|'|]", "", str(compcard.get(0))).split()[:1]):
            userpoint = False
            print('end4')
        elif ' '.join(re.sub("[(|)|,|'|]", "", str(temp[0])).split()[:1]) == ' '.join(re.sub("[(|)|,|'|]", "", str(temp[1])).split()[:1]):
            if cardvals.index(' '.join(re.sub("[(|)|,|'|]", "", str(temp[0])).split()[1:])) > cardvals.index(' '.join(re.sub("[(|)|,|'|]", "", str(temp[1])).split()[1:])):
                userpoint = True
                print('end5')
            else:
                userpoint = False
                print('end6')
        else:
            userpoint = True
            print('end7')
    if compcard.size() == 0:
        return None
    if compcard.get(0) == temp[0] and userpoint == True:
        userpoint = False
        print('switchone')
    elif compcard.get(0) == temp[0] and userpoint == False:
        userpoint = True
        print('switchtwo')
    if userpoint == True:
        score.insert(0, "Your Tricks: {0}".format(int(score.get(0).split()[-1])+1))
        score.delete(1)
        usercard.delete(0)
        compcard.delete(0)
    else:
        print('hola')
        score.insert(1, "Comp Tricks: {0}".format(int(score.get(1).split()[-1])+1))
        score.delete(2)
        usercard.delete(0)
        compcard.delete(0)
        for i in range(0,compcardsavailable.size()+1):
            try:
                if cardvals.index(' '.join(re.sub("[(|)|,|'|]", "", str(compcardsavailable.get(int(i)))).split()[1:])) > 12:
                    todel = compcardsavailable.get(int(i))
                    break
            except:
                break
        if 'todel' not in locals():
            for i in range(0,compcardsavailable.size()+1):
                try:
                    if cardvals.index(' '.join(re.sub("[(|)|,|'|]", "", str(compcardsavailable.get(int(i)))).split()[1:])) > 9:
                        todel = compcardsavailable.get(int(i))
                        break
                except:
                    break
        if 'todel' not in locals():
            todel = compcardsavailable.get(int(random.randint(0, compcardsavailable.size() - 1)))
        compcardsavailable.delete(compcardsavailable.get(0, "end").index(todel))
        compcard.insert("end", todel)
    cardsinplay['state'] = 'disabled'
    choose['state'] = 'normal'

# Create scoreboard
choose=tk.Button(Root, text= "Choose Card", command=lambda: chooseaction())
cardsinplay = tk.Button(text='Simulate', command=simulate)
score.insert(0, "Your Tricks: 0")
score.insert(1, "Comp Tricks: 0")

# grid items onto gui
def griditems():
    title1.grid(row= 1, column= 3)
    trumpsuit.grid(row=1, column=6)
    usercards.grid(row= 2, column= 4)
    compcards.grid(row=2, column= 2)
    compcardsavailable.grid(row= 3, column= 2)
    choose.grid(row=3, column=3)
    usercardsavailable.grid(row=3, column=4)
    compcard.grid(row=4, column=2)
    cardsinplay.grid(row=4, column=3)
    usercard.grid(row=4, column=4)
    scorel.grid(row=3, column=5)
    score.grid(row=3, column=6)

griditems()


button_a = tk.Button(text="HomePage", command=HomePage)
button_b = tk.Button(text="Help", command=Help)
button_a.grid(row=0, column=2)
button_b.grid(row=0, column=4)


def run():
    if __name__ == '__main__':
        Root.mainloop()
run()