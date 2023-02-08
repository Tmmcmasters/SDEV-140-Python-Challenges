#This program is meant to sort the top three priced items from data in a menu.


myDictionary = {
    'Apple': 0.50,
     'Banana': 0.20,
      'Mango': 0.99,
       'Coconut': 2.99,
        'Pineapple': 3.99,
        'Grapefruit': 3.86,
        'Dragonfruit':3.25
        }
# ^^^^^^^ Created Dictionary with the sample data. 
# This is where you can change the dictionary data which will then be used to ouput. 

theValues = list(myDictionary.values())
theValues.sort(reverse=True)
val_list = list(myDictionary.values())
key_list = list(myDictionary.keys())
# I make a list with the dictionary which will the sort the values in reverse order so; most expensive to least expensive. I then create two constants which will hold the list method of the different dictionary values and keys. 


count = 0
while count < 3:
    position = val_list.index(theValues[count])
    print(key_list[position], theValues[count])
    count += 1
# This is a while loop that will print the top three price menu items in the shop with a position variable that will index with for the values which will then be printed in the reverse order that I had. 





