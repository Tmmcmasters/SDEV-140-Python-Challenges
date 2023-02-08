#This program will detmerine the secondary color based off of two primary colors that the user inputs. 

print("There are three primary colors; red, blue, and yellow")
userColorInputOne = str.lower(input("Please enter one primary color: ")).strip()
userColorInputTwo = str.lower(input("Please enter another primary color: ")).strip()

#I printed to the console the three primary colors to ensure the user knows what the three primary colors are. I then prompted them to enter both two primary colors and stored them in two string constants. I also ensure that case sensitivity was a non issue by using the method str.lower. I wanted to make sure that trailing whitespaces were irreveleant as well, so I added the method .strip

if userColorInputOne == "red" and userColorInputTwo == "blue" or userColorInputOne == "blue" and userColorInputTwo == "red":
    print("These two colors combined make a secondary color which is purple.")
elif userColorInputOne == "red" and userColorInputTwo == "yellow" or userColorInputOne == "yellow" and userColorInputTwo == "red":
    print("These two colors combined make a secondary color which is orange.")
elif userColorInputOne == "blue" and userColorInputTwo == "yellow" or userColorInputOne == "yellow" and userColorInputTwo == "blue":
    print("These two colors combined make a secondary color which is green.")
elif userColorInputOne == userColorInputTwo:
    print("These two colors do not make a secondary color, but just make their original color which is ", userColorInputOne,".")
else:
    print("Uh uh oh :(((((((. There is an error! I don't think you entered a primary.")

# In this strand of if/and statements, I determined what two colors the user inputed and I then proceeded to output the resulting secondary color. I also ensured that if the user entered the same primary colors, they would be returned the same primary color. If the user did not entere a primary color at all, then they would result in an error message.