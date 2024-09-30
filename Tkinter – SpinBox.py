# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk 
 
# root  = Tk()
# root.geometry("700x1017")
# root.maxsize(1000,1017)
# root.minsize(400,300)
# root.title("SpinBox")

# def grab():
    
#     value = my_spinbox.get()
#     my_label.config(text = value)
    
#     if  value  == "LUFFY":
        
#         image_path = "https://tse1.mm.bing.net/th?id=OIP.sjoKeM9c0wPbUGm6htL4VAAAAA&pid=Api&P=0&h=180"
#         image = Image.open(image_path)
#         image = image.resize((100, 100), Image.ANTIALIAS)
#         luffy_image = ImageTk.PhotoImage(image)
#         my_label.config(text="LUFFY = [Bounty = 3,000,000,000]", fg="red", bg="white", compound=LEFT, image = luffy_image)
#         my_label.image = luffy_image

# name = ["LUFFY","ZORO","SANJI","BROOK","NAMI","ROBIN","CHOPPER","ZIMBEY","FRENKEY","USOPP"]
# # my_spinbox = Spinbox(root, from_ = 0 , to=1000000 ,increment=10 , font = ("Helvetica",20))
# my_spinbox = Spinbox(root, values=name ,font = ("Helvetica",20))
# my_spinbox.pack(pady=20,padx=20)

# my_btn = Button(root, command=grab,text ="Submit").pack(pady=20,padx=20)

# btn = Button(root, command=root.destroy ,text ="Close").pack(pady=20,padx=20)

# my_label = Label(root,text="")
# my_label.pack(pady=20)

# root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def Luffyimg():
    # Replace this URL with the path to your local image file
        image_path = "./Luffy_image.png"
        image = Image.open(image_path)
        image = image.resize((500, 400), Image.ANTIALIAS)
        luffy_image = ImageTk.PhotoImage(image)
        my_label.config(text="LUFFY = [Bounty = 3,000,000,000]", fg="red", bg="white", compound=LEFT, image=luffy_image)
        my_label.image = luffy_image

def Zoroimg():
    image_path = "./zoroimg.png"
    image = Image.open(image_path)
    image = image.resize((400,400))
    zoro_image = ImageTk.PhotoImage(image)
    my_label.config(text=" ZORO = [Bounty = 1,111,000,000 ", fg="darkgreen", bg="white", compound=LEFT, image=zoro_image)
    my_label.image = zoro_image
    
def Sanjiphoto():
    image_path = "./Sanji-.png"
    image = Image.open(image_path)
    image = image.resize((400,400))
    Sanji_image = ImageTk.PhotoImage(image)
    my_label.config(text=" SANJI = [Bounty = 1,111,000,000", fg="#F6BE00", bg="white", compound=LEFT, image=Sanji_image)
    my_label.image = Sanji_image

def Namiimg():
    image_path = "./Nami-PNG.png"
    image = Image.open(image_path)
    image = image.resize((400,400))
    Nami_image = ImageTk.PhotoImage(image)
    my_label.config(text=" NAMI = [Bounty = 366,000,000", fg="Orange", bg="white", compound=LEFT, image=Nami_image)
    my_label.image = Nami_image
    
def Usoppimg():
    image_path = "./Usopp.png"
    image = Image.open(image_path)
    image = image.resize((400,400))
    Usopp_image = ImageTk.PhotoImage(image)
    my_label.config(text=" USOPP = [Bounty = 500,000,000", fg="brown", bg="white", compound=LEFT, image=Usopp_image)
    my_label.image = Usopp_image

def Chopperimg():
    image_path = "./Chopper.png"
    image = Image.open(image_path)
    image = image.resize((400,400))
    Chopper_image = ImageTk.PhotoImage(image)
    my_label.config(text=" CHOPPER = [Bounty = 1000", fg="#f4c2c2", bg="white", compound=LEFT, image=Chopper_image)
    my_label.image = Chopper_image
    
def Robinimg():
    image_path = "./NikoRobin.png"
    image = Image.open(image_path)
    image = image.resize((400,400))
    Robin_image = ImageTk.PhotoImage(image)
    my_label.config(text=" NICO ROBIN = [Bounty = 930,000,000 ", fg="purple", bg="white", compound=LEFT, image=Robin_image)
    my_label.image = Robin_image

def Frankyimg():
    image_path = "./Frankyl.png"
    image = Image.open(image_path)
    image = image.resize((400,400))
    Franky_image = ImageTk.PhotoImage(image)
    my_label.config(text=" FRANKY = [Bounty = 394,000,000", fg="darkblue", bg="white", compound=LEFT, image=Franky_image)
    my_label.image = Franky_image

def Brookimg():
    image_path = "./Brook.png"
    image = Image.open(image_path)
    image = image.resize((400,400))
    Brook_image = ImageTk.PhotoImage(image)
    my_label.config(text=" BROOK = [Bounty = 383,000,000]", fg="black", bg="white", compound=LEFT, image=Brook_image)
    my_label.image = Brook_image
    
def Jinbeimg():
    image_path = "./Jinbei.png"
    image = Image.open(image_path)
    image = image.resize((400,400))
    Jinbe_image = ImageTk.PhotoImage(image)
    my_label.config(text=" JINBE = [Bounty = 1,100,000,000", fg="blue", bg="white", compound=LEFT, image=Jinbe_image)
    my_label.image = Jinbe_image

root = Tk()
root.geometry("700x1017")
root.maxsize(1000, 1017)
root.minsize(400, 300)
root.title("SpinBox")

def grab():
    value = my_spinbox.get()
    my_label.config(text=value)
    
    if value == "LUFFY":
        Luffyimg()
    elif value == "ZORO":
        Zoroimg()
    elif value == "SANJI":
        Sanjiphoto() 
    elif value == "NAMI":
        Namiimg()
    elif value == "BROOK":
        Brookimg()
    elif value == "JINBE":
        Jinbeimg()
    elif value == "ROBIN":
        Robinimg()
    elif value == "USOPP":
        Usoppimg()
    elif value == "CHOPPER":
        Chopperimg()
    else:
        Frankyimg()

frame = Frame(root, bg="white")  # Change "lightblue" to any color you prefer
frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(frame)  # Change "white" to any color you prefer
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview, bg="grey")  # Change "grey" to any color you prefer
scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

cframe = Frame(my_canvas,bg="lightblue")

image_path = "./strewhat.png"
image = Image.open(image_path)
image = image.resize((700, 700), Image.ANTIALIAS)  # Resize the image
Crew_image = ImageTk.PhotoImage(image)

my_label1 = Label(cframe, bg="white", image=Crew_image)
my_label1.image = Crew_image  # Keep a reference to avoid garbage collection
my_label1.pack(pady=20)
       
name = ["LUFFY", "ZORO", "NAMI", "USOPP", "SANJI","CHOPPER", "ROBIN", "FRENKEY", "BROOK" , "JINBE"]
my_spinbox = Spinbox(cframe, values=name, font=("Helvetica", 20))
my_spinbox.pack(pady=20, padx=20)

my_btn = Button(cframe, command=grab, text="Submit")
my_btn.pack(pady=20, padx=20)

btn = Button(cframe, command=root.destroy, text="Close")
btn.pack(pady=20, padx=20)

my_label = Label(cframe, text="")
my_label.pack(pady=20)

root.mainloop()