# accessing elements by its index number (0 based)

index_example = [ "carpet", "hardwood", "linoleum" ]
print(index_example[1])

list_of_lists = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
print(list_of_lists[2][1])

# negative index
# will starts from the end of the list, and count's backwards

print(index_example[-1]) # takes the last item
print(index_example[-2]) # takes the item before the last...

# items accessed by index in expressions

mixed = [ False, 365, 4.24, "this is a string" ]

print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example of too many times")

# list slicing
# just like strings

sliced = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

print(sliced[:4]) # begining of the list
print(sliced[3:8]) # middle of the list
print(sliced[6:]) # end of the list, starting in the index item number 6

# reassing an item

example_reassign = [ 2, 4, 6, 8, 0 ]
print(example_reassign)

example_reassign[4] = 10 # replace a single element
print(example_reassign)

example_reassign[1:4] = [ 3, 2, 1 ]
print(example_reassign)
