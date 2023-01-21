# elif is equivalent to "else if"

user_num = int(input("Please enter an integer: "))

if user_num < 0:
    print("The number you entered is negative")
elif user_num == 0:
    print("The number you entered is ZERO")
elif 0 < user_num <= 100:
    print("The number you entered is between 1 and 100")
else:
    print("The number you entered is greather than 100!")

