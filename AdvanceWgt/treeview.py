import tkinter as tk
import tkinter.ttk as tk1

w1 = tk.Tk()
w1.title('Treeview Widget')
w1.geometry('500x300')

frm1 = tk.Frame(w1,bd = 2,relief = 'groove')
frm1.pack(padx = 2,pady = 3)

lb1 = tk1.Label(w1,text = 'Treeview Widget',font = ('Fira Code',12))
lb1.pack(padx = 2,pady = 3)

treevw1 = tk1.Treeview(frm1)
treevw1.pack(padx = 2,pady = 3)

# Inserting items to the Treeview
treevw1.insert('',0,'item1',text = 'Coding Needs')
treevw1.insert('',1,'item2',text = 'Computer Science')
treevw1.insert('',2,'item3',text = 'GATE Papers')
treevw1.insert('',3,'item4',text = 'Programming Languages')

# Inserting more than one attributes of a particular items
treevw1.insert('item2','end','Algorithm1',text = 'Algorithm1')
treevw1.insert('item2','end','Algorithm2',text = 'Algorithm2')
treevw1.insert('item3','end','Algorithm3',text = 'Algorithm3')
treevw1.insert('item3','end','Algorithm4',text = 'Algorithm4')
treevw1.insert('item4','end','Algorithm5',text = 'Algorithm5')
treevw1.insert('item4','end','Algorithm6',text = 'Algorithm6')

# Placing items at the right place
treevw1.move('item2','item1',0)
treevw1.move('item3','item1',0)
treevw1.move('item4','item1',0)

w1.mainloop()