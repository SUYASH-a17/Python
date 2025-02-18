from tkinter import *

window = Tk()

def from_kg():
    gms = float(e2_value.get())*1000
    lbs = float(e2_value.get())*2.2
    ozs = float(e2_value.get())*35.2
    gm.delete('1.0', END)
    gm.insert(END,gms)
    lb.delete('1.0', END)
    lb.insert(END,lbs)
    oz.delete('1.0', END)
    oz.insert(END,ozs)
    
e1=Label(window,text="Kg")
e1.grid(row=0,column=1) # The Label is placed in position 0, 0 in the window
 
e2_value=StringVar()  # Create a special StringVar object
e2=Entry(window,textvariable=e2_value)  # Create an Entry box for users to enter the value
e2.grid(row=0,column=0)
 
# Create a button widget
# The from_kg() function is called when the button is pushed
b1=Button(window,text="Convert",command=from_kg)
b1.grid(row=0,column=2)
 
# Create three empty text boxes, t1, t2, and t3
gm=Text(window,height=1,width=20)
gm.grid(row=1,column=0)
 
lb=Text(window,height=1,width=20)
lb.grid(row=1,column=1)
 
oz=Text(window,height=1,width=20)
oz.grid(row=1,column=2)
 
# This makes sure to keep the main window open
window.mainloop()
