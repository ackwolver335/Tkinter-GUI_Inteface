import tkinter as tk 

w1 = tk.Tk()
w1.title('Pack Method')
w1.geometry('500x300')

# Creating a Frame here for using pack method
frm1 = tk.Frame(w1)
frm1.pack(fill = 'both',expand = True)

# Adding some widgets to it 
btn1 = tk.Button(frm1,text = 'Button1',background = 'lightblue')
btn1.pack(fill = 'both',expand = True,side = 'top')

btn2 = tk.Button(frm1,text = 'Button2',background = 'lightgreen')
btn2.pack(fill = 'both',expand = True,side = 'bottom')

w1.mainloop()