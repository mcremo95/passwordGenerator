import tkinter as tk
import random

def generetor(num):
    f = open("parole.txt", "r")
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    list = []
    for i in range(num):
        list.append(random.choice(lines[i]))
    list = [x.lower() for x in list]
    list = [x.capitalize() for x in list]
    print(list)

finestra = tk.Tk()
label = tk.Label(text="Hello, Tkinter")
label.pack()
finestra.mainloop()