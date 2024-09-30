from tkinter import *

def show_value():
    value = var.get()
    print("Checkbutton value:", value)
    Label(root,text=var.get()).pack() 

root = Tk()
root.geometry("400x500")
root.title("Check box")
root.minsize(300,400)
root.maxsize(500,600)

frame = LabelFrame(root, text="frame", relief="solid", height=100, width=200)
frame.pack(padx=20, pady=20, anchor="center")  # Center the frame within the root window

# var = IntVar()  # Create an IntVar to track the checkbutton state
var = StringVar()
check_box = Checkbutton(frame, text="You want pizaa ", variable=var, onvalue="Yes, i want 🍕 ", offvalue="No, i want a 🍔 ")
check_box.grid(row=0, column=0)
check_box.deselect()

btn = Button(frame, text="close", command=root.destroy)
btn.grid(row=2, columnspan=2)

show_value_button = Button(frame, text="Show Value", command=show_value)
show_value_button.grid(row=1, columnspan=2)

root.mainloop()
