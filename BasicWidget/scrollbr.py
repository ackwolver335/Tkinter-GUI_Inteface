import tkinter as tk

w1 = tk.Tk()
w1.title("Scrollbar Widgets")
w1.geometry("250x300")

# Adding label
l1 = tk.Label(w1,text = "Scrollbar Widget",font = ('Fira Code',12),bd = 3,relief = 'ridge')
l1.pack(padx = 2,pady = 3)

# Adding scrollbar
scrlbr1 = tk.Scrollbar(w1)
scrlbr1.pack(side = 'right',fill = 'y')

# adding listbox for getting the phase ready
list1 = tk.Listbox(w1,yscrollcommand = scrlbr1.set,)

for i in range(1,61):
    list1.insert(i,"Geek" + str(i))

list1.pack(side = 'left',fill = "both",padx = 2,pady = 3)

# adding configuration to the scrollbar
scrlbr1.config(command = list1.yview)

# Another format of adding both side of Scrollbar inside the frame
frame1 = tk.Frame(w1,bd = 3,height = 10,width = 300,relief = 'groove')
frame1.pack(padx = 2,pady = 3)

# data to be placed in both vertical format
data_hz = ("A B C D E F G H J K L M N O P Q R S T U V W X Y Z")
data_vt = ("a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nu\nv\nw\nx\ny")

# adding scrollbar data here
svbar = tk.Scrollbar(frame1)
svbar.pack(side = 'right',fill = 'y')

shbar = tk.Scrollbar(w1,orient = tk.HORIZONTAL)
shbar.pack(side = 'bottom',fill = 'x')

# creating two different text box
textbx = tk.Text(frame1,height = 400,width = 400,yscrollcommand = svbar.set,xscrollcommand = shbar.set,wrap = 'none')
textbx = tk.Text(frame1,height = 400,width = 400,yscrollcommand = svbar.set,xscrollcommand = shbar.set,wrap = 'none')

# packing them all
textbx.pack(expand = 0,fill = 'both')
textbx.pack(expand = 0,fill = 'both')

# Inserting them in the frame
textbx.insert(tk.END,data_hz)
textbx.insert(tk.END,data_vt)

# changing its configuration for it
shbar.config(command = textbx.xview)
svbar.config(command = textbx.yview)

w1.mainloop()