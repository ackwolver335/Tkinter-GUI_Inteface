import tkinter as tk 

w1 = tk.Tk()
w1.title('Canvas Move Method')
w1.geometry('400x300')

# Creating a canvas frame
canvas1 = tk.Canvas(w1)
canvas1.pack()

# variable for coordinates
x = 0
y = 0

# adding a rectangle to move it
rect1 = canvas1.create_rectangle(0,0,10,10,fill = 'black')
canvas1.move(rect1,x,y)

w1.mainloop()