import tkinter as tk
from tkinter import ttk as tk1

w1 = tk.Tk()
w1.title('Treeview Scrollbar Widget')
w1.resizable(width = 1,height = 1)

# Creating the Treeview Widget
trw1 = tk1.Treeview(w1,selectmode = 'browse')
trw1.pack(side = 'right')                                                           # packing it at the right side

# Creating a vertical Scrollbar
verscrlbr1 = tk1.Scrollbar(w1,orient = 'vertical',command = trw1.yview)             # Scrollbar and Its Vertical View
verscrlbr1.pack(side = 'right',fill = 'x')                                          # Packing it right side

# Adding configuration to Treeview
trw1.configure(xscrollcommand = verscrlbr1.set)

# Defining Columns
trw1['columns'] = ('1','2','3','4')
trw1['show'] = 'headings'

trw1.column('1',width = 50,anchor = 'c')                                       # Assigning the width and anchor
trw1.column('2',width = 50,anchor = 'se')
trw1.column('3',width = 50,anchor = 'se')
trw1.column('4',width = 40,anchor = 'se')

trw1.heading('1',text = 'Name')                                                     # Defining Columns names
trw1.heading('2',text = 'Shift')
trw1.heading('3',text = 'Section')
trw1.heading('4',text = 'Date')

# Inserting data to the items and their features
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))
trw1.insert('','end',text = 'L1',values = ('First','One','A','23'))

w1.mainloop()