def example():
    print("This is a function")

example()

def function_name(p1, p2, p3):
    print(p1 + str(2) + p3)


first_str = "The number "
function_name(first_str, 5, " is a string")


def default_example(num1=7, num2=8):
    print(num1 * num2)

default_example()
default_example(2,3)
default_example(4)

def return_example(num1=6, num2=4):
    return num1 * num2

value1 = return_example(8,9)
print(value1)
