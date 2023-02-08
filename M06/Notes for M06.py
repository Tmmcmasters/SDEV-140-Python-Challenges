from cmath import e
from tkinter import *

root = Tk()

# Function for the button
def myClick():
    myLabel3 = Label(root, text="Look! I clicked a Button!!")
    myLabel3.grid(row=3, column=0)
  
# Creating a button widget
myButton = Button(root, text="Click me", padx=50, command=myClick, fg="blue", bg="grey")
myButton.grid(row=2, column=0)

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is John Elder")

# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

# Creating input widget
e = Entry(root, width=10, bg="black", fg="white", borderwidth=5)
e.grid(row=2, column=4)
e.get() # <<== This takes the information from the input field

#
def mySecondClick():
    hello = "% s % s" % ("Hello", e.get())
    myLabel4 = Label(root, text=hello)
    myLabel4.grid(row=4, column=4) 

myButtonTwo = Button(root, text="Enter your name", padx=50, command=mySecondClick)
myButtonTwo.grid(row=3, column=4)

root.mainloop()