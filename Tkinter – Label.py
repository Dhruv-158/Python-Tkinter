from tkinter import *
# Tkinter Label: Widget for displaying text or images, customizable text with font options, supports text manipulation like underlining and multiline display.
root = Tk()
root.geometry("1000x1000")
root.minsize(300,200)
root.maxsize(1100,1100)
root.title("Welcome my world")
txt_var = StringVar() # Special variable for widget association.
txt_var.set("Hello Friends")
label = Label(root,
              textvariable=txt_var,
              anchor=CENTER,
              bg="blue",
              height=3,
              width=30,
              bd=3, # boder
              font=("Arial", 16, "bold"),
              cursor="hand2",
              fg="red",#font color
              padx=15,               
              pady=15,
              justify=CENTER,    
              relief=SOLID,               
              wraplength="9999"  # Set a very large value for automatic width adjustment       
                )
# Pack the label into the window             
label.pack(pady=20) # Add some padding to the top
              
root.mainloop()

# anchor=CENTER: This is the default behavior. It centers the text horizontally within the available space and vertically within the line height.
# anchor=NW: Anchor the text to the northwest (top-left) corner of the available space.
# anchor=N: Anchor the text to the top center of the available space.
# anchor=NE: Anchor the text to the northeast (top-right) corner of the available space.
# anchor=W: Anchor the text to the left center of the available space.
# anchor=E: Anchor the text to the right center of the available space.
# anchor=SW: Anchor the text to the southwest (bottom-left) corner of the available space.
# anchor=S: Anchor the text to the bottom center of the available space.
# anchor=SE: Anchor the text to the southeast (bottom-right) corner of the available space.

# Cursor
# arrow: The default cursor, typically an arrow pointer.
# circle: A circle-shaped cursor.
# cross: A crosshair cursor.
# dot: A small dot cursor.
# hand1: A pointing hand cursor, typically used for clickable elements.
# hand2: Another style of pointing hand cursor, often used for hyperlinks or interactive elements.
# watch: A watch or hourglass cursor, indicating that the application is busy or waiting.
# plus: A plus-shaped cursor.
# question_arrow: An arrow cursor with a question mark, indicating help or information.
# xterm: A cursor similar to that used in terminal applications.
# fleur: A fleur (four-pointed flower) cursor.
# pencil: A cursor resembling a pencil, often used for drawing applications.
# no: A "no entry" cursor, indicating that the current action is not allowed.

# justify
# LEFT: Aligns the text to the left edge of the widget.
# RIGHT: Aligns the text to the right edge of the widget.
# CENTER: Centers the text horizontally within the widget.
# JUSTIFY: Justifies the text, meaning it aligns the text to both the left and right edges 

# relief 
# FLAT: This is the default relief style. It means the widget will have no border or relief effect.
# RAISED: This style creates a raised border effect, making the widget appear as if it's raised above the surrounding surface.
# SUNKEN: This style creates a sunken border effect, making the widget appear as if it's pressed into the surrounding surface.
# GROOVE: This style creates a grooved border effect, with a groove carved into the surface around the widget.
# RIDGE: This style creates a ridged border effect, with a ridge protruding out from the surface around the widget.
# SOLID: This style creates a solid border effect, which may be used to emphasize the widget.


