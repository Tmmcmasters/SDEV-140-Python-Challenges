# This program converts celsius temperatures to Fahrenheit temperatures

userCelsius = float(input("Please enter the celsius temperature: "))
# ^^^ This integar variable takes the input from the user of the celsius temperature.

celsiusToFahrenheit = float((1.8 * userCelsius) + 32)
# ^^^ This integar constant holds the equation to convert celsisu to Fahrenheit

finalOutput = str(print(userCelsius,"°C to Fahrenheit is",celsiusToFahrenheit,"°F."))
# ^^^ This string constant holds the final output statement

finalOutput # <----- This declares the print statement
