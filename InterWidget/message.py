import tkinter as tk 

w1 = tk.Tk()
w1.title('Message Widget')
w1.geometry('500x200')

# Message Widget
frm1 = tk.Frame(w1,bd = 3,relief = 'groove')
frm1.pack(padx = 2,pady = 3)

lb1 = tk.Label(frm1,text = 'This is a Label',font = ('Fira Code',10))
lb1.pack(padx = 2,pady = 3)

msg1 = tk.Message(frm1,text = 'This is an important message',font = ('Fira Code',8))
msg1.pack(padx = 2,pady = 3)

w1.mainloop()