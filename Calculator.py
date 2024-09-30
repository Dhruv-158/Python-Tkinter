
from tkinter import *
from tkinter import font
import math

def button_Click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_Clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global Math
    Math = "addition"
    f_num = float(first_number)
    e.delete(0, END)
    
def button_subtract():
    first_number = e.get()
    global f_num
    global Math
    Math = "Subtraction"
    f_num = float(first_number)
    e.delete(0, END)
    
def button_multiply():
    first_number = e.get()
    global f_num
    global Math
    Math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global Math
    Math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_Squre():
    first_number = e.get()
    global Math
    Math = "squre"
    global f_num
    f_num = float(first_number)
    e.delete(0,END)

def button_SQRT():
    first_number = e.get()
    global Math
    Math = "SQRT"
    global f_num
    f_num = float(first_number)
    e.delete(0,END)
    
def button_Per():
    first_number = e.get()
    global Math
    Math = "PERCENTAGE"
    global f_num
    f_num = float(first_number)
    e.delete(0,END)
    
def button_plus_minus():
    try:
        current_number = float(e.get())
        e.delete(0, END)
        e.insert(0, str(-current_number))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    global Math
    if Math == "addition":
        e.insert(0, f_num + float(second_number))
    elif Math == "Subtraction" :
        e.insert(0, f_num - float(second_number))
    elif Math == "multiplication" :
        e.insert(0, f_num * float(second_number))
    elif Math == "division" :
        e.insert(0, f_num / float(second_number))
    elif Math == "squre":
        e.insert(0,math.pow(f_num,2))
    elif Math == "SQRT":
        e.insert(0,math.sqrt(f_num))
    elif Math == "PERCENTAGE":
        e.insert(0,(f_num / float(second_number)) * 100)
    else:
        e.insert("Some thing wrong")

root = Tk()
root.title("Calculator")


e = Entry(root,width = 50,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

button_1 = Button(root,text=1,padx=40,pady=20,command=lambda: button_Click("1"),borderwidth=10)
button_2 = Button(root,text=2,padx=40,pady=20,command=lambda: button_Click("2"),borderwidth=10)
button_3 = Button(root,text=3,padx=40,pady=20,command=lambda: button_Click("3"),borderwidth=10)
button_Sub = Button(root,text="-",padx=39,pady=20,command=button_subtract,borderwidth=10)


button_4 = Button(root,text=4,padx=40,pady=20,command=lambda: button_Click("4"),borderwidth=10)
button_5 = Button(root,text=5,padx=40,pady=20,command=lambda: button_Click("5"),borderwidth=10)
button_6 = Button(root,text=6,padx=40,pady=20,command=lambda: button_Click("6"),borderwidth=10)
button_Multi = Button(root,text="x",padx=39,pady=20,command=button_multiply,borderwidth=10)


button_7 = Button(root,text=7,padx=40,pady=20,command=lambda: button_Click("7"),borderwidth=10)
button_8 = Button(root,text=8,padx=40,pady=20,command=lambda: button_Click("8"),borderwidth=10)
button_9 = Button(root,text=9,padx=40,pady=20,command=lambda: button_Click("9"),borderwidth=10)
button_Div = Button(root,text="÷",padx=39,pady=20,command=button_divide,borderwidth=10)

button_0 = Button(root,text=0,padx=40,pady=20,command=lambda: button_Click("0"),borderwidth=10)
button_Equal = Button(root,text="=",padx=91,pady=20,command=button_equal,borderwidth=10)
button_Add = Button(root,text="+",padx=39,pady=20,command=button_add,borderwidth=10)

button_clear = Button(root,text="Clear",padx=84,pady=20,command=button_Clear,borderwidth=10)
button_plus_mines =  Button(root, text="±", padx=40, pady=20, command=button_plus_minus, borderwidth=10)
button_CLOSE =  Button(root,text="CLOSE",padx=30,pady=20,command=root.destroy ,borderwidth=10)

button_power =  Button(root,text="X²",padx=40,pady=20,command=button_Squre,borderwidth=10)
button_sqrt =  Button(root,text="√",padx=40,pady=20,command=button_SQRT,borderwidth=10)
button_Percentage =  Button(root,text="%",padx=40,pady=20,command=button_Per,borderwidth=10)
button_dot = Button(root,text=".",padx=40,pady=20,command=lambda: button_Click("."),borderwidth=10)

button_Div.grid(row=2 ,column =3)
button_9.grid(row =2 , column =2)
button_8.grid(row =2 , column =1)
button_7.grid(row =2 , column =0)

button_Multi.grid(row =3,column=3)
button_6.grid(row =3 , column =2)
button_5.grid(row =3 , column =1)
button_4.grid(row =3, column  =0)

button_Sub.grid(row=4, column= 3)
button_3.grid(row =4, column = 2)
button_2.grid(row =4, column = 1)
button_1.grid(row =4, column = 0)

button_0.grid(row = 5, column = 0)
button_Equal.grid(row = 5 ,column = 1,columnspan=2)
button_Add.grid(row = 5,column = 3)

button_plus_mines.grid(row = 6,column = 0)
button_clear.grid(row = 6 ,column = 1,columnspan=2)
button_CLOSE.grid(row = 6 ,column = 3)

button_dot.grid(row = 1 ,column = 3)
button_power.grid(row = 1 ,column = 1)
button_sqrt.grid(row = 1, column = 2)
button_Percentage.grid(row = 1, column = 0)

root.mainloop()
