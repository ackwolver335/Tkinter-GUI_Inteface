# 🚀 Tkinter Widget (Intermediate)

**Introduction** :- Tkinter is the most commonly used library for developing GUI (Graphical User Interface) in Python. It is a standard Python interface to the Tk GUI toolkit shipped with Python. As Tk and Tkinter are available on most of the Unix platforms as well as on the Windows system, developing GUI applications with Tkinter becomes the fastest and easiest.

**Some Needed** :- Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python Tkinter is the fastest and easiest way to create GUI applications. Creating a GUI using Tkinter is an easy task.

## 🛠 Intermediate Widget

These are useful in providing some other different features regarding message boxes and other different tools. Creating more Interactive different tools inside your owned application or designed application with the help of different intermediate widgets like Combobox, Scale, Toplevel, message box. These customization tools will surely give you a new look to the Designed Application.

### ⚡️ Overview Table

| **Widgets** | **Uses** |
| :---------- | :------- |
| **Combobox** | It provides a proper dropdown list of options with editable entry |
| **Scale** | It is been created in order to select a value within a particular range |
| **TopLevel** | Used for creating an additional window or dialog box |
| **Message** | Used for displaying a simple messagebox or notification |
| **MenuButton** | Creates a Button for opening the menu of the Window |
| **ProgressBar** | Used for creating a proper progress related to a particular task |
| **SpinBox** | Provides a numerical input and output options to be shown a interact using Arrow Keys |

## Tkinter Intermediate Widget - Combobox

Combobox is a combination of Listbox and an entry field. It is one of the Tkinter widgets where it contains a down arrow to select from a list of options. It helps the users to select according to the list of options displayed. 

When the user clicks on the drop-down arrow on the entry field, a pop up of the scrolled Listbox is displayed down the entry field. The selected option will be displayed in the entry field only when an option from the Listbox is selected.

### Different Method in Combobox

1. **Establishing Combobox()** : This is a procedure that is been used in order to create a combobox and this is been created with the help of a Module which is a part of tkinter Module *ttk* class in it. Further explanation will be provided below in the form of code.

*Syntax Code :*

```python
import tkinter as tk
import tkinter.ttk as ttk1

frm1 = tk.Frame(window,bd = 3,relief = 'groove')                        # frame for Combobox
frm1.pack(padx = 2,pady = 3)                                            # frame packed

str1 = tk.StringVar()                                                   # String variable for Combo Selected Values

cb1 = ttk1.Combobox(frm1,width = 30,textvariable = str1)                # Combobox Creation

l1 = ['January','February','March','April','May','June','July','August','September','Octuber','November','December']
cb1['values'] = l1                                                      # providing data for options
cb1.pack(padx = 3,pady = 4)
cb1.current(0)                                                          # cb1.current() will not show anything in Combobox
```

2. **Getting Selected Item** : This is an overall procedure of getting the item that is been selected by the user and getting a button for clearing overall data or all the data. And the data is taken either the similar one or another one. Below we have the code for its explanation regarding selection in the Combobox.

*Syntax Code :*

```python
import tkinter as tk
import tkinter.ttk as ttk1

frm1 = tk.Frame(window,bd = 3,relief = 'ridge')                         # frame established
frm1.pack(padx = 2,pady = 3)                                            # frame packed

# list data
l1 = ['January','February','March','April','May','June','July','August','September','Octuber','November','December']

def getindex(*args):
    if str2.get() >= str(0):
        lb1 = tk.Label(frm1,text = 'The Value at index ' + str(cb1.current()) + ' is ' + str(str1.get()))
        lb1.pack(padx = 2,pady = 3)

def clear_all():
    cb1.set('')

str1 = tk.StringVar()                                                   # String variable for Selected data

cb1 = ttk1.Combobox(frm1,textvariable = str1)                           # Combobox created
cb1['values'] = l1                                                      # data added
cb1.current(0)                                                          # adding current instance
cb1['state'] = 'readonly'
cb1.pack(padx = 2,pady = 4)

str1.trace_add('write',getindex)                                        # tracing the selected item

btn1 = tk.Button(window,text = 'Clear All',command = clear_all)         # btn for clearing or reseting
btn1.pack(padx = 2,pady = 3)
```

## Tkinter Intermediate Widget - Scale

The Scale widget is used whenever we want to select a specific value from a range of values. It provides a sliding bar through which we can select the values by sliding from left to right or top to bottom depending upon the orientation of our sliding bar.

### Methods in Scale

| **Methods** | **Uses** |
| ----------- | -------- |
| **set(value)** | Used for setting up the values of the scale |
| **get()** | Returns the value of the scale from selected |

### Implementation of Scales

1. **Horizontal Scale** : This procedure is been used in order to implement the Horizontal Scale properly in the main window designed for solving particular problem with the help of GUI Interface.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 3,relief = 'groove')                    # frame established
frm1.pack(padx = 2,pady = 3)                                        # frame packed

var1 = tk.DoubleVar()                                               # variable for scale's value

# Implementation of scale
scl1 = tk.Scale(frm1,variable = var1,from_ = 1,to = 100,orient = tk.HORIZONTAL)         # Scale Established
scl1.pack(padx = 2,pady = 3)                                                            # Scale packed

lb1 = tk.Label(frm1,text = 'Horizontal Scale',font = ('Fira Code',12))                  # label for Scale
lb1.pack(padx = 2,pady = 3)                                                             # label packed

# Method for getting the value on click
def showval():
    set1 = "Horizontal Scale value : " + str(var1.get())
    lb2.coonfig(text = set1,font = ('Fira Code',9))

lb2 = tk.Label(frm1)                                                                    # label for value
lb2.pack(padx = 2,pady = 3)                                                             # label packed

btn1 = tk.Button(frm1,text = 'Display Value',command = showval)                         # Button for value
btn1.pack(padx = 2,pady = 3)
```

2. **Vertical Scale** : This procedure is been used for implementing a Vertical Scale in the window for scaling or selecting a particular value in the GUI Interface for selection, further concept will be explained with the help of code given below.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 3,relief = 'groove')                    # frame established
frm1.pack(padx = 2,pady = 3)                                        # frame packed

var1 = tk.DoubleVar()                                               # variable for scale's value

# Implementation of scale
scl1 = tk.Scale(frm1,variable = var1,from_ = 1,to = 100,orient = tk.VERTICAL)           # Scale Established
scl1.pack(padx = 2,pady = 3)                                                            # Scale packed

lb1 = tk.Label(frm1,text = 'Vertical Scale',font = ('Fira Code',12))                    # label for Scale
lb1.pack(padx = 2,pady = 3)                                                             # label packed

# Method for getting the value on click
def showval():
    set1 = "Vertical Scale value : " + str(var1.get())
    lb2.coonfig(text = set1,font = ('Fira Code',9))

lb2 = tk.Label(frm1)                                                                    # label for value
lb2.pack(padx = 2,pady = 3)                                                             # label packed

btn1 = tk.Button(frm1,text = 'Display Value',command = showval)                         # Button for value
btn1.pack(padx = 2,pady = 3)
```

## Tkinter Intermediate Widget - TopLevel

A Toplevel widget is used to create a window on top of all other windows. The Toplevel widget is used to provide some extra information to the user and also when our program deals with more than one application. These windows are directly organized and managed by the Window Manager and do not need to have any parent window associated with them every time.

### Common Methods of Toplevel

| **Method's Name** | **Uses** |
| ----------------- | -------- |
| **iconify()** | It helps the developer for turning a particular window into an icon |
| **deiconify()** | It helps to turn that particular window back into that particular icon |
| **state()** | It is used for getting the state of the window to be returned |
| **withdraw()** | It is used for removing the window from the screen |
| **title()** | It is used for defining the title of the window |
| **frame()** | It returns the window identifier which is system specific |

### Different Ways for Toplevel

1. **General Implementation** : This is a simple method or procedure to work on the Topleve Widget and is useful when we need to take work from more than one Window at a time in order to implement more work from the user. Further explanation is been given in the code below. This is simply used for creating more than one window at a time.

*Syntax Code :*

```python
lb1 = tk.Label(window,text = 'Main Window',font = ('Fira Code',10))                 # Label Established
lb1.pack(padx = 2,pady = 3)                                                         # Label packed

top1 = tk.Toplevel(window)
top1.title('Second Window')
top1.geometry('300x200')

btn1 = tk.Button(top,text = 'Close',command = top1.destroy)                         # Button for Closing Window
btn1.pack()                                                                         # Button packed

top1.mainloop()
```

2. **Generating Toplevel** : This is another method for the implementation of the Toplevel Widget for implementing more than one window, and in the similar way we can generate more than one window at a time.

*Syntax Code :*

```python
l1 = tk.Label(window,text = 'Main Window Label',font = ('Fira Code',10))            # Label Established
l1.pack()                                                                           # Label Packed

def cmd1():
    top1 = tk.Toplevel(window)
    top1.title('Second Window')
    top1.geometry('400x200')

    btn1 = tk.Button(top1,text = 'Close',command = top1.destroy)                    # Button For Closing Window
    btn1.pack(padx = 2,pady = 3)                                                    # Button Packed

    top1.mainloop()

btn1 = tk.Button(window,text = 'Open Another Window',command = cmd1)                # Open another window
btn1.pack(padx = 2,pady = 4)                                                        # Button Packed
```

## Tkinter Intermediate Widget - Message

Python offers multiple options for developing a GUI (Graphical User Interface). Out of all the GUI methods, Tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. 

Python with Tkinter is the fastest and easiest way to create GUI applications. Creating a GUI using Tkinter is an easy task. The Message widget is used to show the message to the user regarding the behavior of the python application. The message text contains more than one line.

### Different Implementation of Message

1. **General Implementation** : This is a general procedure for implementing the Message Widget in the Main GUI Window, it is been done with the help of tk Module. Further concept will be explained with the help of code given below.

*Syntax Code :*

```python
frm1 = tk.Frame(window,bd = 3,relief = 'groove')                                                        # frame Established
frm1.pack()

lb1 = tk.Label(frm1,text = 'Simple Label',font = ('Fira Code',10))                                      # Label Created
lb1.pack()

msg1 = tk.Message(frm1,text = 'This is a general Message in GUI Window',font = ('Fira Code'.12))        # Message in GUI
msg1.pack()
```

## Tkinter Intermediate Widget - MenuButton

The Menubutton widget can be defined as the drop-down menu that is shown to the user all the time. The Menubutton is used to implement various types of menus in the python application.

### Different Methods in MenuButton

1. **General Implementation** : This is an overall procedure for the implementation of MenuButton inside the main GUI Window regarding view and purpose for different methods for getting view from the user and developers.

*Syntax Code :*

```python
menubtn = tk.Menubutton(window,text = 'Menu')           # Menu Button Implementation
menubtn.menu = tk.Menu(menubtn)                         # Adding Menu Widget
menubtn['menu'] = menubtn

var1 = tk.IntVar()                                      # Variables for getting input regarding menu options
var2 = tk.IntVar()
var3 = tk.IntVar()

menubtn.menu.add_checkbutton(label = 'Label1',variable = var1)          # First Option
menubtn.menu.add_checkbutton(label = 'Label2',variable = var2)          # Second Option
menubtn.menu.add_checkbutton(label = 'Label3',variable = var3)          # Third Option

# Packing the Menu
menubtn.pack(padx = 2,pady = 3)
```