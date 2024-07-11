import tkinter as tk 

w1 = tk.Tk()
w1.title('Binding Function/Method')
w1.geometry('500x300')

# defining methods for binding the frame
def enter(event):
    print('Button 2 pressed at x = %d,y = %d'%(event.x,event.y))

def leave(event):
    print('Button 3 pressed at x = %d,y = %d'%(event.x,event.y))

# Using Binding Method on a frame
frm1 = tk.Frame(w1,bd = 2,relief = 'raised',width = 200,height = 300)
frm1.pack()

frm1.bind('<Enter>',enter)
frm1.bind('<Leave>',leave)

w1.mainloop()