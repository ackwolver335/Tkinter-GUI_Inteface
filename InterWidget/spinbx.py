import tkinter as tk

w1 = tk.Tk()
w1.title('SpinBox Widget')
w1.geometry('500x300')

def cmd1():                                             # Method for SpinBox
    value = spn1.get()
    print('Value Changed to : ' + str(value))

# adding frame for spinbox
spn1 = tk.Spinbox(w1,from_ = 0 ,to = 100,width = 10,relief = 'sunken',repeatdelay = 400,repeatinterval = 100,font = ('Fira Code',12),bg = 'lightblue',fg = 'White',command = cmd1)

# adding configuration
spn1.config(state = 'normal',bd = 3,justify = 'center',wrap = True)
spn1.pack()

def cmd2():                                             # Use of Delete Method in Spinbox
    spn1.delete(0)

btn1 = tk.Button(w1,text = 'Delete',command = cmd2)     # Button for deleting Values in Spinbox
btn1.pack(padx = 2,pady = 4)

def cmd3():                                      
    spn1.insert(0,'12')                                 # insert() method for inserting data values

btn2 = tk.Button(w1,text = 'Add Data',command = cmd3)   # Button for inserting data values
btn2.pack(padx = 2,pady = 3)

def cmd4():
    val1 = spn1.identify(0,3)                           # identify to check its range identification
    print(val1)

btn3 = tk.Button(w1,text = 'Check',command = cmd4)      # Button for using identify method
btn3.pack(padx = 2,pady = 3)

def cmd5():
    data1 = spn1.index(2)                                       # index() method to get the value at specified index
    print(data1)

btn4 = tk.Button(w1,text = 'Check Index',command = cmd5)        # Button for using index() method
btn4.pack(padx = 2,pady = 4)

w1.mainloop()