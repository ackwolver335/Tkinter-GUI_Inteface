import tkinter as tk 
import tkinter.ttk as ttk1

w1 = tk.Tk()
w1.title("Combobox Widget")
w1.geometry('500x200')

# Adding a particular frame for Combobox
frm1 = tk.Frame(w1,bd = 3,relief = 'groove')
frm1.pack(padx = 2,pady = 5)

# String for taking selected output
str1 = tk.StringVar()

# combobox
cb1 = ttk1.Combobox(frm1,width = 30,textvariable = str1)

l1 = ['January','February','March','April','May','June','July','August','September','Octuber','November','December']
cb1['values'] = l1                              # Adding list for it
cb1.pack(padx = 4,pady = 5)
cb1.current(0)                                  # cb1.current() = Show nothing in the Box

# Getting Index of selected One
frm2 = tk.Frame(w1,bd = 2,relief = 'raised')
frm2.pack(padx = 2,pady = 10)

def getindex(*args):                            # method for getting current position
    if str2.get() >= str(0):
        lb1 = tk.Label(frm2,text = "The Value at index " + str(cb2.current()) + " is " + str(str2.get()))
        lb1.pack(padx = 2,pady = 3)                 # Using label

def clear_all():
    cb2.set('')

str2 = tk.StringVar()                           # String Var for Combobox value
cb2 = ttk1.Combobox(frm2,textvariable = str2)
cb2['values'] = l1                              # Using the same list
cb2.current(0)                                  # setting default value
cb2['state'] = 'readonly'
cb2.pack(padx = 4,pady = 5)

str2.trace_add('write',getindex)                # tracing selected element in combobox

btn1 = tk.Button(w1,text = 'Clear All',command = clear_all)
btn1.pack(padx = 2,pady = 3)

# Autocomplete Combobox
frm3 = tk.Frame(w1,bd = 2,relief = 'groove')                # Frame for Autocomplete Combobox
frm3.pack(padx = 2,pady = 3)

l2 = ['C++','Python','PHP','Perl','Ruby','Java']            # Data driver

# method for Entry
def checkkey(event):
    v1 = event.widget.get()         # retrieving data

    if v1 == '':
        data = l2                   # initiating data
    else:
        data = []
        for item in l2:             # checking data
            if v1.lower() in item.lower():
                data.append(item)

    update(data)                    # for updating data in the listbox

def update(data):
    list1.delete(0,'end')           # clearing preview data
    for item in data:
        list1.insert('end',item)    # putting new data

# entry box
e1 = tk.Entry(frm3)
e1.pack(padx = 2,pady = 3)
e1.bind('<KeyRelease>',checkkey)

# Listbox for it
list1 = tk.Listbox(frm3)
list1.pack(padx = 2,pady = 3)
update(l2)

w1.mainloop()