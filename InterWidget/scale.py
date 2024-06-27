import tkinter as tk 

w1 = tk.Tk()
w1.title("Scale Widget")
w1.geometry('400x300')

frm1 = tk.Frame(w1,bd = 2,relief = 'groove')                # frame established
frm1.pack(padx = 2,pady = 3)                                # frame packed

var1 = tk.DoubleVar()                                       # Variable for getting scale's value

# Implementing the Scale
scl1 = tk.Scale(frm1,variable = var1,from_ = 1,to = 100,orient = tk.HORIZONTAL)
scl1.pack(padx = 2,pady = 3)

lb1 = tk.Label(frm1,text = 'Horizontal Scale',font = ('Fira Code',12))
lb1.pack(padx = 2,pady = 3)

def showval():
    set1 = "Horizontal Scale Value : " + str(var1.get())
    lb2.config(text = set1,font = ('Fira Code',8))

lb2 = tk.Label(frm1)
lb2.pack(padx = 2,pady = 3)

btn1 = tk.Button(frm1,text = 'Display Value',command = showval,bg = 'Blue')
btn1.pack(padx = 2,pady = 3)

# Implementing the Scale in Vertical Format
frm2 = tk.Frame(w1,bd = 3,relief = 'raised')
frm2.pack(padx = 2,pady = 3)

var2 = tk.DoubleVar()                                                                   # variable for frame's value

scl2 = tk.Scale(frm2,variable = var2,from_ = 50,to = 1,orient = tk.VERTICAL)            # Scale Established
scl2.pack(padx = 2,pady = 3)

lb3 = tk.Label(frm2,text = 'Vertical Scale',font = ('Fira Code',12))
lb3.pack(padx = 2,pady = 3)

def showval1():
    set2 = "Vertical Scale Value : " + str(var2.get())
    lb4.config(text = set2,font = ('Fira Code',9))

lb4 = tk.Label(frm2)
lb4.pack(padx = 2,pady = 3)

btn2 = tk.Button(frm2,text = 'Display Value',command = showval1,bg = 'Purple')
btn2.pack(padx = 2,pady = 3)

w1.mainloop()