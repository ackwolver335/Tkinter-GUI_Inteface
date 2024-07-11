import tkinter as tk 

# Main Window
w1 = tk.Tk()
w1.title('Binding Method Double Click')
w1.geometry('500x300')

# adding frame for the listbox
frm1 = tk.Frame(w1,width = 200,height = 100)
frm1.pack()

# defining the method for binding function
def bind1(event):
    color_scheme = lbx1.curselection()              # Getting selected values

    # updating label text
    lb1.config(text = lbx1.get(color_scheme))

    # Loop for Color selection
    for data in color_scheme:
        if data == 0:
            w1.config(background = 'red')
        elif data == 1:
            w1.config(background = 'blue')
        elif data == 2:
            w1.config(background = 'lightgreen')
        elif data == 3:
            w1.config(background = 'lightblue')

# Creating a listbox and further selection
lbx1 = tk.Listbox(frm1,height = 4)

# adding elements in Listbox
lbx1.insert(0,'red')
lbx1.insert(1,'blue')
lbx1.insert(2,'lightgreen')
lbx1.insert(3,'lightblue')

# binding it with the method
lbx1.bind('<Double-1>',bind1)
lbx1.pack()

# Adding label here
lb1 = tk.Label(frm1,text = 'Default')
lb1.pack()

w1.mainloop()