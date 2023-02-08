#This program will take the input from a user of how many random numbers they would like to generate. It will then output a set of random numbers(ranging from 1-500) in a new file.  


# This will import the random module and open the file that I will use to write the data. 
from fileinput import close
import random
fileOpener = open("McMastersTimothyM03_M03Ex2.txt", 'w')

# This takes the input for the amount of numbers the user will enter. 
inputRange = int(input("Please enter the amount of random numbers you want here: "))

# This is the for loop that writes the data to the folder and also prints the same set of random numbers to the console
for count in range(inputRange):
    number = random.randint(1, 500)
    fileOpener.write(str(number) + '\n')
    print(int(number), '\n')

# This will close the file with the new numbers in it
fileOpener.close()

