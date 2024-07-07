import tkinter as tk
import tkinter.ttk as tk1

w1 = tk.Tk()
w1.title('Grid Method')
w1.geometry('500x300')

# Learning Grid Method by making its different Frames
frm1 = tk.Frame(w1,bd = 2)
frm1.pack(padx = 2,pady = 3)

# Creating the elements for the Frames
lb1 = tk.Label(frm1,text = 'First Name',font = ('Fira Code',10))
lb2 = tk.Label(frm1,text = 'Last Name',font = ('Fira Code',10))

# Placing it with the help of grid
lb1.grid(row = 0,column = 0,pady = 2)
lb2.grid(row = 1,column = 0,pady = 2)

# Getting some entry used here
e1 = tk.Entry(frm1)
e2 = tk.Entry(frm1)

# Placing the entries in the frame
e1.grid(row = 0,column = 1,pady = 2)
e2.grid(row = 1,column = 1,pady = 2)

# Another Frame for Another Varient of Grid Method
frm2 = tk.Frame(w1,bd = 2,relief = 'ridge')
frm2.pack(padx = 2,pady = 3)

# Creating the elements for the Frames
lb3 = tk.Label(frm2,text = 'First Name',font = ('Fira Code',10))
lb4 = tk.Label(frm2,text = 'Last Name',font = ('Fira Code',10))

# Placing it with the help of grid
lb3.grid(row = 0,column = 0,pady = 2)
lb4.grid(row = 1,column = 0,pady = 2)

# Getting some entry used here
e3 = tk.Entry(frm2)
e4 = tk.Entry(frm2)

# Placing the entries in the frame
e3.grid(row = 0,column = 1,pady = 2)
e4.grid(row = 1,column = 1,pady = 2)

# Adding some other elements to it
cbtn1 = tk1.Checkbutton(frm2,text = 'Preview')                      # Checkbutton added
cbtn1.grid(row = 2,column = 0,columnspan = 2)                       # Checkbutton Placed

# Adding the Image
img = tk.PhotoImage(file = r"E:\Python\tkint\Images\First1.png")
img1 = img.subsample(2,2)

# Setting image with label
lb5 = tk.Label(frm2,image = img1,width = 50,height = 50)
lb5.grid(row = 0,column = 2,columnspan = 2,rowspan = 2,padx = 5,pady = 5)

# Adding some Buttons here
btn1 = tk.Button(frm2,text = 'Zoom In')
btn2 = tk.Button(frm2,text = 'Zoom Out')

# Placing these button with grid methods
btn1.grid(row = 2,column = 2)
btn2.grid(row = 2,column = 3)

# Some other useful methods are explained below
# using grid location method for checking its coordinates

def click(event):

    # getting the coordinates of these
    x = event.x_root - frm1.winfo_rootx()
    y = event.y_root - frm1.winfo_rooty()

    z = frm1.grid_location(x,y)                     # now these coordinates will have the frame locations
    print(z)

def grdsz(event):

    # getting the size of the grid
    x = frm1.grid_size()
    print(x)

# using button for getting the frame location
btn3 = tk.Button(w1,text = 'Button1')
btn3.pack(padx = 2,pady = 3)

w1.bind('<Button-1>',click)                         # Binding for getting the coordinates of first frame

# Button for getting the grid size
btn4 = tk.Button(w1,text = 'Button2')
btn4.pack(padx = 2,pady = 3)

w1.bind('<Button-2>',grdsz)                         # Binding for getting the size of the grid

w1.mainloop()