def guessingGame ():
    import random
    randomNumber = random.randrange(1, 100)
    # I imported the random module to come up with the random number between 1 and 100. I did this using .randrange 
    userGuess = 0.0
    userGuess = float(input('Please guess my random number: '))
    numberGuesses = 1
    # ^^^^ I declared the variables and take the first user guess.
    while userGuess != randomNumber: # I use this while loop to hold the if statements till the user guess the right number
        if userGuess > randomNumber:
            userGuess = float(input("Too high, Try again: "))
            numberGuesses += 1
        elif userGuess < randomNumber:
            userGuess = float(input("Too low, Try again: "))
            numberGuesses += 1
        else:
            numberGuesses += 1
            
    print("Congratulations!! :D  You guessed my number correctly!")
    print("It took you", numberGuesses, "try(ies) to guess my number.")
    print("Let's start over!")
    guessingGame()
    # Finally I printed the number of tries, and after they break the while loop that means that they guess the correct number, so I congradulate them and recall the function.

guessingGame()
    

        