from tkinter import *

# Create the main window
root = Tk()
root.title("Learn Frame")

# Create a frame with a label
frame = LabelFrame(root, text="This is my frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

# Create buttons inside the frame
b1 = Button(frame, text="click")
b2 = Button(frame, text="don't click", command=frame.destroy)  # This button destroys the frame when clicked

# Pack the buttons inside the frame
b1.pack()
b2.pack()

b3 = Button(root,text="close",command=root.destroy)

b3.pack(padx=5,pady=5)

# Run the Tkinter event loop
root.mainloop()
