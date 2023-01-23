# Programming Challenge: Factorial
# Create a function which takes one positive integer as its input and returns its factorial.

# To make sure that your function works correctly, you should call it with the inputs 3, 4, 
# and 5 and print what is returned by those calls.  For those inputs, you should get 6, 24, 
# and 120, respectively.

def factorial(fac_num):
    if (fac_num <= 0):
        raise Exception("The number must be a NON ZERO POSITIVE number!")

    factorial = 1
    for num in range(fac_num, 0, -1):
        factorial *= num

    return factorial


def output(fac_num):
    print("The factorial of " + str(fac_num) + " is " + str(factorial(fac_num)))


output(3)
output(4)
output(5)

output(10)

output(100)

