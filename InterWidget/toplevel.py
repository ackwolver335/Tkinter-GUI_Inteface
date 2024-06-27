import tkinter as tk 

w1 = tk.Tk()
w1.title("Toplevel Widgets")
w1.geometry('500x300')

l1 = tk.Label(w1,text = 'Main Window')
l1.pack(padx = 2,pady = 3)

def command1():
    top2 = tk.Toplevel(w1)
    top2.title('Third Window')
    top2.geometry('500x200')

    btn2 = tk.Button(top2,text = "Exit",command = top2.destroy)
    btn2.pack(padx = 2,pady = 3)

    top2.mainloop()

btn1 = tk.Button(w1,text = 'Third Window',command = command1)
btn1.pack(padx = 2,pady = 3)

top1 = tk.Toplevel(w1)
top1.title("Second Window")
top1.geometry('300x200')

l2 = tk.Label(top1,text = 'Second Window Label')
l2.pack(padx = 2,pady = 3)

top1.mainloop()

w1.mainloop()