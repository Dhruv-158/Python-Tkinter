# from tkinter import * 


# root = Tk()

# # specify size of window.
# root.geometry("250x170")

# # Create text widget and specify size.
# T = Text(root, height = 5, width = 52)

# # Create label
# # l = Label(root, text = "Fact of the Day")
# # l.config(font =("Courier", 14))

# Fact = """A man can be arrested in
# Italy for wearing a skirt in public."""

# # Create button for next text.
# b1 = Button(root, text = "Next", )

# # Create an Exit button.
# b2 = Button(root, text = "Exit",
# 			command = root.destroy) 

# # l.pack()
# T.pack()
# b1.pack()
# b2.pack()

# # Insert The Fact.
# T.insert(END, Fact)

# root.mainloop()


from tkinter import *

root = Tk()
root.geometry("300x300")
root.title(" Q&A ")

def Take_input():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	if(INPUT == "120"):
		Output.insert(END, 'Correct')
	else:
		Output.insert(END, "Wrong answer")
	
l = Label(text = "What is 24 * 5 ? ")
inputtxt = Text(root, height = 10,
				width = 25,
				bg = "light yellow")
inputtxt.insert(END, "write ans = ")

Output = Text(root, height = 5, 
			width = 25, 
			bg = "light cyan")

Display = Button(root, height = 2,
				width = 20, 
				text ="Show",
				command = lambda:Take_input())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
