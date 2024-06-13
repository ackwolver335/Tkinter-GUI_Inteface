from logging import disable
import tkinter as tk
from tkinter import DISABLED, StringVar, messagebox

w1 = tk.Tk()
w1.title("Entry Widget")
w1.geometry('500x300')
w1.resizable(False,False)

l1 = tk.Label(w1,text = "Username",padx = 2,pady = 2,font = ('Fira Code',10))
l1.grid(row = 0,column = 0)

e1 = tk.Entry(w1,font = ('Fira Code',10))                                           # Basic Entry
e1.grid(row = 0,column = 1,padx = 2,pady = 2)

def command1():
    print(e1.get())     # get() method
    w1.destroy()

btn1 = tk.Button(w1,text = "Submit",font = ('Fira Code',10),command = command1)
btn1.grid(row = 1,column = 0)

# Canvas
c1 = tk.Canvas(w1,width = 250,height = 150)
c1.pack()

l2 = tk.Label(w1,text = "Enter your good name")
c1.create_window(100,110,window = l2)

l3 = tk.Label(w1,text = "Enter your owned email")
c1.create_window(100,150,window = l3)

e2 = tk.Entry(w1)
c1.create_window(200,110,window = e2)

e3 = tk.Entry(w1)
c1.create_window(200,150,window = e3)

def command2():
    messagebox.showinfo("Submitted","Your data is been submitted successfully !")
    e2.delete(0)
    e3.delete(0)

btn2 = tk.Button(w1,text = "Submit Data")
c1.create_window(150,200,window = btn2)

l4 = tk.Label(w1,text = "Default Text")
l4.pack()

e4 = tk.Entry(w1,justify = "center")
e4.insert(0,"Default Value")                # insert() method
e4.pack()

text1 = StringVar()
text1.set("Disabled Value")
e5 = tk.Entry(w1,textvariable = text1,state = DISABLED,justify = "center")                  # Disabled Entry
e5.pack()

w1.mainloop()