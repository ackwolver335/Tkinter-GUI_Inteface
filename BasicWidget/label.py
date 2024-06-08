import tkinter as tk

# Creating window
window = tk.Tk()
window.geometry("400x400")
window.title("Label Categories")

# First Label
l1 = tk.Label(window,text = "Text on Label")
l1.pack()

window.mainloop()