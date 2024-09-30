from tkinter import *

root = Tk()

root.geometry("500x600")
root.minsize(200, 300)
root.maxsize(600, 700)

def delete():
    my_listbox.delete(ANCHOR)
    
def Select():
    selected_item = my_listbox.get(ANCHOR)
    selected_label.config(text=selected_item)


frame = LabelFrame(root,padx=10,pady=10)
frame.pack()

my_listbox = Listbox(frame)
my_listbox.pack(pady=10,padx=10)

my_listbox.insert(END, "pizza")
my_listbox.insert(END, "burger")
my_listbox.insert(END, "dosa")
my_listbox.insert(END, "chole bhature")

r = IntVar()

my_list = ["Pavbhaji","Sendwich","vadapav"]

for i in my_list:
    my_listbox.insert(END,i)

b0 = Button(frame,text="delete",command=delete ).pack()

b1 = Button(frame,text="Select",command=Select).pack()

b2 = Button(frame,text="close",command=root.destroy)
b2.pack()

selected_label = Label(root)
selected_label.pack()


root.mainloop()

