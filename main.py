import os
import tkinter as tk

class game:
    def __init__(self):
        Root = tk.Tk()
        Root.title("Whist")
        Root.configure(bg='#ff1234')
        Root.geometry('200x150')

        def maingame():
            Root.destroy()
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(dir_path,'test.py')
            os.system(f'py {file_path}')
        def help():
            Root.destroy()
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(dir_path,'help.py')
            os.system(f'py {file_path}')
        def rps():
            Root.destroy()
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(dir_path,'rockpaperscissors.py')
            os.system(f'py {file_path}')
        def rpshelp():
            Root.destroy()
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(dir_path,'help2.py')
            os.system(f'py {file_path}')


        label_a = tk.Label(text="Welcome to Your Home Page Interface")
        button_a = tk.Button(text="Play Original Whist", command=maingame)
        button_b = tk.Button(text="Whist Help/Rules", command=help)
        button_c = tk.Button(text="Play RockPaperScissors", command=rps)
        button_d = tk.Button(text="RockPaperScissors help", command=rpshelp)

        label_a.grid()
        button_a.grid()
        button_b.grid()
        button_c.grid()
        button_d.grid()

        tk.mainloop()
