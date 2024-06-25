import tkinter as tk 

w1 = tk.Tk()                    # main window
w1.title("Canvas Widgets")
w1.geometry('500x300')

frm1 = tk.Frame(w1,bd = 2,relief = 'groove')
frm1.pack(padx = 2,pady = 3)

c1 = tk.Canvas(frm1,bg = 'lightblue',height = 250,width = 300)                          # canva frame here first 1
c1.pack(padx = 2,pady  = 3)

line1 = c1.create_line(108,110,90,210,fill = 'red')                                     # line creation
arc1 = c1.create_arc(180,150,80,210,start = 0,extent = 200,fill = 'red')                # arc creation
oval1 = c1.create_oval(80,30,140,150,fill = 'Green')                                    # oval creation
rect1 = c1.create_rectangle(20,40,100,120,fill = 'pink')

# creating another frame for different Widget with different lines
frm2 = tk.Frame(w1,bd = 3,relief = 'ridge')                                             # another frame
frm2.pack(padx = 2,pady = 3)

c2 = tk.Canvas(frm2,bg = 'lightgreen',height = 200,width = 350)                         # canva frame here first 2
c2.pack(fill = tk.BOTH,expand = True)

# adding different formats of lines
lin1 = c2.create_line(15,25,200,25)                         # straight forward line
lin2 = c2.create_line(300,35,300,200,dash = (5,2))          # straight vertical line
lin3 = c2.create_line(55,85,155,85,105,180,55,85)           # straight triangle line

w1.mainloop()