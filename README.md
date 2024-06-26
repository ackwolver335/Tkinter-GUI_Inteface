# 🚀 Tkinter - GUI Interface

It represents all the Basics and Elementary concepts of GUI Interface of Python Tkinter, and contains all the needed code concepts for proper implementation and creation of a Basic GUI Application.

This GitHub repository features a collection of Python projects utilizing Tkinter for graphical user interfaces. It includes various examples, from simple widgets to complex applications, demonstrating Tkinter's capabilities. Ideal for developers seeking practical, hands-on experience with GUI development in Python. Comprehensive documentation and source code are provided.

## Getting Started with it

Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python Tkinter is the fastest and easiest way to create GUI applications. Creating a GUI using Tkinter is an easy task.

## 🛠 Skills Used

- *[Python Setup](https://www.python.org/downloads/)*
- *[Documentation](https://www.python.org/doc/)*

## Installing Tkinter

Below we have the command for intalling tkinter in Windows using this command in CMD

```
pip install tkinter
```

For Testing whether the Module is been installed properly or not !

```python
import tkinter as tk
tk._test()
```

Initiating the Window with **Tk()**

To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. To change the name of the window, you can change the className to the desired one.

Ending it the **mainloop()** Method

There is a method known by the name mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur, and process the event as long as the window is not closed.

General Syntax Code : 

```python
import tkinter as tk                    # Module Imported
window = tk.Tk()                        # Main window Initiated
"""
widgets........
frames.........
"""
window.mainloop()
```

## Basic Widgets for GUI

Creating Interactive applications using Tkinter’s, using basic widgets. From simple frames and labels to more complex elements like scrollable frames and treeviews, we’ll cover a wide range of widgets and their customization options.

| **Widgets** | **Uses** |
|:----------- | :------- |
| **Label** | Used for getting the static text and images to be displayed |
| **Button** | Used for creating different buttons containing different purposes or methods |
| **Entry** | Allow the user for creating input places for getting single-line text input from the user |
| **Frame** | Used for creating frame or like a container for particular purpose |
| **Checkbutton** | Creates the checkbox and allow multiple input choices from the user |
| **Radiobutton** | Used in the case of creating a single choice in the form of single input from the user |
| **Listbox** | Used for creating multiple list options |
| **Scrollbar** | Creates a Scrollbar for providing this feature in the window |
| **Menu** | Used for creating a Menu Options as a general taskbar for Main Window |
| **Canvas** | Used for creating graphics and all canvas elements |

## Intermediate Widget for GUI

Creating more Interactive different tools inside your owned application or designed application with the help of different intermediate widgets like Combobox, Scale, Toplevel, message box. These customization tools will surely give you a new look to the Designed Application.

| **Widgets** | **Uses** |
| :---------- | :------- |
| **Combobox** | It provides a proper dropdown list of options with editable entry |
| **Scale** | It is been created in order to select a value within a particular range |
| **TopLevel** | Used for creating an additional window or dialog box |
| **Message** | Used for displaying a simple messagebox or notification |
| **MenuButton** | Creates a Button for opening the menu of the Window |
| **ProgressBar** | Used for creating a proper progress related to a particular task |
| **SpinBox** | Provides a numerical input and output options to be shown a interact using Arrow Keys |