# 🚀 Tkinter Geometry Management

Efficiently managing the geometry of Tkinter windows and widgets is essential for creating polished user interfaces. In this section, we’ll cover everything from setting window dimensions to handling resizing, padding, and widget positioning. 

We’ll explore methods like place(), grid(), and pack() to help you create organized and responsive layouts. Additionally, we’ll delve into advanced techniques like the PanedWindow widget.

## General Usable Methods

- **place()** : Used for providing specific position in the Entire GUI Window.
- **pack()** : Used for placing at the position after the earlier widget.
- **grid()** : It is used for placing the elements in the format of grid view or grid structure.

## Place() Method - Geometry Management

The Place geometry manager is the simplest of the three general geometry managers provided in Tkinter. It allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window. You can access the place manager through the place() method which is available for all standard widgets.

It is usually not a good idea to use place() for ordinary window and dialog layouts; its simply too much work to get things working as they should. Use the pack() or grid() managers for such purposes.

*Syntax Code :*

```python
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
```

## Grid() Method - Geometry Management

The Grid geometry manager puts the widgets in a 2-dimensional table. The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget. The grid manager is the most flexible of the geometry managers in Tkinter.

*Syntax Code :*

```python
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
```

## Pack() Method - Geometry Management

The Pack geometry manager packs widgets relative to the earlier widget. Tkinter literally packs all the widgets one after the other in a window.  We can use options like fill, expand, and side to control this geometry manager.

*Syntax Code :*

```python
# Creating a Frame here for using pack method
frm1 = tk.Frame(w1)
frm1.pack(fill = 'both',expand = True)

# Adding some widgets to it 
btn1 = tk.Button(frm1,text = 'Button1',background = 'lightblue')
btn1.pack(fill = 'both',expand = True,side = 'top')

btn2 = tk.Button(frm1,text = 'Button2',background = 'lightgreen')
btn2.pack(fill = 'both',expand = True,side = 'bottom')
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