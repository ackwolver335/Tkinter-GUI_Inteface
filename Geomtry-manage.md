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