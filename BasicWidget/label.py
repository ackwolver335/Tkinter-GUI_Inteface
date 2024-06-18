import tkinter as tk

# Creating window
window = tk.Tk()
window.geometry("400x400")
window.title("Label Categories")

# defining function for method over labels
def command1():
    l5.config(text = "Border Label Changed")

# First Label
l1 = tk.Label(window,text = "Text on Label")
l1.pack()

# Label with anchor options
l2 = tk.Label(window,text = "Anchor Option",anchor = tk.CENTER)
l2.pack()

# Label with some Height and Width
l3 = tk.Label(window,text = "Spaced Label",height = 2,width = 10)
l3.pack()

# Background and Font Editing
l4 = tk.Label(window,text = "Edited",height = 2,width = 10,font = ("Fira Code",15),fg = "#2596be",bg = "yellow")
l4.pack()

# Border and Effects
l5 = tk.Label(window,text = "Border Effect",bg = "Green",fg = "white",borderwidth = 4,relief = "raised",padx = 5,pady = 5)
l5.pack()

# Changing Text of Label
b1 = tk.Button(window,text = "Change Border Text",borderwidth = 4,relief = 'groove',padx = 5,pady = 5,command = command1)
b1.pack()

# Setting position using place method
l6 = tk.Label(window,text = "New Label",borderwidth = 2,relief = "solid",padx = 4,pady = 4)
l6.place(x = 20,y = 100)

# Another Positioning Methods
l7 = tk.Label(window,text = "Another Positioning",borderwidth = 4)
l7.place(relx = 0.5,rely = 0.5)

# Label Frame
lframe1 = tk.LabelFrame(window,text = "Label Frame",padx = 5,pady = 5)
lframe1.pack(expand = True,fill = "both")

# Labels for labelFrame
lf1 = tk.Label(lframe1,text = "First One")
lf1.place(x = 5,y = 5)
lf2 = tk.Label(lframe1,text = "Second One")
lf2.place(x = 5,y= 20)
lf3 = tk.Label(lframe1,text = "Third One")
lf3.place(x = 5,y = 35)

window.mainloop()