import tkinter as tk 
from PIL import ImageTk, Image
from tkinter import PhotoImage as PI
from tkinter import filedialog

w1 = tk.Tk()
w1.title('Image Methods Part - 1')
w1.geometry('400x200')

# Loading image in the code first
img1 = ImageTk.PhotoImage(Image.open('First1.png'))

# reading the image
lb1 = tk.Label(w1,image = img1,width = 100,height = 100)
lb1.pack(side = 'left')

# using canvas for creating specific image
canvas1 = tk.Canvas(w1,width = 200,height = 200)
canvas1.pack()

canvas1.create_image(100,20,anchor = 'nw',image = img1)             # image created using canvas

# adding icon to the Tkinter Window
p1 = PI(file = 'First1.png')
w1.iconphoto(False,p1)

# defining method for Button Command
def openfilename():
    filename = filedialog.askopenfilename(title = 'First1.png')
    return filename

def openimg():
    
    # Getting the file name first
    x = openfilename()

    # using it to open image first
    img = Image.open(x)

    # resizing image and applying high quality sampling
    img = img.resize((250,250),Image.LANCZOS)

    # Using Photoimage for icon or picture direct
    img = ImageTk.PhotoImage(img)

    # again creating a label for adding image to window
    lb2 = tk.Label(w1,image = img)
    lb2.pack(padx = 2,pady = 3)


btn1 = tk.Button(w1,text = 'Open Image',command = openimg)
btn1.pack(padx = 2,pady = 3)

# Resizing the image
image = Image.open('First1.png')
resize_img = image.resize(size = (100,100))
img2 = ImageTk.PhotoImage(resize_img)

# Adding image using label in the window
lb3 = tk.Label(w1,image = img2)
lb3.pack(padx = 2,pady = 3)

w1.mainloop()