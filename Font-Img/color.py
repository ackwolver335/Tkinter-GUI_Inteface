import tkinter as tk
import tkinter.colorchooser as ch

w1 = tk.Tk()
w1.title('Color Editing')
w1.geometry('400x200')

# changing the configuration of the window
w1.config(bg = 'grey')

# adding an entry widget here
e1 = tk.Entry(w1)
e1.pack(padx = 2,pady = 3)

# changing configuration of entry
e1.config(selectbackground = 'lightgreen',selectforeground = 'green')

# adding label with different color
lb1 = tk.Label(w1,text = 'This label has change in its color',fg = 'red')
lb1.pack(padx = 2,pady = 3)

# adding method for choosing color
def choice():
    color = ch.askcolor(title = 'choosecolor')
    print('Color which is selected : ',color[1])

# applying colors to the Button Widget
btn1 = tk.Button(w1,text = 'Click and Change',fg = 'white',bg = 'black',activebackground = 'yellow',activeforeground = 'blue',command = choice)
btn1.pack(padx = 2,pady = 3)

w1.mainloop()