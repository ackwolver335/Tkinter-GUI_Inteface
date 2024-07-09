import tkinter as tk 
import tkinter.font as tkfont

from numpy import true_divide

w1 = tk.Tk()
w1.title('Font Editings')
w1.geometry('400x200')

# adding our personal designed fonts
normal_font = tkfont.Font(family = 'Fira Code',size = 12,weight = tkfont.NORMAL)            # adding normal font style

# Using it while creating different widgets
frm1 = tk.Frame(w1)
frm1.pack(padx = 2,pady = 3)

# Adding label for testing the designed fonts
lb1 = tk.Label(frm1,text = 'Label Containing Normal Font Format',font = normal_font)        # using normal font here
lb1.pack(padx = 2,pady = 3)

# another self designed font
font1 = tkfont.Font(family = 'Helvetica',size = 12,weight = 'bold')                         # adding bold font style

# adding another label for testing it
lb2 = tk.Label(frm1,text = 'This is another bold font varient',font = font1)
lb2.pack(padx = 2,pady = 3)

# adding another font varient
font2 = tkfont.Font(family = 'Arial',size = 12,slant = 'italic',underline = True)           # using underline and italic style together

# using it in another label
lb3 = tk.Label(frm1,text = 'This is another font varient with Arial Font Family',font = font2)
lb3.pack(padx = 2,pady = 3)

# Using the last one font which is Roman
font3 = tkfont.Font(family = 'Arial',size = 12,slant = 'roman')                             # using Roman Style Font Varient

# adding it to another label
lb4 = tk.Label(frm1,text = 'This is the Roman Style font varient',font = font3)
lb4.pack(padx = 2,pady = 3)

# adding methods for buttons
def method1():
    font3.config(size = font3.actual()['size'] + 1)

def method2():
    font3.config(size = max(8,font3.actual()['size'] - 1))

# adding button for increasing font size
btn1 = tk.Button(frm1,text = 'Increase Font Size',command = method1)                        # Button for increasing font size font3
btn1.pack(padx = 2,pady = 3)

# adding button for decreasing font size                                                    # Button for decreasing font size font3
btn2 = tk.Button(frm1,text = 'Decrease Font Size',command = method2)
btn2.pack(padx = 2,pady = 3)

w1.mainloop()