from tkinter import *
from tkinter import messagebox
# entry = tk.Entry(parent, options)

      
root = Tk()
txt_name=StringVar()
txt_password=StringVar()
root.geometry("1000x500")

def submit():
    name=txt_name.get().strip()
    password=txt_password.get().strip()
    
    if not name or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
    else:
        print(f"""
              the username is = {name}
              the user password is = {password}
              """)
        
    txt_name.set(" ")
    txt_password.set(" ")
name_label = Label(
                root,
                text="username :-",
                padx=5,
                font=('calibre',10, 'bold'))

name_entry = Entry(root,
              textvariable = txt_name,
              font=('calibre',10,'normal')) 
pass_label = Label(
                root,
                text="Password :-",
                padx=5,
                font=('calibre',10, 'bold')
             )

pass_entry = Entry(root,
              textvariable = txt_password,
              show = '*',
              font=('calibre',10,'normal')) 
sub_btn = Button(root,
                 command = submit,
                 text="SUBMIT",
                 font=('calibre',10, 'bold'),
                 width=10,
                 height=1,
                 bg="blue",
                 activebackground="green",
                 activeforeground="red",
                 relief="solid"
                 )
Close_btn = Button(root,
                 command = root.destroy,
                 text="Close",
                 font=('calibre',10, 'bold'),
                 width=10,
                 height=1,
                 bg="blue",
                 activebackground="red",
                 activeforeground="black",
                 relief="solid") 

name_label.grid(row=0, column=0, pady=5)  
name_entry.grid(row=0, column=1, pady=5)  
pass_label.grid(row=1, column=0, pady=5)  
pass_entry.grid(row=1, column=1, pady=5)  
sub_btn.grid(row=3, column=1, pady=5)     
Close_btn.grid(row=3, column=2, pady=5)

root.mainloop()
