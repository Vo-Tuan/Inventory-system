import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('{}x{}'.format(1280, 720))
root.title('Inventory Managment')
root.config(bg='red')

mainframe = tk.Frame(root,background='#DADBD5')
mainframe.pack(fill=tk.BOTH,expand=True)

topbar = tk.Frame(mainframe,height=60,background='#1B263B')
topbar.pack(fill=tk.X,side=tk.TOP)

sidebar = tk.Frame(mainframe,width=180,background='#415A77')
sidebar.pack(fill=tk.Y,side=tk.LEFT)

scrollbar = tk.Scrollbar(mainframe)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

tree = ttk.Treeview(mainframe,yscrollcommand=scrollbar.set)
tree['columns'] =list(range(3)) 
tree.heading('#0',text='Product')
tree.heading('0',text='Product ID')
tree.heading('1',text='Cost')
tree.heading('2',text='Amount')
tree.pack(fill=tk.BOTH,expand=True,padx=(0,180),side=tk.BOTTOM)
scrollbar.config(command = tree.yview)
ttk.Style().configure("Treeview", background="#E0E1DD", foreground="black")

for x in range(200):
    tree.insert('', 'end', text=f'{x} Example product', values=('value 1','value 2','value 3'))
root.mainloop()
