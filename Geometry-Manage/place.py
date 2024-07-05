import tkinter as tk 
import tkinter.ttk as tk1

w1 = tk.Tk()
w1.title('Place Method')
w1.geometry('500x300')

# First Method for placement of Widgets or Elements
# Using relx and relx in place() method
lb1 = tk.Label(w1,text = 'This is a simple label',font = ('Fira Code',10))                  # Lable Initiated
lb1.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)                                         # Lable Placed

# Second Method for placement of Widget inside Frame
btn1 = tk.Button(w1,text = 'Close Window',command = w1.destroy)                             # Button Created
btn1.place(x = 10,y = 5)                                                                    # Button Placed

# Third Method for placement of Widgets
btn2 = tk1.Button(w1,text = 'Another Button')
btn2.place(anchor = 'nw')

# Another Button for btn2 proper placement
btn3 = tk.Button(w1,text = 'Click Me !')
btn3.place(in_ = btn2,relx = 0.5,rely = 0.5,anchor = 'center')

w1.mainloop()