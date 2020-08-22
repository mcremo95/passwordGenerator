import tkinter as tk
from tkinter import Checkbutton
from tkinter import IntVar
from tkinter import messagebox
from tkinter import Label
from tkinter import ttk
import random

def generetor(num):
    f = open("parole.txt", "r")
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    global list
    list = []
    for i in range(num):
        list.append(random.choice(lines))
    for i in range(num):
        list[i] = list[i].title()
    #print(list)

def call():
    generetor(int(combobox.get()))
    tmp = ""
    tmp = tmp.join(list)
    if CheckVar1.get() == 1:
        random.seed()
        if (random.randrange(0, 2)) == 1:
            tmp = tmp + str(random.randrange(0, 101))
        else:
            tmp = str(random.randrange(0, 101)) + tmp
    #print(tmp)
    t.configure(state='normal')
    t.delete("1.0","end")
    t.insert('end', tmp)
    t.configure(state='disabled')

def copy():
    finestra.clipboard_clear()
    finestra.clipboard_append(t.get("0.1", "end"))

finestra = tk.Tk()
t = tk.Text(finestra, state='disabled', height=1, width=60)
combobox = ttk.Combobox(finestra, state="readonly",
                            values=[
                                    "2", 
                                    "3",
                                    "4",
                                    "5"])

combobox.current(0)

bottoneGen = tk.Button(finestra, text ="Generate Password", command = call)
bottoneCopy = tk.Button(finestra, text ="Copy to Clipboard", command = copy)
CheckVar1 = IntVar()
C1 = Checkbutton(finestra, selectcolor = "black", text = "Numbers",
                    variable = CheckVar1, offvalue = 0, height=5, width = 20)

t.pack()
C1.pack()
combobox.pack()
bottoneGen.pack()
bottoneCopy.pack()
finestra.mainloop()