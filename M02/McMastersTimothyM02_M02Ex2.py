#This program is meant to allow the user to enter a non-negative integar and use a loop to calculate the factorial of the loop.

from itertools import count


userIntegar = int(input("Please enter a postive number: "))

#This takes the input from a user and holds it as a constant integar. 

countNumber = int(1)
holdingSolution = int(1)

#I declare the integar variables here. countNumber is meant to count upwards till it exceeds the userIntegar number. holdingSolution is meant to multiple against countNumber and hold the solution to the problem. 

while countNumber <= userIntegar:
        holdingSolution = holdingSolution * countNumber
        countNumber += 1

#The goal of this while statement is to determine the factorial of userIntegar. 

print("The factorial of", userIntegar,"is", holdingSolution, ".")

#This last print statement outputs the intital number and the factorial solution. 

