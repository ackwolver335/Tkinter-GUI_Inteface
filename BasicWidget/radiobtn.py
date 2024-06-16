import tkinter as tk
import tkinter.ttk as tk1

w1 = tk.Tk()
w1.title("RadioButton Widget")
w1.geometry("500x300")

# a general radiobutton
str1 = tk.StringVar(w1,'1')

# Creating a frame for RadioButtons
frame1 = tk.Frame(w1,bd = 3,relief = 'ridge',height = 10,width = 300,bg = "lightblue")
frame1.pack(padx = 2,pady = 3)

# creating label for frame
lb1 = tk.Label(frame1,text = "Ttk Module Radio Buttons",font = ('Fira Code',10,'italic'),bd = 3,relief = 'sunken')
lb1.pack(padx = 3,pady = 5)

# adding radiobuttons
rd1 = tk1.Radiobutton(frame1,text = "Radio Button1",variable = str1,value = "1")
rd2 = tk1.Radiobutton(frame1,text = "Radio Button2",variable = str1,value = "2")
rd3 = tk1.Radiobutton(frame1,text = "Radio Button3",variable = str1,value = "3")

# packing radio buttons
rd1.pack(padx = 2,pady = 3,ipady = 5)
rd2.pack(padx = 2,pady = 3,ipady = 5)
rd3.pack(padx = 2,pady = 3,ipady = 5)

# Creating another frame for Tkinter Radio Buttons
str2 = tk.StringVar(w1,'A')

frame2 = tk.Frame(w1,bd = 3,relief = 'groove',height = 10,width = 300,bg = "lightgreen")
frame2.pack(padx = 2,pady = 3)

# creating label for frame
lb2 = tk.Label(frame2,text = "Tk Module Radio Buttons",font = ('Fira Code',10,'italic'),bd = 3,relief = 'groove')
lb2.pack(padx = 3,pady = 5)

# adding radiobuttons from tkinter modules
radio1 = tk.Radiobutton(frame2,text = "Radio Button1",variable = str2,value = 'A')
radio2 = tk.Radiobutton(frame2,text = "Radio Button2",variable = str2,value = 'B')
radio3 = tk.Radiobutton(frame2,text = "Radio Button3",variable = str2,value = 'C')

# packing radio buttons for tkinter Module
radio1.pack(padx = 2,pady = 3,ipady = 3)
radio2.pack(padx = 2,pady = 3,ipady = 3)
radio3.pack(padx = 2,pady = 3,ipady = 3)

w1.mainloop()