import tkinter as tk
import tkinter.ttk as tk1
from tkinter import scrolledtext as st

w1 = tk.Tk()
w1.title('ScrolledText Widget')
w1.geometry('500x300')

# Creating frame for first Scrolledtext
frm1 = tk.Frame(w1,bd = 3,relief = 'groove')
frm1.pack(padx = 2,pady = 3)

# Label in the Window
lb1 = tk1.Label(frm1,text = 'ScrolledText Widget',font = ('Fira Code',12),background = 'red')
lb1.pack(padx = 2,pady = 3)

# Scrolledtext Area Widget
scrolled1 = st.ScrolledText(frm1,wrap = tk.WORD,width = 40,height = 5,font = ('Fira Code',12))
scrolled1.pack(padx = 2,pady = 3)
scrolled1.focus()

# Creating frame for second Scrolledtext
frm2 = tk.Frame(w1,bd = 3,relief = 'raised')
frm2.pack(padx = 2,pady = 3)

# Another Label in the Window
lb2 = tk1.Label(frm2,text = 'Alternate Widget',font = ('Fira Code',12),background = 'blue')
lb2.pack(padx = 2,pady = 3)

# Scrolledtext Area Widget
scrolled2 = st.ScrolledText(frm2,wrap = tk.WORD,width = 40,height = 5,font = ('Fira Code',12))
scrolled2.pack(padx = 2,pady = 3)

scrolled2.insert(tk.INSERT,"This is the default data added to it !")
scrolled2.configure(state = 'disabled')

w1.mainloop()