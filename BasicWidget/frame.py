import tkinter as tk

w1 = tk.Tk()
w1.title("Frame Widgets")
w1.geometry("500x400")
w1.resizable(False,False)

# Frame
frame1 = tk.Frame(w1,bg = "#00FE00",bd = 4,height = 100,width = 200,highlightbackground = "red",highlightcolor = "black",highlightthickness = 2,relief = "ridge")
frame1.pack(padx = 3,pady = 5)

# Label inside Frame
l1 = tk.Label(frame1,text = "Coding Needs",font = ('Fira Code',10),bg = "lightblue",bd = 3,relief = "groove",height = 5,width = 20)
l1.pack(padx = 2,pady = 3)

l2 = tk.Label(frame1,text = "Ack Wolver",font = ("Fira Code",9),bg = "red",fg = "yellow")
l2.pack(padx = 2,pady = 3)



w1.mainloop()