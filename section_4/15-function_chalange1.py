# Do all of this in a .py file in Pycharm.

# For this programming challenge, you will be creating a function that calculates the volume of a rectangular prism 
# in cubic feet.  The formula to find the volume of a rectangular prism is V = l * w * h where l, w, and h are length, 
# width, and height, respectively.

# First, create three variables representing length, width, and height.   Assign each of them an integer as user input 
# using the input() function and int().

# Next, create a function to calculate the volume of the rectangular prism.  It should have 3 parameters representing length,
# width, and height and return the volume of a rectangular prism calculated using those 3 parameters.

# Finally, use print() to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." 
# in the output.  You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.

def prism_volume(pL, pW, pH):
    return pL * pW * pH


print("\n\n=== Prism Volume Calculation ===")
length = float(input("Enter the Length of the prism: "))
width = float(input("Enter the Width of the prism: "))
height = float(input("Enter the Height of the prism: "))
volume = prism_volume(length, width, height)

print("The volume of the prism is: " + str(volume))
print("\n\n\n")
