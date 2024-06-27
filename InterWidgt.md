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