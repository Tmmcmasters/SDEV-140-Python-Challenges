from cgitb import text
from cmath import e
from tkinter import *

root = Tk()

blankOne = Label(root, text="           ")
blankTwo = Label(root, text="           ")
blankOne.grid(row=0, column=0)
blankTwo.grid(row=0, column=3)

labelOne = Label(root, text="Enter your number:")
labelOne.grid(row=0, column=1)

userInput = Entry(root, width=10, bg="grey", fg="white",borderwidth=2)
userInput.grid(row=0, column=2)
userInput.get()

def toFahrenheit():
    fahrenheit = (1.8 * float(userInput.get())) + 32
    outputStatement = "%s %f%s" % ("Converting to fahrenheit makes", fahrenheit, "°F" )
    fahrenheitOutput = Label(root, text = outputStatement)
    fahrenheitOutput.grid(row=3, column=0)
def toCelcius():
    celcius = (float(userInput.get()) - 32)*(5/9) 
    outputStatement = "%s %f%s" % ("Converting to celcius makes", celcius, "°C" )
    celciusOutput = Label(root, text = outputStatement)
    celciusOutput.grid(row=3, column=0)

toCelciusButton = Button(root, text="Convert to Celcius", bg="black", fg="white", borderwidth=2, command=toCelcius)
toFahrenheitButton = Button(root, text="Convert to Fahrenheit", bg="black", fg="white", borderwidth=2, command=toFahrenheit)
toCelciusButton.grid(row=2, column=1)
toFahrenheitButton.grid(row=2, column=2)


root.mainloop()