import tkinter as tk
import tkinter.ttk as tk1

w1 = tk.Tk()
w1.title("Frame Widgets")
w1.geometry("400x300")
# w1.overrideredirect(True)         # Used for creating frameless window

# Frame
frame1 = tk.Frame(w1,bg = "#00FE00",bd = 4,height = 100,width = 200,highlightbackground = "red",highlightcolor = "black",highlightthickness = 2,relief = "ridge")
frame1.pack(padx = 3,pady = 5)

# Label inside Frame
l1 = tk.Label(frame1,text = "Coding Needs",font = ('Fira Code',10),bg = "lightblue",bd = 3,relief = "groove",height = 5,width = 20)
l1.pack(padx = 2,pady = 3)

l2 = tk.Label(frame1,text = "Ack Wolver",font = ("Fira Code",9),bg = "red",fg = "yellow")
l2.pack(padx = 2,pady = 3)

# Scrollable Frames
h1 = tk.Scrollbar(w1,orient = "horizontal")              # Horizontal Scrollbar
h1.pack(side = "bottom",fill = "x")

v1 = tk.Scrollbar(w1)                                   # Vertical Scrollbar
v1.pack(side = "right",fill = "y")

# Adding Text
t1 = tk.Text(w1,width = 10,height = 10,wrap = "none",xscrollcommand = h1.set,yscrollcommand = v1.set)

# Inserting Data
for i in range(10):
    t1.insert(tk.END,"Data Added\n")

t1.pack(side = "top",fill = "x")

h1.config(command = t1.xview)
v1.config(command = t1.yview)

# Changing Label Frame Border
# Adding Style Method/Functions
st1 = tk1.Style()

# Using already defined theme
st1.theme_use("clam")
st1.configure("TLabelFrame",bordercolor = "red")

lframe1 = tk1.LabelFrame(w1,text = "Frame1")
lframe1.pack(padx = 30,pady = 30)

label1 = tk.Label(lframe1,text = "First One")
label1.pack()

w1.mainloop()