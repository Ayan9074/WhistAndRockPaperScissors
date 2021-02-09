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
    file_path = os.path.join(dir_path,'rockpaperscissors.py')
    os.system(f'py {file_path}')

root = tk.Tk()

text1 = tk.Text(root, height=20, width=30)
photo = tk.PhotoImage(file='./rps.png')
text1.insert(tk.END, '\n')
text1.image_create(tk.END, image=photo)

button_a = tk.Button(text="Home", command=back)
button_b = tk.Button(text="Play The Game", command=maingame)


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
text2.insert(tk.END,'\nHow To Play RockPaperScissors\n', 'big')
text = """
To play the game press either the rock, paper or scissors button.
Next the computer will choose either of the three options and the results will be compared.
The scores will cumulate over time and will be displayed at the bottom
"""
text2.insert(tk.END, text, 'color')
text2.insert(tk.END, 'follow-up\n', 'follow')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()