import tkinter as tk

w1 = tk.Tk()
w1.title("Menu Widget")
w1.geometry("400x200")

# Menu Bar
menu1 = tk.Menu(w1,background = 'lightblue',fg = 'red')

def cmd1():
    w_new = tk.Tk()
    w_new.title("New Page")
    w_new.mainloop()

def cmd2():
    pass

# Different Menu Options
file = tk.Menu(menu1,tearoff = 0)
menu1.add_cascade(label = 'File',menu = file)                   # adding title to first Options, and it to menu
file.add_command(label = 'New Page',command = cmd1)
file.add_command(label = 'Open')
file.add_separator
file.add_command(label = 'Close',command = w1.destroy)

# adding more options
edit = tk.Menu(menu1,tearoff = 0)
menu1.add_cascade(label = 'Edit',menu = edit)
edit.add_command(label = 'Cut',command = cmd2)
edit.add_command(label = 'Paste')

# adding menu to the window
w1.config(menu = menu1)

t1 = tk.StringVar()

# Using OptionMenu
opt1 = tk.OptionMenu(w1,t1,"First","Second","Third","Fourth")
opt1.config(bg = "green",fg = "black")
opt1.grid(pady = 10)

w1.mainloop()