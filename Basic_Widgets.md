# 🚀 Tkinter Widgets (Basics)

**Introduction** : Tkinter is Python’s standard GUI (Graphical User Interface) package. tkinter we can use to build out interfaces – such as buttons, menus, interfaces, and various kind of entry fields and display areas. We call these elements Widgets.

**Widgets** : In Tkinter, a widget is essentially a graphical component that the user can interact with. They can range from simple elements like buttons and labels to more complex ones like text entry fields, listboxes, and canvases. Each widget serves a specific purpose and can be customized to fit the design and functionality requirements of your application.

## Working of Widgets

Each widget in Tkinter is an instance of a specific class defined in the Tkinter Module. These classes provide methods and attributes that allow you to configure the widget’s appearance, behavior, and functionality. Widgets are typically added to the application’s window or frames using layout managers like pack(), grid(), or place(), which determine their position and size within the interface.

## 🛠 Basic Widgets

Below we have the combined table for **Basic Widgets** and their uses in *Python Tkinter Programming* :

| **Widgets** | **Their Uses** |
| :---------- | :------------- |
| *Label* | Used for getting the static text and images displayed |
| *Button* | Used for adding Buttons to the Application for different purposes and Operations |
| *Entry* | Used for taking textual inputs from the Users |
| *Frame* | Used as a Container for holding different widgets in a single frame |
| *RadioButton* | Used for taking one input out of multiple available options |
| *CheckButton* | Used for taking multiple inputs as options in Boolean Formats |
| *ListBox* | Displays the list of items for Selection of One |
| *ScrollBar* | Provides scrollable interface to the user in case of wide data arrangements |
| *Menu* | Provides a Menu Bar similar to the one available on different Application's Top Side |
| *Canvas* | Used for Drawing different lines,text and Visuals. |

## Tkinter - Label Widget

Tkinter Label is a widget that is used to implement display boxes where you can place text or images. The text displayed by this widget can be changed by the developer at any time you want. It is also used to perform tasks such as underlining the part of the text and spanning the text across multiple lines. 

It is important to note that a label can use only one font at a time to display text. To use a label, you just have to specify what to display in it (this can be text, a bitmap, or an image).

### Different Args in Label

1. **Simple Label** : Used for creating simple text label at the beginning with general pack methods.

*Syntax Code :*

```python
label1 = tk.Label(window,text = "Label Text")
label1.pack()
```

2. **Anchor Arg** : This argument is used for placing the label at particular position or with particular alignment.

*Syntax Code :*

```python
label2 = tk.Label(window,text = "Label",anchor = tk.CENTER)
label2.pack()
```

3. **Height and Width** : This argument is used in a way in order to keep the label specified by particular height and width getting a space on the main screen.

*Syntax Code :* 

```python
label3 = tk.Label(window,text = "Label",height = 10,width = 10)
label3.pack()
```

4. **Background and Font Editing** : This argument is used in order to keep the Background and Foreground color or text color changed on the Label to be in proper look and edited together by its different editing.

*Syntax Code :* 

```python
label4 = tk.Label(window,text = "Label",font = ("Fira Code",15),fg = "yellow",bg = "green")
label4.pack()
```

5. **Border and Effects** : This argument is used in order to mark the label with the Border and Effects over to different padding and relief styling.

*Syntax Code :*

```python
label5 = tk.Label(window,text = "Label",borderwidth = 4,relief = "solid",padx = 5,pady = 5)
label5.pack()
```

6. **Changing Label Text Dynamically** : This argument is used in order to change the Label text dynamically with the help of creating an event using Buttons.

*Syntax Code :*

```python
label6 = tk.Label(window,text = "Initial Text")
label6.pack()

def command1():
    label6.config(text = "Text Changed Dynamically")

b1 = tk.Button(window,text = "Changed Label Text")
b1.pack()
```

7. **Setting Position using place()** : This method is used in order to change the position of the label using known pixel position using units in pixels value.

*Syntax Code :*

```python
label7 = tk.Label(window,text = "Positioned Text")
label7.place(x = 10,y = 60)
```

8. **Setting Position using relx args** : These arguments are used in a way that we need to provide the value, by keeping in mind that the whole window's screen is a graph containing different points.

*Syntax Code :*

```python
label8 = tk.Label(window,text = "Another Positioned Method")
label8.place(relx = 0.5,rely = 0.5)
```

9. **Label Frame** : This is the method or creating the combination of different Labels together to form a whole frame containing different labels.

*Syntax Code :*

```python
lframe = tk.LabelFrame(window,text = "Label Frame",padx = 5,pady = 5)
lframe.pack(expand = "yes",fill = "both")

# labels for LabelFrames
lf1 = tk.Label(lframe,text = "First Label of Frame")
lf1.place(x = 10,y = 10)
lf2 = tk.Label(lframe,text = "Second Label of Frame")
lf2.place(x = 10,y = 20)
```

## Tkinter - Button Widget

The Tkinter Button widget is a graphical control element used in Python’s Tkinter library to create clickable buttons in a graphical user interface (GUI). It provides a way for users to trigger actions or events when clicked.

### Different Button's Overviews

1. **Button()** : This method includes simple button widget of tkinter in the main window of the App.

*Syntax Code :*

```python
btn1 = tk.Button(window,text = "Simple Button")
btn1.pack()
```

2. **Active Interfaces** : This method is used in order to keep the view of the Button changed when the user press on it.

*Syntax Code :*

```python
btn2 = tk.Button(window,text = "Active Changes",activebackground = "green",activeforeground = "yellow")
btn2.pack()
```

3. **Replacing Method** : This method is used in order to change the position of the Button using anchor argument as one of its example is been shown below.

*Sytnax Code :*

```python
btn3 = tk.Button(window,text = "Differ Position",anchor = 'sw')
btn3.pack()
```

4. **Border Method** : This method is used in order to create a Button containing Border on its all sides together with different of its arguments and options.

```python
btn4 = tk.Button(window,text = "Border Method",border = 3,borderwidth = 4,relief = 'groove')
btn4.pack()
```

5. **Height, Width and Padding** : These arguments are used in order to maintain the height width and padding space of the buttons in the GUI Interface.

*Syntax Code :*

```python
btn5 = tk.Button(window,text = "Maintained",height = 5,width = 20,padx = 2,pady = 3)
btn5.pack()
```

6. **Highlighting Options** : These are some arguments used in a way to get the Button Highlighted at a specific moment.

*Syntax Code :*

```python
btn6 = tk.Button(window,text = "Highlight",highlightbackground = "green",highlightcolor = "yellow",highlightthickness = 3)
btn6.pack()
```

7. **Close Window** : This command is used simply in order to close the window created by the Tkinter Module Functionality.

*Syntax Code :*

```python
btn7 = tk.Button(window,text = "Close",command = window.destroy)
btn7.pack()
```

8. **Justification and Wrapping** : These arguments are used in order to justify the button at a specific position and wraplength as per the width of the main window.

*Syntax Code :*

```python
btn8 = tk.Button(window,text = "Different",justify = "center",wraplength = 100)
btn8.pack()
```

9. **Multiple Commands** : This method or procedure is useful in order to run multiple methods or commands at once, this is done using lambda keyword by wrapping multiple methods in one single list.

*Syntax Code :*

```python
# Methods
def first1():
    print("First Method Initiated")

def second():
    print("Second Method Initiated")

btn9 = tk.Button(window,text = "Multiple",command = lambda : [first1(),second()])
btn9.pack()
```

10. **Opening New Window** : This method is useful when we need to create a new window using similar button just by one click.

*Syntax Code :*

```python
def newindow():
    w1 = tk.Tk()
    w1.title("New Window")
    w1.geometry("500x400")

btn10 = tk.Button(window,text = "New Window",command = newindow)
btn10.pack()
```

## Tkinter - Entry Widget

Python offers multiple options for developing a GUI (Graphical User Interface). Out of all the GUI methods, Tkinter is the most commonly used method. Python with Tkinter is the fastest and easiest way to create GUI applications. Creating a GUI using Tkinter is an easy task.

The Entry Widget is a Tkinter Widget used to Enter or display a single line of text.

### Different Entry Args

1. **Default Args** : This method in tkinter Entry is used in order to keep the Entry at Basic Levels, also adding font,padding is similar to the one we used in label widget.

*Syntax Code :*

```python
E1 = tk.Entry(window,font = ('Fira Code',10,'bold'))
E1.pack()
```

2. **Button Submittion** : This is an overall procedure in which we uses the Button together with the Entry Widget in Tkinter window to keep them working together to get the general required output from the users.

*Syntax Code :*

```python
L1 = tk.Label(window,text = "Enter your good name : ")
L1.pack()

E2 = tk.Entry(window)
E2.pack()

def command1():
    print(E1.get())
    window.destroy()

B1 = tk.Button(window,text = "Submit Data")
B1.pack()
```

3. **Canvas** : This method includes creating canvas in tkinter window that includes different lines, and working projects with it together with having a better explanation with the code below.

*Syntax Code :*

```python
c1 = tk.Canvas(w1,width = 250,height = 150)
c1.pack()

l2 = tk.Label(w1,text = "Enter your good name")
c1.create_window(100,110,window = l2)

l3 = tk.Label(w1,text = "Enter your owned email")
c1.create_window(100,150,window = l3)

e2 = tk.Entry(w1)
c1.create_window(200,110,window = e2)

e3 = tk.Entry(w1)
c1.create_window(200,150,window = e3)

def command2():
    messagebox.showinfo("Submitted","Your data is been submitted successfully !")
    e2.delete(0)
    e3.delete(0)

btn2 = tk.Button(w1,text = "Submit Data")
c1.create_window(150,200,window = btn2)
```

4. **get()** : This is a common method used by the Programmers and Developers for getting the data of the Entry created in order to take input from the user.

*Syntax Code :*

```python
L1 = tk.Label(window,text = "Enter your name here : ")
L1.pack()

E1 = tk.Entry(window)
E1.pack()
```

5. **delete()** : This method is simply used in order to delete the data from the Entry created in order to refresh for further details coming from the user's side.

*Syntax Code :*

```python
E1 = tk.Entry(window)
E1.pack()

B1 = tk.Button(window,text = "Clear Data",command = E1.delete(0))
B1.pack()
```

6. **insert()** : It is the method used in tkinter in order to make changes or insert the default value or data to the Entry Widget in tkinter.

*Syntax Code :*

```python
E1 = tk.Entry(window)
E1.insert(0,"Default Data")
E1.pack()
```

7. **Disabled Entry** : This is an optional argument used in order to get the entry disabled based on a particular condition or whenever the programmer or developer wants to.

*Syntax Code :*

```python
E1 = tk.Entry(window,state = DISABLED,justify = "center")
E1.pack()
```

## Tkinter - Frame Widget

A frame is a rectangular region on the screen. A frame can also be used as a foundation class to implement complex widgets. It is used to organize a group of widgets.

### Some Args Options : 

- **bg** : This option used to represent the normal background color displayed behind the label and indicator.
- **bd**: This option used to represent the size of the border around the indicator and the default value is 2 pixels.
- **cursor** : By using this option, the mouse cursor will change to that pattern when it is over the frame.
- **height** : The vertical dimension of the new frame.
- **highlightcolor** : This option used to represent the color of the focus highlight when the frame has the focus.
- **highlightthickness** : This option used to represent the color of the focus highlight when the frame does not have focus.
- **highlightbackground** : This option used to represent the thickness of the focus highlight..
- **relief** : The type of the border of the frame. It’s default value is set to FLAT.
- **width** : This option used to represents the width of the frame.

### Args/Methods Implementation

1. **General Frame with Label** : This method contains the availability and combination of different labels inside a particular frame together by its different customization options and methods included in it. 

*Syntax Code :*

```python
# frame
frame = tk.Frame(window,bg = "red",bg = 4,height = 100,width = 200,highlightbackground = "blue",highlightcolor = "green",relief = "groove")
frame.pack(padx = 3,pady = 4)

# Labels
l1 = tk.Label(frame,text = "Coding",font = ('Calibri',10),bg = "lightgreen",bd = 2,height = 3,width = 10)
l1.pack(padx = 2,pady = 2)

l2 = tk.Label(frame,text = "Programming",font = ('Arial',8),bg = "lightgreen",bd = 3,height = 2,width = 20)
l2.pack(padx = 2,pady = 2)
```

2. **Scrollable Frames** : This procedure include different options regarding horizontal and vertical formats for creating a scrollable frame together with different of its labels and textual data to be good looking in the final window.

*Syntax Code :*

```python
# Horizontal Scrollbar
h1 = tk.Scrollbar(window,orient = "horizontal")
h1.pack(side = "bottom",fill = "x")

# Vertical Scrollbar
v1 = tk.Scrollbar(window)
v1.pack(side = "right",fill = "y")

# Adding Textual Data
t1 = tk.Text(window,height = 10,width = 10,wrap = "none",xscrollcommand = h1.set,yscrollcommand = v1.set)

for i in range(13):
    t1.insert(tk.END,"Data Inserted\n")

t1.pack(side = "top",fill = "x")

# Configuration of Views
h1.config(command = t1.xview)
v1.config(command = t1.yview)
```

3. **Changing LabelFrame Border** : This process includes changing of border that is been initialised using different themes of the Labelframes regarding its frames.

*Syntax Code :*

```python
import tkinter.ttk as tk1

st1 = tk1.style()               # Styles
st1.theme_use("clam")
st1.configure("TLabelFrame",bordercolor = "red")

lframe1 = tk.LabelFrame(window,text = "Frame1")
lframe1.pack(padx = 20,pady = 20)

label1 = tk.Label(lframe1,text = "First One")
label1.pack()
```

## Tkinter - CheckButton Widget

The Checkbutton widget is a standard Tkinter widget that is used to implement on/off selections. Checkbuttons can contain text or images. When the button is pressed, Tkinter calls that function or method.

### Methods in Checkbutton :

| **Method Name** | **Uses** |
| --------------- | -------- |
| **deselect()** | It is used in order to turn off checkbutton from getting selected |
| **flash()** | It is used to flash the checkbutton between active and normal colors |
| **invoke()** | This is used to invoke() any method associated with the checkbutton |
| **select()** | It is used to select the checkbutton or to turn it on |
| **toggle()** | It is used for toggling between different checkbuttons |

### Different Usages of Checkbuttons 

1. **On Button Toggle Method** : This method or procedure is used in order to create a Checkbutton, together by its basic requirements to be fulfilled on checking at run time. This is a creative method regarding it.

*Syntax Code :*

```python
def cb_command():                               # Method to be initiated, when checkbutton is used
    if var1.get() == 1:
        print("Checkbutton is Turned ON")
    else:
        print("Checkbutton is Turned OFF")

var1 = tk.IntVar()                              # variable for taking input from checkbutton
cb1 = tk.Checkbutton(window,text = "Check1",variable = var1,onvalue = 1,offvalue = 0,command = cb_command)
cb1.pack(padx = 10,pady = 10)
```

2. **Multiple CheckButton** : This is another method or process for proper implementation of Multiple Checkbutton at once for providing a particular multiple choice question format to the user over to the GUI Window.

*Syntax Code :*

```python
var1 = tk.IntVar()          # Creating fot checkbutton activity
var2 = tk.IntVar()
var3 = tk.IntVar()

frm1 = tk.Frame(window,bd = 3,relief = 'groove',width = 300,height = 20)        # creating frame for checkbuttons
frm1.pack(padx = 10,pady = 10)

lb1 = tk.Label(window,text = "Checkbutton Choices",font = ('Fira Code',10))     # label for defining the frame
lb1.pack(padx = 2,pady = 3)

# defining a checkbutton
cbtn1 = tk.Checkbutton(frm1,text = "Choice1",variable = var1,onvalue = 1,offvalue = 0)
cbtn2 = tk.Checkbutton(frm1,text = "Choice2",variable = var1,onvalue = 1,offvalue = 0)
cbtn3 = tk.Checkbutton(frm1,text = "Choice3",variable = var1,onvalue = 1,offvalue = 0)

# packing them inside the frame
cbtn1.pack()
cbtn2.pack()
cbtn3.pack()
```

3. **Using Focus** : This is an argument which is been used in order to keep the focus of a particular checkbutton over to a particular option or not. Also this is been done by using ttk Module of TKinter Library.

*Syntax Code :*

```python
import tkinter.ttk as tk1           # required module for taking focus at checkbuttons
import tkinter as tk

frm1 = tk.Frame(window,bd = 1,width = width = 300,height = 20)                          # frame added
frm1.pack(padx = 5,pady = 8)

lb1 = tk.Label(frm1,text = "Programming Languages",bd = 1,font = ('Fira Code',12))      # label added
lb1.pack(padx = 4,pady = 6)

# adding checkbuttons
ckbtn1 = tk1.Checkbutton(frm1,text = "Java",takefocus = 1)
ckbtn2 = tk1.Checkbutton(frm1,text = "Python",takefocus = 1)

# packing checkbuttons
ckbtn1.pack(padx = 2,pady = 2)
ckbtn2.pack(padx = 2,pady = 2)
```

4. **Text Dynamic Change** : It is a simple way of creating the checkbutton which usually changes the text dynamically on getting checked or unchecked and below we have an example of it.

*Syntax Code :*

```python
import tkinter.ttk as tk1
import tkinter as tk

text1 = tk.StringVar()              # first string variable
text2 = tk.StringVar()              # second string variable

text1.set('OFF')                    # setting the values for it
text2.set('ON')

# adding checkbuttons
cbtn1 = tk1.Checkbutton(window,textvariable = text1,variable = text1,offvalue = "Turned OFF",onvalue = "Turned ON")
cbtn2 = tk1.Checkbutton(window,textvariable = text1,variable = text1,offvalue = "Switched OFF",onvalue = "Switched ON")

# packing the checkbuttons
cbtn1.pack(side = 'top',pady = 5)
cbtn2.pack(side = 'top',pady = 5)
```

## Tkinter - RadioButton Widget

The Radiobutton is a standard Tkinter widget used to implement one-of-many selections. Radiobuttons can contain text or images, and you can associate a Python function or method with each button. When the button is pressed, Tkinter automatically calls that function or method.

### Different Usage Methods

1. **Multiple RadioButtons (TK Module)** : This is the first method of adding radiobuttons to the main window of our GUI Applications. It is been established using the RadioButton method with the tkinter Module, together by using the value argument and variable one. Below we have a proper format structure of the code.

*Syntax Code :*

```python
string1 = tk.StringVar(window,'1')

frm1 = tk.Frame(window,bd = 2,relief = 'ridge',height = 10,width = 200,bg = "lightgreen")               # Frame Adjusted
frm1.pack(padx = 2,pady = 3)

lb1 = tk.Label(frm1,text = "Radio Buttons",font = ('Fira Code',10),bd = 2,relief = 'groove')            # label created
lb1.pack(padx = 2,pady = 3)

# Establising RadioButtons
rd1 = tk.Radiobutton(frm1,text = "Button1",variable = string1,value = '1')
rd2 = tk.Radiobutton(frm1,text = "Button2",variable = string1,value = '2')
rd3 = tk.Radiobutton(frm1,text = "Button3",variable = string1,value = '3')

# packing them in the window
rd1.pack(padx = 2,pady = 3,ipady = 4)
rd2.pack(padx = 2,pady = 3,ipady = 4)
rd3.pack(padx = 2,pady = 3,ipady = 4)
```

2. **Ttk Module RadioButtons** : This is another method of creating radiobuttons using ttk module in tkinter Library. And the difference regarding the both the module is just of the view, which is available in the preview folder in this repo. Further code example is been given below.

*Syntax Code :*

```python
str1 = tk.StringVar(window,'A')

frm1 = tk.Frame(window,bd = 2,relief = 'ridge',height = 10,width = 200,bg = "lightgreen")               # Frame Adjusted
frm1.pack(padx = 2,pady = 3)

lb1 = tk.Label(frm1,text = "Radio Buttons",font = ('Fira Code',10),bd = 2,relief = 'groove')            # label created
lb1.pack(padx = 2,pady = 3)

# Establising RadioButtons
rd1 = tk.Radiobutton(frm1,text = "Button1",variable = str1,value = 'A')
rd2 = tk.Radiobutton(frm1,text = "Button2",variable = str1,value = 'B')
rd3 = tk.Radiobutton(frm1,text = "Button3",variable = str1,value = 'C')

# packing them in the window
rd1.pack(padx = 2,pady = 3,ipady = 5)
rd2.pack(padx = 2,pady = 3,ipady = 5)
rd3.pack(padx = 2,pady = 3,ipady = 5)
```

## Tkinter - Listbox Widget

The ListBox widget is used to display different types of items. These items must be of the same type of font and having the same font color. The items must also be of Text type. The user can select one or more items from the given list according to the requirement.

### General Methods in Listbox

| **Method Name** | **Uses** |
| --------------- | -------- |
| **get()** | Used to get all the items of the list in a particular range |
| **activate(index)** | Used to activate a particular list item as per given index or passed index. |
| **size()** | Used to get the number of lines in the list |
| **delete(start,last)** | Used to delete lines as per specified index passed in the function/method |
| **nearly(y)** | Returns the index of the line nearest to the line whose index is passed |
| **curseselection()** | Returns a tuple for all the lines which are selected by the user's side |

### Different Methods in ListBox

1. **General Listbox** : This is simple method or procedure for getting the Listbox created in order to learn its creation in main window simply. We further have its different arguments like activestyle, insert() method for placing the list items as per the passed index, and at the end packing it simply using the general pack() method.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 2,relief = 'groove')
frm1.pack(padx = 2,pady = 3)

lb1 = tk.Listbox(frm1,height = 2,width = 10,activestyle = 'dotbox')

lb1.insert(1,'Data1')                        # inserting data manually
lb1.insert(2,'Data2')
lb1.insert(3,'Data3')
lb1.insert(4,'Data4')

lb1.pack(padx = 2,pady = 3,side = 'left',fill = 'both')
```

2. **Scrollbar Listbox** : This is another method of creating a listbox together by adding scrollbar to it. It is been done with the use of another widget which is scrollbar to the frame or window in which the ListBox is been created. Below we have further code explanation regarding it.

*Syntax Code :*

```python
frm1 = tk.Frame(height = 2,width = 3,activestyle = 'dotbox')                            # main frame
frm1.pack(padx = 2,pady = 3)                                                            # frame packed

lb1 = tk.Listbox(frm1,height = 2,width = 3,activestyle = 'dotbox')                      # listbox initiated

# Adding some items to it
lb1.insert(1,'Data1')
lb1.insert(2,'Data2')

lb1.pack(padx = 2,pady = 3,side = 'left',fill = 'both')                                 # listbox packed

scrlbar1 = tk.Scrollbar(frm1)                                                           # scrollbar created
scrlbar1.pack(side = 'right',fill = 'both')                                             # scrollbar packed

lb1.config(yscrollcommand = scrlbar1.set)                                               # configured listbox for setting scrollbar
scrlbar1.config(command = lb1.yview)                                                    # configured scrollbar
```

3. **Selecting Particular List Item** : This is particular procedure done in order to select a partcular list item with the use of two method together with the curseselection() and get() method also printing them in the console for getting the review.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 2,relief = 'groove')                                    # frame established
frm1.pack(padx = 2,pady = 3)                                                        # frame packed

lb1 = tk.Listbox(frm1,height = 2,width = 3,activestyle = 'dotbox')                  # listbox established

# Inserting data or list items
lb1.insert(1,'Data1')
lb1.insert(2,'Data2')
lb1.insert(3,'Data3')

lb1.pack(padx = 2,pady = 3)                                                         # listbox established

def command1():                                                                     # Method for printing selected list item
    for i in lb1.curseselection():
        print(lb1.get(i))

btn1 = tk.Button(window,text = 'Print Selected Item',command = command1)
btn1.pack(padx = 2,pady = 3)
```

4. **Deleting Particular List Item** : This particular method is been used in order to delete a particular selected item of the list. And this procedure is been established using curseselection() and delete() method as per the code shown below.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 2,relief = 'groove')                        # frame established
frm1.pack(padx = 2,pady = 3)                                            # frame packed

lb1 = tk.Listbox(frm1,height = 2,width = 10,activegstyle = 'dotbox')    # listbox established

lb1.insert(1,'Data1')                                                   # adding items to the listbox
lb1.insert(2,'Data2')
lb1.insert(3,'Data3')

lb1.pack(padx = 2,pady = 3)                                             # packing the listbox

def command1():                                                         # method for the button
    for i in lb1.curseselection():
        delete(i)

btn1 = tk.Button(window,text = 'Delete Selected',command = command1)    # button for deleting list items
btn1.pack(padx = 2,pady = 3)                                            # packing the buttons
```

## Tkinter - Scrollbar Widget

Python offers multiple options for developing a GUI (Graphical User Interface). Out of all the GUI methods, Tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with Tkinter is the fastest and easiest way to create GUI applications. 

Creating a GUI using Tkinter is an easy task.The scrollbar widget is used to scroll down the content. We can also create the horizontal scrollbars to the Entry widget.

### Methods in Scrollbar Widget

| **Method's Name** | **Uses** |
| ----------------- | -------- |
| **get()** | Used in order to get the current coordinates of the scrollbar position |
| **set(first,last)** | It is used for setting up the scrollbar with other available widgets and in other widget we uses the yscrollcommand or xscrollcommand for setting up scrollbar to them |

### Different Implementation of Scrollbar

1. **General Implementation** : This is the simple implementation for getting the scrollbar setup regarding a particular frame or window and in usual way we used to get the config() method for getting the scrollbar added together with the list view. Further will be explained with the help of code below.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 2,relief = 'groove')                        # frame established
frm1.pack(padx = 2,pady = 3)                                            # frame packed

label1 = tk.Label(frm1,text = 'Scrollbar Frame',font = ('Fira Code',10),bd = 2,relief = 'groove')       # label established
label1.pack(padx = 2,pady = 3)                                                                          # label packed

scrlbr1 = tk.Scrollbar(frm1)                                                                            # Scrollbar established
scrlbr1.pack(side = 'right',fill = 'y')                                                                 # Scrollbar packed

list1 = tk.Listbox(frm1,yscrollcommand = scrlbr1.set)                                                   # listbox established and scrollbar set

for i in range(1,50):                                                   # adding items in list
    list1.insert(i,"Coding" + str(i))

list1.pack(side = 'left',fill = 'both',padx = 2,pady = 3)               # packing listbox

# Configuration of scrollbar regarding listbox
scrlbr1.config(command = list1.yview)
```

2. **Using Horizontal Keyword** : This particular scrollbar is setted up with the use of Text() method and particular arguments that are used in this one for converting the particular code into a proper working frame for the main window.

*Syntax Code :*

```python
frame1 = tk.Frame(w1,bd = 3,height = 10,width = 300,relief = 'groove')
frame1.pack(padx = 2,pady = 3)

# data to be placed in both vertical format
data_hz = ("A B C D E F G H J K L M N O P Q R S T U V W X Y Z")
data_vt = ("a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nu\nv\nw\nx\ny")

# adding scrollbar data here
svbar = tk.Scrollbar(frame1)
svbar.pack(side = 'right',fill = 'y')

shbar = tk.Scrollbar(w1,orient = tk.HORIZONTAL)
shbar.pack(side = 'bottom',fill = 'x')

# creating two different text box
textbx = tk.Text(frame1,height = 400,width = 400,yscrollcommand = svbar.set,xscrollcommand = shbar.set,wrap = 'none')
textbx = tk.Text(frame1,height = 400,width = 400,yscrollcommand = svbar.set,xscrollcommand = shbar.set,wrap = 'none')

# packing them all
textbx.pack(expand = 0,fill = 'both')
textbx.pack(expand = 0,fill = 'both')

# Inserting them in the frame
textbx.insert(tk.END,data_hz)
textbx.insert(tk.END,data_vt)

# changing its configuration for it
shbar.config(command = textbx.xview)
svbar.config(command = textbx.yview)
```

## Tkinter - Menu Widgets

Menus are the important part of any GUI. A common use of menus is to provide convenient access to various operations such as saving or opening a file, quitting a program, or manipulating data. Toplevel menus are displayed just under the title bar of the root or any other toplevel windows.

### Different Args in Menu

1. **Menu() Initiation** : This is the initial method used in order to create a specific menu together by applying different commands in the options available in the list of it. Also the configuration of it at the end together with the window variable created at first.

*Syntax Code :*

```python
import tkinter as tk                    # main module for GUI Designing

w1 = tk.Tk()                            # window
w1.title("Menu Widget")                 # window title
w1.geometry('400x300')                  # window default dimension

# initiating menu bar
menu1 = tk.Menu(w1,background = 'green',fg = 'red')

file = tk.Menu(menu1,tearoff = 0)                           # created file option
menu1.add_cascade(label = 'File',menu = file)               # adding file option
file.add_cascade(label = 'Open New')                        # Options
file.add_seperator()
file.add_cascade(label = 'Close',command = w1.destroy)

w1.config(menu = menu1)                                     # menu added to the main window
```

2. **Option Menu() Method** : This is another kind of method used for specific method in order to specify something with a particular option. Further explanation is been given in the code below.

*Syntax Code :*

```python
text1 = tk.StringVar()                  # variable for storing selected value
list1 = ['First','Second','Third','Fourth']

opt1 = tk.OptionMenu(w1,text1,*(list1))
opt1.config(bg = "lightgreen",fg = "white")
opt1.grid(pady = 5)
```

## Tkinter - Canvas Widget

The Canvas widget lets us display various graphics on the application. It can be used to draw simple shapes to complicated graphs. We can also display various kinds of custom widgets according to our needs.

### Different Methods in Canvas

1. **create_line(x1,y1,x2,y2,..,options = ..)** : This method is used in order to create a line inside a particular frame widget or window widget.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 2,relief = 'groove')                                # frame for Canvas
frm1.pack(padx = 2,pady = 3)

cvs1 = tk.Canvas(frm1,bg = 'lightblue',height = 200,width = 300)                # Canvas established inside Frame
cvs1.pack(fill = tk.BOTH,expand = True)                                         # Canvas packed

lin1 = cvs1.create_line(15,25,200,25)                                           # straight canvas line
lin2 = cvs1.create_line(300,35,300,200,dash = (5,2))                            # straight vertical line
lin3 = cvs1.create_line(55,85,155,85,105,180,55,85)                             # straight triangle line
```

2. **create_rectangle(x1,y1,x2,y2,..option = ..)** : This method in tkinter Canvas is used for creating rectangular shape inside a particular selected frame or window for different designing with the help of Canvas.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 2,relief = 'groove')                            # Frame Established
frm1.pack(padx = 2,pady = 3)

c1 = tk.Canvas(frm1,bg = 'lightgreen',height = 100,width = 300)             # Canvas Frame
c1.pack(padx = 2,pady = 3)

rect1 = c1.create_rectangle(20,40,100,120,fill = 'pink')                    # rectangle created
```

3. **create_arc(x1,y1,x2,y2,..option = ...)** : This particular method is used in order to create an arc in the Frame or window selected for the Canvas Frame for designing different tools or frames.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 2,relief = 'ridge')                             # frame established
frm1.pack(padx = 2,pady = 3)                                                # frame packed

c1 = tk.Canvas(frm1,bg = 'lightblue',height = 100,width = 300)              # Canvas Established
c1.pack(padx = 2,pady = 3)                                                  # Canvas Packed

arc1 = c1.create_arc(180,150,80,210,start = 0,extent = 200,fill = 'red')    # arc created
```

4. **create_oval(x1,y1,x2,y2,..option = ..)** : This particular method or function of Canvas Class is been used in order to create an oval shape in the frame of Canvas, also the arguments are needed to be filled as per requirements.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 2,relief = 'groove')                            # frame established
frm1.pack(padx = 2,pady = 3)                                                # frame packed

c1 = tk.Canvas(frm1,bg = 'lightblue',height = 150,width = 300)              # Canvas created
c1.pack(padx = 2,pady = 3)                                                  # Canvas Packed

oval1 = c1.create_oval(80,30,140,150,fill = 'green')                        # Oval Created
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