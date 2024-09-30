from tkinter import *

root = Tk()

Name = StringVar() 

e = Entry(root, width=50, bg="lightblue", fg="red", borderwidth=5,textvariable=Name)
e.pack(padx=10,pady=10)
e.insert(0,"Enter Your Name = ")

def myclick():
    mylabel = Label(root,text=f"my name is {Name.get().strip()}")
    mylabel.pack() 

    
myButton = Button(root,text="Click ME",command=myclick)
myButton.pack()

root.mainloop()