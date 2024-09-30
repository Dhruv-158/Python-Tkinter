from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ComboBox")
root.geometry("700x600")
root.minsize(300, 400)
root.maxsize(900, 1017)

def selected(event):
    if clicked.get() == "Friday":
        my_label = Label(root, text="It's Friday")
        my_label.pack()
    else:
        my_label = Label(root, text=clicked.get())
        my_label.pack()

def comboclick(event):
    if my_combo.get() == "Friday":
        my_label = Label(root, text="It's Friday")
        my_label.pack()
    else:
        my_label = Label(root, text=my_combo.get())
        my_label.pack()

options = ["      ",
           "Sunday",
           "Monday",
           "Tuesday",
           "Wednesday",
           "Thursday",
           "Friday",
           "Saturday"
           ]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

my_combo = ttk.Combobox(root, value=options)
my_combo.current(0)
my_combo.bind("<<ComboboxSelected>>", comboclick)
my_combo.pack()

root.mainloop()
