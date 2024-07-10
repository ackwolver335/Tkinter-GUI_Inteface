import tkinter as tk 

w1 = tk.Tk()
w1.title('Canvas Widgets')
w1.geometry('400x300')

# Canvas space created in window
canvas1 = tk.Canvas(w1)

# adding different shapes in Canvas
canvas1.create_oval(10,10,80,80,outline = 'green',fill = 'black',width = 3)
canvas1.create_oval(110,10,210,80,outline = 'blue',fill = 'red',width = 4)
canvas1.create_rectangle(230,10,290,60,outline = 'black',fill = 'yellow',width = 3)
canvas1.create_arc(30,200,120,100,start = 0,outline = 'red',width = 3)

# defining some points for the polygon
points = [150,100,200,120,240,180,210,200,150,150,100,200]

# adding the points to the polygon
canvas1.create_polygon(points,outline = 'yellow',fill = 'orange',width = 4)

# packing the canvas for final placing into the Window
canvas1.pack(fill = 'both',expand = 1)

w1.mainloop()