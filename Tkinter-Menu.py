
from tkinter import *

root = Tk()

root.title("MENU")
root.geometry("500x600")
root.maxsize(600,700)
root.minsize(200,300)

my_menu = Menu(root)
root.config(menu=my_menu)

# Create a menu item

file_menu = Menu(my_menu,tearoff = 0)
my_menu.add_cascade(label ="File", menu=file_menu)
file_menu.add_command(label = "New" , command = None )
file_menu.add_command(label ='New File', command = None) 
file_menu.add_command(label ='Open...', command = None) 
file_menu.add_command(label ='Save', command = None) 
file_menu.add_command(label = "Exit" , command = root.quit )

# Adding Edit Menu and commands 
edit = Menu(my_menu, tearoff = 0) 
my_menu.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = None) 
edit.add_command(label ='Copy', command = None) 
edit.add_command(label ='Paste', command = None) 
edit.add_command(label ='Select All', command = None) 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None) 

# Adding Help Menu 
help_ = Menu(my_menu, tearoff = 0) 
my_menu.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None) 


root.mainloop()
