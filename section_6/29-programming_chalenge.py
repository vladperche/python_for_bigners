# Programming Challenge: Sum of Numbers From A Positive Integer
# Write a program which gets two positive integers from a user using input() and assigns it to variables.

# The program should then use a while loop to get the sum of all of the integers between the integers that was entered by the user.

print("\n\n=== Sum of sequence ===")

start = int(input("Enter the start of the sequence: "))
finish = int(input("Enter the finish of the sequence: "))

sum = 0
counter = start
while counter <= finish:
    sum += counter
    counter += 1

print("\n\nThe sum of all numbers between " + str(start) + " and " + str(finish) + " is equal to " + str(sum))

