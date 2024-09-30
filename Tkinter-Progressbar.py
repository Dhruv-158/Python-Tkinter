from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.geometry("1200x1017")
root.title("Progressbar")

def step():
    # my_progress["value"] += 20
    # my_progress.start(6)
    for x in range(5):
        my_progress["value"] += 20
        root.update_idletasks()
        time.sleep(1)
    
def Stop():
    my_progress.stop()    

my_progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
my_progress.pack(pady=20)

my_button = Button(root,text = "Progress",command =step)
my_button.pack(pady=20)

my_button1 = Button(root,text = "Stop",command =Stop)
my_button1.pack(pady=20)

my_btn = Button(root,text = "Close",command =root.destroy)
my_btn.pack(pady=20)

 
root.mainloop()