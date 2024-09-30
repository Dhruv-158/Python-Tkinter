from tkinter import *

root = Tk()
root.geometry("600x700")
root.minsize(300, 400)
root.maxsize(800, 1017)
root.title("Canvas")

canvas = Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=20)

# Drawing a line
canvas.create_line(50, 50, 250, 150, fill="blue")

# Adding text
canvas.create_text(150, 180, text="Hello, Canvas!", fill="red", font=("Arial", 16))

# Adding a rectangle
canvas.create_rectangle(50, 150, 250, 50, fill="pink")

# Adding a polygon
canvas.create_polygon(50, 150, 250, 150, 250, 50, fill="lightblue")

root.mainloop()
