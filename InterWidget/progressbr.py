import tkinter as tk
import tkinter.ttk as tk1
import time as t

w1 = tk.Tk()
w1.title('Progress Bar Widget')
w1.geometry('500x300')

frm1 = tk.Frame(w1)                                     # frame for first Progress Bar
frm1.pack()

# progressbar
pgrs1 = tk1.Progressbar(frm1,orient = tk.HORIZONTAL,length = 100,mode = 'determinate')
pgrs1.pack(padx = 10,pady = 10)

def cmd1():                             # method for running progress bar
    pgrs1['value'] = 20                 # for filling first 20% of Progress Bar
    frm1.update_idletasks()
    t.sleep(1)

    pgrs1['value'] = 40                 # for 40%
    frm1.update_idletasks()
    t.sleep(1)

    pgrs1['value'] = 60                 # for 60%
    frm1.update_idletasks()
    t.sleep(1)

    pgrs1['value'] = 80                 # for 80%
    frm1.update_idletasks()
    t.sleep(1)

    pgrs1['value'] = 100                # for 100%
    frm1.update_idletasks()
    t.sleep(1)

# Button for initiating Progress Bar
btn1 = tk.Button(frm1,text = "Start",command = cmd1)
btn1.pack()

frm2 = tk.Frame(w1)                     # Frame for another progres bar
frm2.pack()

# Another Varient
pgrs2 = tk1.Progressbar(frm2,orient = tk.HORIZONTAL,length = 100,mode = 'indeterminate')
pgrs2.pack(padx = 5,pady = 10)

def cmd2():
    pgrs2['value'] = 20
    frm2.update_idletasks()
    t.sleep(1)

    pgrs2['value'] = 40
    frm2.update_idletasks()
    t.sleep(1)

    pgrs2['value'] = 60
    frm2.update_idletasks()
    t.sleep(1)

    pgrs2['value'] = 80
    frm2.update_idletasks()
    t.sleep(1)

    pgrs2['value'] = 100
    frm2.update_idletasks()
    t.sleep(1)

btn2 = tk.Button(frm2,text = 'Start',command = cmd2)
btn2.pack(padx = 4,pady = 5)

w1.mainloop()