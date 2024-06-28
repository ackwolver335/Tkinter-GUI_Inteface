import tkinter as tk 

w1 = tk.Tk()
w1.title('MenuButton Widget')
w1.geometry('500x300')

# MenuButton Widget
menu1 = tk.Menubutton(w1,text = 'Menu')
menu1.menu = tk.Menu(menu1)
menu1['menu'] = menu1.menu

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

menu1.menu.add_checkbutton(label = 'Courses',variable = var1)               # First option
menu1.menu.add_checkbutton(label = 'Second Opt',variable = var2)            # Second option
menu1.menu.add_checkbutton(label = 'Third Opt',variable = var3)             # Third option

menu1.pack(padx = 2,pady = 3)                                               # Menu Button packed

w1.mainloop()