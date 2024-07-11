import tkinter as tk 

w1 = tk.Tk()
w1.title('Binding Right Click Method')
w1.geometry('500x200')

# adding a frame here
frm1 = tk.Frame(w1)
frm1.pack()

# Creating a label for it
lb1 = tk.Label(frm1,text = 'Right Click to get the Menu',width = 50,height = 10)
lb1.pack() 

# adding menu here
m1 = tk.Menu(frm1,tearoff = 0)
m1.add_command(label = 'Cut')
m1.add_command(label = 'Copy')
m1.add_command(label = 'Paste')
m1.add_separator()
m1.add_command(label = 'Exit',command = w1.destroy)

# adding a binding method for opening the menu
def open(event):
    try:
        m1.tk_popup(event.x_root,event.y_root)
    finally:
        w1.grab_release()

# binding it with the label
lb1.bind('<Button-3>',open)

w1.mainloop()