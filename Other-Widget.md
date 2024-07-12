# 🚀 Other Tkinter Widgets and Methods

The choice of fonts, colors, and images can make a significant impact on the user experience and the overall aesthetic appeal of an application. In this section, we will delve into the intricacies of customizing fonts, exploring a variety of color options, and incorporating images into your projects.

## 🛠 Fonts Widget - Tkinter

Fonts in Tkinter are used to customize the appearance of text displayed in various widgets such as labels, buttons, entry widgets, and more. They allow you to control the font family, size, weight, style, and other properties of the text.

### Use Cases in Fonts

- **Customizing Text** : You can use fonts to set the style, size, and family of text displayed in widgets like labels, buttons, and text widgets.
- **Improving Readability** : Choosing the right font and size can improve the readability of your application, making it more user-friendly.
- **Consistency** : By defining fonts for your application, you can maintain consistency in the appearance of text across different widgets and windows.
- **Accessibility** : Using appropriate fonts and sizes can improve accessibility for users with visual impairments, ensuring that text is legible and easy to read.

*Syntax Code :*

```python
# Using it while creating different widgets
frm1 = tk.Frame(w1)
frm1.pack(padx = 2,pady = 3)

# Adding label for testing the designed fonts
lb1 = tk.Label(frm1,text = 'Label Containing Normal Font Format',font = normal_font)        # using normal font here
lb1.pack(padx = 2,pady = 3)

# another self designed font
font1 = tkfont.Font(family = 'Helvetica',size = 12,weight = 'bold')                         # adding bold font style

# adding another label for testing it
lb2 = tk.Label(frm1,text = 'This is another bold font varient',font = font1)
lb2.pack(padx = 2,pady = 3)
```

## 🛠 Color Widget - Tkinter

Colors are essential for enhancing the visual appeal and user experience of graphical user interfaces (GUIs). In Tkinter, the popular Python GUI toolkit, you have access to a range of color options to tailor the appearance of widgets. Let’s delve into the common color options and how they are utilized in Tkinter.

### Different Arguments and Options

| **Arguments** | **Options and Uses** |
| :------------ | :------------------- |
| **Active Background and Foreground** | - *active foreground* is used for getting the color of the text changed whent the widget is active. |
| | - *active background* is used for getting the color of the widget changed when it is active. |
| **Background and Foreground** | - *background or bg*, it is used for getting the background changed with specific color |
| | - *foreground or fg* is used for changing or applying the color of text in the widget |
| **Disabled State Colors** | - *disabledforeground* is used for setting the color of the widget when it is disabled |
| | - *highlightbackground* is used for setting the color of the highlighted region when the widgeg is focused |
| | - *highlightcolor*, it is used for defining foreground color of highlight region when that particular widget has focus |
| **Selection Colors** | - *selectbackground* is used for setting up the background color for selected items within the widgets, or in selected entry or in Listbox. |
| | - *selectforeground* is used for defining the foreground color of the current or selected widget |

*Syntax Code :*

```python
# adding an entry widget here
e1 = tk.Entry(w1)
e1.pack(padx = 2,pady = 3)

# changing configuration of entry
e1.config(selectbackground = 'lightgreen',selectforeground = 'green')

# adding label with different color
lb1 = tk.Label(w1,text = 'This label has change in its color',fg = 'red')
lb1.pack(padx = 2,pady = 3)
```

## 🛠 Image Widget - Tkinter

There are numerous tools for designing GUI (Graphical User Interface) in Python such as tkinter, wxPython, JPython, etc where Tkinter is the standard Python GUI library, it provides a simple and efficient way to create GUI applications in Python.

iconphoto() method is used to set the titlebar icon of any tkinter/toplevel window. But to set any image as the icon of titlebar, image should be the object of PhotoImage class.

*Syntax Code :*

```python
import tkinter as tk 
from PIL import ImageTk, Image
from tkinter import PhotoImage as PI

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
```

## 🛠 Canvas Widget - Tkinter

The Canvas widget lets us display various graphics on the application. It can be used to draw simple shapes to complicated graphs. We can also display various kinds of custom widgets according to our needs.

| **Argument's Name** | **Uses** |
| ----------------- | -------- |
| **root** | It is the window or frame where the canvas is placed or packed with |
| **height** | It is used for defining the height in numbers, and its unit is Pixels |
| **width** | It is used for defining the width in numbers, in similar way the height is defined |
| **scrollregion** | A tuple argument defined in a region in order to set the scrolling from all the directions left, top, bottom and right side |
| **confine** | It is helpful in deciding that if the canvas can be defined outside the scroll region |
| **relief** | Used for setting the type or category of the Border if set by the developer or programmer |

*Syntax Code :*

```python
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
```

## 🛠 Binding Function - Tkinter

It provides a variety of Widget classes and functions with the help of which one can make our GUI more attractive and user-friendly in terms of both looks and functionality.

The binding function is used to deal with the events. We can bind Python’s Functions and methods to an event as well as we can bind these functions to any particular widget.

*Syntax Code :*

```python
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
```

## 📫 How to Reach Me

- **Email** - abhaych335@gmail.com
- **Instagram** - [@coding.needs](https://www.instagram.com/coding.needs/)
- **Twitter** - [@AbhayCh84760](https://x.com/AbhayCh84760)

## Support Me

If you likes what I do and want to support me :

- Give me a ⚡️ Star on my Repo
- Share my [work](https://github.com/ackwolver335/Tkinter-GUI_Inteface) and [profile](https://github.com/ackwolver335) with your network

Thanks for visiting my Github Repo ! Hope you find my projects useful, helpful and inspiring. Let's connect and collaborate to build something amazing !

Abhay Chaudhary [Ack Wolver](https://github.com/ackwolver335/ackwolver335) !