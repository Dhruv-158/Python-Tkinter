from tkinter import *

root = Tk()
root.geometry("500x600") 
root.minsize(200,300)
root.maxsize(700,800)
root.title("Radiobtn")

def Show():
    Label(frame,text=r.get()).pack()
    
frame = LabelFrame(root,text=" ")
frame.pack()

r = IntVar()
Radiobutton(frame,text="Option 1",variable = r,value = 1).pack()
Radiobutton(frame,text="Option 2",variable = r,value = 2).pack()

show = Button(frame,text = "Show",command = Show)
show.pack()

destroy = Button(frame,text = "Close",command = root.destroy)
destroy.pack()

root.mainloop()

