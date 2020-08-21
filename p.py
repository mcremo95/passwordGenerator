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
    print(list)

def helloCallBack():
    generetor(3)
    tmp = ""
    tmp = tmp.join(list)
    print(tmp)

finestra = tk.Tk()

combobox = ttk.Combobox(finestra, state="readonly",
                            values=[
                                    "2", 
                                    "3",
                                    "4",
                                    "5"])

combobox.current(0)

B = tk.Button(finestra, text ="Hello", command = helloCallBack)
label = tk.Label(text="Hello, Tkinter")
CheckVar1 = IntVar()
C1 = Checkbutton(finestra, text = "Numbers", variable = CheckVar1,\
                    offvalue = 0, height=5, width = 20)

label.pack()
C1.pack()
combobox.pack()
B.pack()
finestra.mainloop()