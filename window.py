import tkinter as tk
from tkinter import Button, ttk
import subprocess
import threading
import sys

root = tk.Tk()
root.title('Auto Click GUI')
root.geometry('300x200')
root.resizable(False,False)

def quit(event):
    sys.exit()

label1 = ttk.Label (
    root,
    text='Press "s" to start/stop',
    compound='top'
)
label1.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

label2 = ttk.Label (
    root,
    text='Press "e" to exit',
    compound='bottom'
)
label2.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

def start():
    subprocess.call(['python', 'autoclick.py'])

btn = Button(
    root,
    text="click to start",
    command=threading.Thread(target = start).start,
    compound= 'bottom'
)
btn.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

root.bind('e', quit)

root.mainloop()
