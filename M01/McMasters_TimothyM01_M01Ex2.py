# This program will calculate the total amount of a meal purchased at restaurant

userFoodCharge = float(input("Please enter the charge for the food: "))
# ^^^ This integar variable holds the input for the user's total charge for the food

eighteenPercentTip = float(.18 * userFoodCharge)
# ^^^ This integar variable calculates an 18 percent tip from the user's food charge

sevenPercentSales = float(.07 * userFoodCharge)
# ^^^This integar variable calculates 7 percent sales charge from the user's food charge

totalAmount = float(userFoodCharge + sevenPercentSales + eighteenPercentTip)
# ^^^ This integar variable calculates the total amount charged

print("The tip at 18 percent is", eighteenPercentTip,".")
print("The sales tax at 7 percent is", sevenPercentSales,".")
print("The total amount owed is", totalAmount,".")
