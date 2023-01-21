# The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:
# F = 1.8 * C + 32

# Where F is the Fahrenheit temperature and C is the Celsius temperature.

# In a .py file, create a variable and assign it an float representing a celsius temperature that is entered as user input(). 
# input()'s message should prompt the user to enter an float value.

# For this programming challenge, you will then write a function called fahrenheit that takes in an float representing a Celsius
# temperature as its argument.  The function will return the Fahrenheit equivalent temperature of that argument to 1 place after the decimal.

# At the end of your program, display the Fahrenheit equivalent in a print statement message formatted like so:
# "The Fahrenheit equivalent of [user entered float] degrees Celsius is [number returned by function]".

# To make sure that the function works, run your program multiple times and call the function on different user entered integer values 
# both negative and positive.

def celsius_to_fahrenheit(pCelcius):
    return 1.8 * pCelcius + 32

print("\n\n\n==== Celcius to Fahrenheit conversion ===\n\n")
celsius = float(input("Enter the temperature in Celcius: [float] "))

fahrenheit = round(celsius_to_fahrenheit(celsius), 1)
celsius = round(celsius, 1)

print("The tempeture " + str(celsius) + "°C is equivalent to " + str(fahrenheit) + "°F\n\n")

