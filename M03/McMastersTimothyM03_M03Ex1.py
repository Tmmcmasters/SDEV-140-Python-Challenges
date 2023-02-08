#This program is meant to calculate the sum from a series of single digit numbers without spaces between them. 


# This takes the input from the user
print(" ")
print("Please enter a series of single digit numbers without any spaces between them.")
print("Ex: 132115")
numberInput = (input("Enter here: "))

# This statement will ensure that the user entered the correct type of input.
if numberInput.isdigit():
    print("I like those numbers!!!")
else:
    while numberInput.isdigit() == False:
        print(" ")
        print("The provided input was not a number.")
        print("Please enter a series of single digit numbers without any spaces between them.")
        print("Ex: 132115")
        numberInput = (input("Enter here: "))


# I declare the main variables here that will be included in my while loop
lengthOfInput = int(len(numberInput))
sumOutput = int(0)
loopCounter = int(0)

# This is the loop that calculates the sum of the numbers inputed
while loopCounter < lengthOfInput:
    sumOutput += int(numberInput[loopCounter])
    loopCounter += 1

# The ouput statement that also includes a space for better readibility
print(" ")
print("The sum of the numbers you input are", sumOutput)


