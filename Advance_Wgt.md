# 🚀 Tkinter Widget (Advance)

**Introduction** :- Tkinter is the most commonly used library for developing GUI (Graphical User Interface) in Python. It is a standard Python interface to the Tk GUI toolkit shipped with Python. As Tk and Tkinter are available on most of the Unix platforms as well as on the Windows system, developing GUI applications with Tkinter becomes the fastest and easiest.

**Some Needed** :- Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python Tkinter is the fastest and easiest way to create GUI applications. Creating a GUI using Tkinter is an easy task.

## 🛠 Advance Widget

There are various types of widgets available in Tkinter such as button, frame, label, menu, scrolledtext, canvas and many more. A widget is an element that provides various controls. ScrolledText widget is a text widget with a scroll bar. 

### ⚡️ Overview Table

| **Widgets** | **Uses** |
| :---------- | :------- |
| **ScrolledText** | Used for creating text widget together with the built-in Scrollbars |
| **Treeview** | It is used for getting the hierarchical data in a tree-like structure. |
| **MessageBox** | Used for getting the dialog box displayed the warnings or messages,.etc |
| **Treeview Scrollbar** | Used for adding scrollbar to the Treeview |
| **Text** | It creates multiple line text input with advance editable capacities |

## Tkinter Advance Widget - ScrolledText

The tkinter.scrolledtext module provides the text widget along with a scroll bar. This widget helps the user enter multiple lines of text with convenience. Instead of adding a Scroll bar to a text widget, we can make use of a scrolledtext widget that helps to enter any number of lines of text.

### Different Implementation of ScrolledText

1. **Entry ScrolledText** : This is first procedure for the implementation of the ScrolledText Widget in Advance Widget Categories of Tkinter, in this we'll have some block with some property like of entry and scrollbar. Further explanation will be available with the help of code given below.

*Syntax Code :*

```python
import tkinter as tk
from tkinter import scrolledtext as st

frm1 = tk.Frame(w1,bd = 2,relief = 'groove')                    # frame for scrolledtext
frm1.pack(padx = 2,pady = 3)                                    # packing the frame

lb1 = tk.Label(frm1,text = 'ScrolledText Widget',font = ('Fira Code',12))       # label for Explanation
lb1.pack(padx = 2,pady = 3)                                                     # label packed

scrolldtxt1 = st.ScrolledText(frm1,wrap = tk.WORD,width = 20,height = 4,font = ('Fira Code',10))
scrolldtxt1.pack(padx = 2,pady = 3)
scrolldtxt1.focus()                             # for getting the focus on window
```

2. **ReadOnly ScrolledText** : This is another procedure that is used in order to create a readonly structure of the first one that is been explained above. Other properties are all same as mentioned above. Further explanation is been available in the code below.

*Syntax Code :*

```python
import tkinter as tk
from tkinter import scrolledtext as st

frm1 = tk.Frame(frm1,bd = 3,relief = 'ridge')                       # frame for scrolledtext established
frm1.pack(padx = 2,pady = 3)                                        # frame packed

lb1 = tk.Label(w1,text = 'Readable ScrolledText',font = ('Fira Code',12))           # label for it established
lb1.pack(padx = 2,pady = 3)                                                         # label packed

scrolldtxt1 = st.ScrolledText(frm1,wrap = tk.WORD,width = 30,height = 6,font = ('Fira Code',10))
scrolldtxt1.pack(padx = 2,pady = 3)

# inserting data into the ScrolledText Area
scrolldtxt1.insert(tk.INSERT,'This is the simple text\nAnd this is another line content')
scrolldtxt1.configure(state = 'disabled')
```

## Tkinter Advance Widget - Treeview

This widget is helpful in visualizing and permitting navigation over a hierarchy of items. It can display more than one feature of every item in the hierarchy. It can build a tree view as a user interface like in Windows explorer. Therefore, here we will use Tkinter in order to construct a hierarchical treeview in the Python GUI application. 

### General Code Implementation

In Treeview, this is the general implementation done with the help of Treeview() method of *ttk* Module in Tkinter Library and some of the methods like insert and move are used in order to properly implement the Treeview Widget in the Tkinter Window. Below we have one code example for its explanation.

*Syntax Code :*

```python
import tkinter.ttk as tk1

treeview = tk1.Treeview(window)                         # Treeview Implemented
treeview.pack(padx = 2,pady = 3)                        # Treeview packed

treeview.insert('',0,'item1',text = 'Data1')            # Inserting the Data Elements
treeview.insert('',1,'item1',text = 'Data2')
treeview.insert('',2,'item1',text = 'Data3')
treeview.insert('',3,'item1',text = 'Data4')

treeview.insert('item2','end','Part1',text = 'Data3')   # Inserting more than one attribute
treeview.insert('item2','end','Part1',text = 'Data3')
treeview.insert('item3','end','Part2',text = 'Data4')
treeview.insert('item3','end','Part2',text = 'Data4')
treeview.insert('item4','end','Part3',text = 'Data5')
treeview.insert('item4','end','Part3',text = 'Data5')

# Placing the items at the right side
treeview1.move('item2','item1',0)
treeview1.move('item3','item1',0)
treeview1.move('item4','item1',0)
```

## Tkinter Advance Widget - MessageBox

Python Tkinter – MessageBox Widget is used to display the message boxes in the python applications. This module is used to display a message using provides a number of functions.

### Different Available Methods

| **Method's Name** | **Uses** |
| ----------------- | -------- |
| **showinfo()** | It is used to show the message box regarding some relevant information to the user |
| **showwarning()** | It works similar to the *showinfo()* method that show information together with the Warning Icon |
| **showerror()** | It works simlar to other show methods together with the error symbol with the dialog box appeared |
| **askquestion()** | Used to ask question together by providing the multiple options in it |
| **askokcancel()** | It is used in order to check a confirmation regarding a particular question |
| **askyesno()** | As per the name of this method it is used in order to create a question diaglog and ask the answer in yes or no |
| **askretrycancel()** | It works regarding retry and cancel similar to other methods |

### Implementation of these methods

- Below we have a proper syntax and code regarding the Explanation of methods and proper code usage.

*Syntax Code :*

```python
from tkinter import messagebox as mgbx

mgbx1 = mgbx.showinfo('showinfo-Title','Data to be shown')
mgbx2 = mgbx.showwarning('showwarning-title','Warning Information')
mgbx3 = mgbx.showerror('showerror-Title','Error Warning Message')
mgbx4 = mgbx.askquestion('Question-title','Question text line ?')
mgbx5 = mgbx.askokcancel('Question-title','Question Main title')
mgbx6 = mgbx.askyesno('Question-Title','Finding the values ?')
mgbx7 = mgbx.askretrycancel('Recheck Question','Try Again ?')
```