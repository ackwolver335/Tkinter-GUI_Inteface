import tkinter as tk
import tkinter.messagebox as mg

w1 = tk.Tk()
w1.title('Message Box Widget')
w1.geometry('500x400')

frm1 = tk.Frame(w1,bd = 2,relief = 'groove')
frm1.pack(padx = 2,pady = 3)

mg1 = mg.showinfo('showinfo','Information')                                     # Show Information
mg2 = mg.showwarning('showwarning','This is a warning message')                 # Show Warning
mg3 = mg.showerror('showerror','This is an error message')                      # Show Error

mg4 = mg.askquestion('askQuestion','Are you sure ?')                            # Ask Question
mg5 = mg.askokcancel('askokcancel','Choose one ?')                              # Ask ok or Cancel
mg6 = mg.askyesno('askyesno','Choose Either Yes or No ?')                       # Ask yes OR no
mg7 = mg.askretrycancel('retrycancel','Either Retry or Cancel')                 # Retry or Cancel

w1.mainloop()