# Programming Challenge: Find The Number of Characters in A String
# In a .py file, write a program which calculates the number of characters in a string.

# The string should be entered using input() and assigned to a variable. 

# Use print() twice at the end of your program.  The first print() will print the string 
# that the user entered and the second print() will display the number of characters in 
# the string.

# For example, if the user entered the string "hello world", the number of characters would be 11.

user_string = input("Please, enter a phrase: ")

couter = 0
for letter in user_string:
    couter += 1

print("The phrase you entered, has " + str(couter) + " characters length")

