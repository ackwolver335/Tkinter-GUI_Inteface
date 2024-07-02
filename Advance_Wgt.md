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