# This program is meant to calculate the monthly taxes when the function is called. 

def monthlyTaxes ():
    totalSales = float(input("Enter your total sales for the month: "))
    stateTax = .05 * float(totalSales)
    countyTax = .025 * float(totalSales)
    totalTaxes = countyTax + stateTax
    print("Your state tax is", stateTax)
    print("Your county tax is", countyTax)
    print("Your total taxes are", totalTaxes)

# This function multiplies .05 on the user's total sales and then holds it in stateTax variable.
# This function also multiplies .025 on the user's total sales and then holds it in countyTax variable.
# This function adds countTax and StateTax to get the total amount of taxes and then holds it in the totalTaxes variable. 
# Finally it prints the stateTax, countyTax, and totalTaxes variables. 

monthlyTaxes()
