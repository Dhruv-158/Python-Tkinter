from tkinter import *

root = Tk()
root.title("Scrollbar")
root.geometry("600x700")
root.minsize(300, 400)
root.maxsize(800, 900)

frame = Frame(root, bg="lightblue")  # Change "lightblue" to any color you prefer
frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(frame, bg="red")  # Change "white" to any color you prefer
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)


scrollbar = Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview, bg="grey")  # Change "grey" to any color you prefer
scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

cframe = Frame(my_canvas,bg="lightblue")

my_canvas.create_window((0, 0), window=cframe, anchor="nw")

for btn in range(20):
    Button(cframe, text=f"button {btn} ").grid(row=btn, column=0, pady=10, padx=10)

root.mainloop()
