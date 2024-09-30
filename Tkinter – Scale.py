from tkinter import *


root = Tk() 
root.geometry("400x300") 

v1 = DoubleVar() 

def show1(): 
	
	sel = "Horizontal Scale Value = " + str(v1.get()) 
	l1.config(text = sel, font =("Courier", 14)) 


s1 = Scale( root, variable = v1, 
		from_ = 1, to = 100, 
		orient = HORIZONTAL) 

l3 = Label(root, text = "Horizontal Scaler") 

b1 = Button(root, text ="Display Horizontal", 
			command = show1, 
			bg = "yellow") 

l1 = Label(root) 


s1.pack(anchor = CENTER) 
l3.pack() 
b1.pack(anchor = CENTER) 
l1.pack() 

v2 = DoubleVar()

def show2(): 
      
    sel = "Vertical Scale Value = " + str(v2.get())  
    l2.config(text = sel, font =("Courier", 14)) 
  
s2 = Scale( root, variable = v2, 
           from_ = 50, to = 1, 
           orient = VERTICAL)  
  
l4 = Label(root, text = "Vertical Scaler") 
  
b2 = Button(root, text ="Display Vertical", 
            command = show2, 
            bg = "purple",  
            fg = "white") 
  
l2 = Label(root) 
  
s2.pack(anchor = CENTER)  
l4.pack() 
b2.pack() 
l2.pack() 

root.mainloop() 
