import tkinter as tk 

# Adding Window
w1 = tk.Tk()
w1.title('Text Widget')
w1.geometry('500x300')

# Frame Widget for overall Bouded Implementation
frm1 = tk.Frame(w1,bd = 2,relief = 'raised')
frm1.pack(padx = 2,pady = 3)

# Implementing the Text Widget
t1 = tk.Text(frm1,height = 5,width = 30)
t1.pack(padx = 5,pady = 5)

# Label for General Information
lb1 = tk.Label(frm1,text = 'A General Example of Text Widget',font = ('Fira Code',10,'bold'))
lb1.pack(padx = 2,pady = 3)

# Data for the Text Widget
text_data = "A general text data for the Text Widget for adding in the Window's main frame for Text Widget Example !"

# Adding data to the Text Widget
t1.insert(tk.END,text_data)

# Adding Button for closing the Window
btn1 = tk.Button(frm1,text = 'Close Window',font = ('Fira Code',10,'bold'))
btn1.pack(padx = 2,pady = 3)

w1.mainloop()