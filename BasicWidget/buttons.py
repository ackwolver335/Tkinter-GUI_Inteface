import tkinter as tk
from tkinter.ttk import *

# Window
window = tk.Tk()
window.title("Buttons")
window.geometry("500x400")

# Button with normal text
btn1 = tk.Button(window,text = "Simple Button")
btn1.pack()

# Button with active interfaces
btn2 = tk.Button(window,text = "Active Changes",activebackground = "#000000",activeforeground = "#ffffff")
btn2.pack()

# Replacing using anchor
btn3 = tk.Button(window,text = "Positioned Button",anchor = "nw")
btn3.pack(padx = 1,pady = 1)

# Adding Border to it
btn4 = tk.Button(window,text = "Border Button",bd = 3,borderwidth = 5,relief = "groove")
btn4.pack(padx = 2,pady = 2)

# Different Hightlight Options
btn5 = tk.Button(window,text = "Highlighted Button",highlightbackground = "green",highlightcolor = "red",highlightthickness = 3)
btn5.pack()

# Setting up the height,width and Padding
btn6 = tk.Button(window,text = "Spaced Button",height = 2,width = 10,padx = 3,pady = 5)
btn6.pack()

# Special command to close the window
btn7 = tk.Button(window,text = "Close",command = window.destroy)
btn7.pack()

# Justification and Wrapping Length
btn8 = tk.Button(window,text = "Button8",justify = "left",wraplength = 100)
btn8.pack()

def display1():
    print("First Display method here !")

def display2():
    print("Second Display method here !")

# Binding multiple commands in a single Button
btn9 = tk.Button(window,text = "Multiple Binded",command = lambda : [display1(),display2()])
btn9.pack()

# Open new window from one Window
def method1():
    w1 = tk.Tk()
    w1.title("New Window")
    w1.geometry("500x300")

btn10 = tk.Button(window,text = "Open New Window",command = method1)
btn10.pack()

# Border to the Button
btn12 = tk.Button(window,text = "Bordered Button",border = 4,borderwidth = 3,relief = 'raised')
btn12.pack() 

# Ending the Window
window.mainloop()