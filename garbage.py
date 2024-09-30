from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import random

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Tkinter.com - Magic 8-Ball!')
# root.iconbitmap('c:/tkinter.com/codemy.ico')
root.geometry("500x500")

# Shake The 8-Ball Function
def shake():
	answers = {
		"It is certain": "green",
		"It is decidedly so": "green",
		"Without a doubt":"green",
		"Yes definitely":"green",
		"You may rely on it":"green",
		"As I see it, yes":"green",
		"Most likely":"green",
		"Outlook good":"green",
		"Yes":"green",
		"Signs point to yes":"green",

		"Reply hazy, try again":"yellow",
		"Ask again later":"yellow",
		"Better not tell you now":"yellow",
		"Cannot predict now":"yellow",
		"Concentrate and ask again":"yellow",

		"Don't count on it!":"red",
		"My reply is no!":"red",
		"My sources say no!":"red",
		"Outlook not so good!":"red",
		"Very doubtful!":"red"}
	# Convert dictionary to list
	answer_list = list(answers.items())
	# shuffle the list
	random.shuffle(answer_list)
	#print(answer_list)
	# Output to the screen
	results.config(text = from tkinter import *
from bs4 import BeautifulSoup
import urllib
from urllib import request
from datetime import datetime

root = Tk()
root.title('Codemy.com - Bitcoin Price Grabber')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("550x210")
root.config(bg="black")

global previous
previous = False

# Get Current Time
now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")


# Create a Frame
my_frame = Frame(root, bg="black")
my_frame.pack(pady=20)

# Define logo image
logo = PhotoImage(file='images/bitcoin.png')
logo_label = Label(my_frame, image=logo, bd=0)
logo_label.grid(row=0, column=0, rowspan=2)

# Add bitcoin price label
bit_label = Label(my_frame, text='TEST', 
	font=("Helvetica", 45),
	bg="black",
	fg="green",
	bd=0)
bit_label.grid(row=0, column=1, padx=20, sticky="s")

# Latest Price Up/Down
latest_price = Label(my_frame, text="move test",
	font=("Helvetica", 8),
	bg="black",
	fg="grey")
latest_price.grid(row=1, column=1, sticky="n" )

#Grab the bitcoin price
def Update():
	global previous

	# Grab Bitcoin Price
	page = urllib.request.urlopen("https://www.coindesk.com/price/bitcoin").read()
	html = BeautifulSoup(page, "html.parser")
	price_large = html.find(class_="price-large")
	
	# convert to string so we can slice
	price_large1 = str(price_large)
	# Grab a slice that contains the price
	price_large2 = price_large1[54:63]

	# Update our bitcoin label
	bit_label.config(text=f'${price_large2}')
	# Set timer to 30 seconds
	# 1 second = 1000
	root.after(30000, Update)

	# Get Current Time
	now = datetime.now()
	current_time = now.strftime("%I:%M:%S %p")

	# Update the status bar
	status_bar.config(text=f'Last Updated: {current_time}   ')

	# Determine Price Change
	# grab current Price
	current = price_large2

	# remove the comma
	current = current.replace(',', '')

	if previous:
		if float(previous) > float(current):
			latest_price.config(
				text=f'Price Down {round(float(previous)-float(current), 2)}', fg="red")

		elif float(previous) == float(current):
			latest_price.config(text="Price Unchanged", fg="grey")	

		else:
			latest_price.config(
				text=f'Price Up {round(float(current)-float(previous), 2)}', fg="green")			


	else:
		previous = current
		latest_price.config(text="Price Unchanged", fg="grey")

# Create status bar
status_bar = Label(root, text=f'Last Updated {current_time}   ',
	bd=0,
	anchor=E,
	bg="black",
	fg="grey")

status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# On program start, run update function
Update()
root.mainloop()[0][0], fg=answer_list[0][1])



# Define Our Images
ball = ImageTk.PhotoImage(Image.open("./Images/play50.png"))
ball_img = Label(root, image=ball, bd=0)
ball_img.pack(pady=35)

# Set Results
results = Label(root, text="", font=("Helvetica", 28), bg="#1a1a1a")
results.pack(pady=20)

# Define Our Button
my_button = customtkinter.CTkButton(master=root, text="Shake 8-Ball", width=190, height=40, compound="top", command=shake)
my_button.pack(pady=30)

root.mainloop()