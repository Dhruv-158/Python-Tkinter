from tkinter import *

root = Tk() 
root.geometry("300x200") 

w = Label(root, text ='GeeksForGeeks', font = "50") 
w.pack() 

# Create a Menubutton
menubutton = Menubutton(root, text="Menu", 
                        bg="lightblue", fg="black", 
                        activebackground="blue", activeforeground="white",
                        relief="raised", bd=3,
                        cursor="hand2", direction="right",
                        justify="center", wraplength=100) 
	
menubutton.menu = Menu(menubutton) 
menubutton["menu"] = menubutton.menu 

# Create IntVar variables
var1 = IntVar() 
var2 = IntVar() 
var3 = IntVar() 

# Add checkbuttons to the menu
menubutton.menu.add_checkbutton(label="Courses", variable=var1) 
menubutton.menu.add_checkbutton(label="Students", variable=var2) 
menubutton.menu.add_checkbutton(label="Careers", variable=var3) 
	
menubutton.pack() 
root.mainloop()
