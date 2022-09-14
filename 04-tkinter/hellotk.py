from tkinter import *
from tkinter import ttk


def click_me():
    print("Button clicked")


root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Hello Tkinter").grid(column=0, row=0)
ttk.Button(frame, text="Click Me", command=click_me).grid(column=0, row=1)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=0, row=2)
root.mainloop()

