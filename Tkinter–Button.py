from tkinter import *
def button_clicked():
    print("""
             ( ♡  ♡ )
                 ^ 
            """)
def dont_click():
    print("             bye bye 😘   ")
    root.destroy()
def on_enter(event):
    button.config(bg="blue", fg="white")

def on_leave(event):
    button.config(bg="lightgray", fg="black") 
root = Tk()
root.geometry("1000x1000")
root.minsize(300,200)
root.maxsize(1100,1100)
button = Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="red", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100
                   )
button.pack(padx=20, pady=20)
button.bind("<Enter>",on_enter)
button.bind("<Leave>",on_leave)
btn = Button(root,
            text = "DON'TClick me !", 
            command = dont_click
            ) 
# Set the position of button on the top of window 
btn.pack(side = 'top')     
root.mainloop()

