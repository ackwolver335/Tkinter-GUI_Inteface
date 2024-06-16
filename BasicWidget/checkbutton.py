import tkinter as tk
import tkinter.ttk as tk1

w1 = tk.Tk()
w1.title("Checkbutton Widget")
w1.geometry("400x400")

def cb_command():
    if var1.get() == 1:
        print("Checkbutton is ON !")
    else:
        print("Checkbutton is OFF !")

# Creating a Checkbutton
# On Button Toggle Method
var1 = tk.IntVar()
cb1 = tk.Checkbutton(w1,text = "Check1",variable = var1,onvalue = 1,offvalue = 0,command = cb_command)

# adding configuration
cb1.config(bg = "lightblue",fg = "Green",font = ('Fira Code',12),selectcolor = "yellow",relief = 'raised',padx = 5,pady = 5)

# adding bitmap for checkbutton
cb1.config(bitmap = "info",width = 30,height = 5)
cb1.pack(padx = 10,pady = 10)
cb1.flash()                                                     # Calling Methods

# Working with Multiple Checkbutton
cbt1 = tk.IntVar()
cbt2 = tk.IntVar()
cbt3 = tk.IntVar()

# Formatting with Frames
frame1 = tk.Frame(w1,bd = 3,relief = 'groove',width = 300,height = 30)
frame1.pack(padx = 10,pady = 10)

# adding a label heading to the frames
label1 = tk.Label(frame1,text = "Tkinter Checkbutton Widgets",bd = 2,relief = 'groove',font = ('Fira Code',8))
label1.pack(padx = 2,pady = 2)

# Adding Checkbuttons to the Frames
cbtn1 = tk.Checkbutton(frame1,text = "Checkbutton1",variable = cbt1,onvalue = 1,offvalue = 0)
cbtn2 = tk.Checkbutton(frame1,text = "Checkbutton2",variable = cbt2,onvalue = 1,offvalue = 0)
cbtn3 = tk.Checkbutton(frame1,text = "Checkbutton3",variable = cbt3,onvalue = 1,offvalue = 0)

# Packing the Buttons to the window
cbtn1.pack()
cbtn2.pack()
cbtn3.pack()

# Creating another frame for ttk module checkbutton widgets
frame2 = tk.Frame(w1,bd = 3,relief = 'raised',width = 300,height = 30)
frame2.pack(padx = 3,pady = 4)

# adding label to the frame
label2 = tk.Label(frame2,text = "Programming Languages",bd = 3,relief = 'raised',font = ('Fira Code',8,'italic'))
label2.pack(padx = 4,pady = 5)

# adding checkbuttons to the Second Frame for ttk Checkbuttons
ckbtn1 = tk1.Checkbutton(frame2,text = "JAVA",takefocus = 1)
ckbtn2 = tk1.Checkbutton(frame2,text = "Python",takefocus = 1)
ckbtn3 = tk1.Checkbutton(frame2,text = "C++",takefocus = 1)

# packing them using pack() method
ckbtn1.pack(padx = 2,pady = 2)
ckbtn2.pack(padx = 2,pady = 2)
ckbtn3.pack(padx = 2,pady = 2)

# changing checkbutton text dynamically
t1 = tk.StringVar()
t2 = tk.StringVar()

# setting the values
t1.set('OFF')
t2.set('OFF')

# adding checkbuttons
chkb1 = tk1.Checkbutton(w1,textvariable = t1,variable = t1,offvalue = "Turned OFF",onvalue = "Turned ON")
chkb2 = tk1.Checkbutton(w1,textvariable = t2,variable = t2,offvalue = "Checked OFF",onvalue = "Checked ON")

chkb1.pack(side = 'top',pady = 10)
chkb2.pack(side = 'top',pady = 10)

w1.mainloop()