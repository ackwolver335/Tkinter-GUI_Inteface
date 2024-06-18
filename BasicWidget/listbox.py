import tkinter as tk

w1 = tk.Tk()
w1.title("ListBox Widget")
w1.geometry("400x300")

# Creating a frame first
frame1 = tk.Frame(w1,bg = "lightblue",bd = 3,relief = 'ridge')
frame1.pack(padx = 3,pady = 5)

lb1 = tk.Listbox(frame1,height = 2,width = 15,bg = "lightgreen",activestyle = 'dotbox',fg = "blue")

# inserting elements
lb1.insert(1,"Python")
lb1.insert(2,"Java")
lb1.insert(3,"C++")
lb1.insert(4,"HTML")
lb1.insert(5,"CSS")

lb1.pack(padx = 2,pady = 3,side = 'left',fill = 'both')         # packing for getting final output

# adding scrollbar to it
scrollbr1 = tk.Scrollbar(frame1)
scrollbr1.pack(side = 'right',fill = 'both')

lb1.config(yscrollcommand = scrollbr1.set)                      # Setting List configuration
scrollbr1.config(command = lb1.yview)                           # Setting Scrollbar Configuration

# Selecting Multiple Items
lb2 = tk.Listbox(frame1,bg = "lightgreen",activestyle = 'dotbox',selectmode = tk.MULTIPLE)
lb2.pack(padx = 2,pady = 3)

# creating list for adding elements
data = ['Apple','Orange','Mango','Banana']

for i in data:
    count = 1
    lb2.insert(count,i)
    count += 1

def command1():                                 # Method for first Button command
    selected_one = lb2.curselection()
    for selected in selected_one[::-1]:
        print(selected)
        lb2.delete(selected)
    
def command2():
    for i in lb2.curselection():
        print(lb2.get(i))

# Creating a Button to delete the list elements
btn1 = tk.Button(w1,text = "Delete Elements",command = command1)
btn1.pack(padx = 2,pady = 3)

# Creating another button for getting selected values
btn2 = tk.Button(w1,text = "Print Selected Values",command = command2)
btn2.pack(padx = 2,pady = 3)

w1.mainloop()