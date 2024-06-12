# Tkinter Widgets (Basics)

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