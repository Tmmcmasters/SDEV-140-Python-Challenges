# This program is meant to find all the prime numbers from 2 through the number input

numInput = input("Please enter a number that is greater than one: ")
numlist = []
constTwo = 2
#^^^^This takes the input and declares our list and constant integar two variable 

while constTwo <= int(numInput):
    numlist.append(constTwo)
    constTwo += 1

numLength = len(numlist)
# ^^^^^Our while loop that creates the list and declaring our variable for the length of our list for later use. 

def primeTester(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return "is not prime."
        return "is prime."
    else:
        return "is not prime." 
# ^^^^This is the function that determines if a number is prime or not. 

count = 0
while count < numLength:
    print(numlist[count], primeTester(numlist[count]))
    count += 1
# ^^^This is the while loop that runs all of the integars in the list through the primeTester function

