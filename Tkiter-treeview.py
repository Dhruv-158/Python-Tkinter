from tkinter import*
from tkinter import ttk

app = Tk()
app.geometry("1000x1017")
app.minsize(600,700)
app.maxsize(1100,1017)
app.title("treeview")

treeview = ttk.Treeview(app)
treeview.pack()

treeview.insert('','0',"item1",text="GeekforGeeks")
treeview.insert('','1','item2',text="Computer Science")
treeview.insert('','2','item3',text="Gate Pepar")
treeview.insert('','end','item4',text="progrsming Language")

treeview.insert('item2','1',"Algorithm",text="Algorithm")
treeview.insert('item2','2',"Data structure",text="Structure")
treeview.insert("item3",'1',"2022 Paper",text="2022 Paper")
treeview.insert('item3','2',"2023 Paper",text="2023 Paper")
treeview.insert('item4','1',"Python",text="Python")
treeview.insert('item4','2','Java',text="Java")

treeview.move('item2','item1','end')
treeview.move('item3','item1','end')
treeview.move('item4','item1','end')



app.mainloop()

