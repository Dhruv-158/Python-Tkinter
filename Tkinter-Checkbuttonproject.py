from tkinter import *
from tkinter import messagebox

def show_value():
    value = var.get()
    when count is 1 and value is 0 that time show alert 
    
    if value == "":
        messagebox.showwarning("Alert", "Please select an option!")
    else:
        print("Checkbutton value:", value)
        Label(root, text=var.get()).pack()

def create_checkbuttons():
    checkbutton_info = [
        ("Check if she loves you 💏", "Yes, she's in love 💖", "No, she's not in love 💔"),
        ("Check 💋 for a kiss", "Blown a kiss 😘", "Yearning for affection 💔"),
        ("Tap 💖 to flirt", "Flirting mode activated 😉", "Feeling ignored 😔"),
        ("Select 💌 for a love letter", "Heartfelt words written 💕", "Longing for romance 💔"),
        ("Swipe 📱 for a date", "Exciting plans ahead 🥂", "Waiting for a connection 💔"),
        ("Click 🍷 for a romantic evening", "Candlelit dinner planned 🕯️", "Craving intimacy 💔"),
        ("Toggle 💞 for affection", "Feeling loved and cherished 💖", "Seeking attention 💔"),
        ("Press 🥰 to express love", "Overflowing with affection 😍", "Feeling lonely 💔"),
        ("Select 🌹 for a romantic gesture", "Sweet surprise planned 🎁", "Craving romance 💔"),
        ("Swipe 👫 for companionship", "Together forever ❤️", "Yearning for a partner 💔"),
        ("Click 😏 for a flirty wink", "Sending a playful wink 😉", "Desiring attention 💔")
    ]

    for i, (text, onvalue, offvalue) in enumerate(checkbutton_info):
        check_box = Checkbutton(frame, text=text, variable=var, onvalue=onvalue, offvalue=offvalue)
        check_box.grid(row=i, column=0, sticky=W)
        check_box.deselect()

root = Tk()
root.geometry("400x500")
root.title("Check box")
root.minsize(300, 400)
root.maxsize(500, 600)

frame = LabelFrame(root, text="frame", relief="solid", height=100, width=200)
frame.pack(padx=20, pady=20, anchor="center")

var = StringVar()
create_checkbuttons()

btn = Button(frame, text="close", command=root.destroy)
btn.grid(row=11, column=0, columnspan=2, pady=(10, 0))

show_value_button = Button(frame, text="Show Value", command=show_value)
show_value_button.grid(row=12, column=0, columnspan=2, pady=(10, 0))

root.mainloop()
