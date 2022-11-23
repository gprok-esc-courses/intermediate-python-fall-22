from abc import abstractmethod, ABC
from tkinter import *
from tkinter import ttk


class ButtonObserver(ABC):
    @abstractmethod
    def action(self):
        pass

class DBAction(ButtonObserver):
    def action(self):
        print("Database updated")

class LogFileAction(ButtonObserver):
    def action(self):
        print("Log file updated")

class EmailAction(ButtonObserver):
    def action(self):
        print("Email sent")

button_observers = []

def click_me():
    for obs in button_observers:
        obs.action()


db = DBAction()
log =LogFileAction()
email = EmailAction()
button_observers.append(db)
# button_observers.append(log)
button_observers.append(email)
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Hello Tkinter").grid(column=0, row=0)
ttk.Button(frame, text="Click Me", command=click_me).grid(column=0, row=1)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=0, row=2)
root.mainloop()