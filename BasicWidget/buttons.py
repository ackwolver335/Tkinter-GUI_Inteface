import tkinter as tk

# Window
window = tk.Tk()

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

# Ending the Window
window.mainloop()