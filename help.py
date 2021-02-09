import tkinter as tk
import os


def back():
    root.destroy()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'runfile.py')
    os.system(f'py {file_path}')

def maingame():
    root.destroy()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'test.py')
    os.system(f'py {file_path}')

root = tk.Tk()

text1 = tk.Text(root, height=20, width=30)
photo = tk.PhotoImage(file='./whist.png')
text1.insert(tk.END, '\n')
text1.image_create(tk.END, image=photo)

button_a = tk.Button(text="Back", command=back)
button_b = tk.Button(text="PlayTheGame", command=maingame)


button_a.pack(side=tk.TOP)
button_b.pack(side=tk.TOP)
text1.pack(side=tk.LEFT)


text2 = tk.Text(root, height=20, width=50)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color',
                    foreground='#476042',
                    font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('follow',
               '<1>',
               lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
text2.insert(tk.END,'\nHow To Play Whist\n', 'big')
text = """
In this version of whist you will be playing against the computer.
Each player (you and the computer) will be given 7 cards to play with.
These cards can be seen in the middle of the screen.
The trump suit can be seen at the top right and your tricks can be seen middle left of the screen.
To choose a card to play, press the card than press choose. Next press simulate to see if you win or the computer wins that round.
If the computer wins it plays its card first. If you win you get to play a card first.
The way the simulate button checks who wins:
First it checks if the second players card is the same as the first play, if not the first player wins unless the second player played a trump card which in that case it would check if both cards were trump cards and see which one was higher ranked.
If a trump card was not selected and the second player did not have any cards left other than another suit than player one automatically wins the trick.
If the second player did choose the same suit than the player with the highest card value wins.
"""
text2.insert(tk.END, text, 'color')
text2.insert(tk.END, 'follow-up\n', 'follow')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()