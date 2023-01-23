# .add()

scifi = { "star trek", "star wars", "halo" }
scifi.add("mass effect")
print(scifi)

scifi.add("mass effect")
print(scifi)

# .remove()

fruits = { "apple", "orange", "banana", "tomato" }
fruits.remove("tomato")
print(fruits)

# fruits.remove("pear") => will cause an error message, cause "pear" isn't in the list
# print(fruits)

fruits.discard("pear") # error don't occurs
print(fruits)

fruits.discard("apple")
print(fruits)

# .copy()

moutains = { "Everest", "Kilimanjaro", "Fuji" }
copied_set = moutains.copy()

# .union()

set_1 = { 1, 2, 3, 4, 5, 6, 7 }
set_2 = { 6, 7, 8, 9, 10 }
set_3 = set_1.union(set_2)
# (alternative)
# set_3 = set_1 | set_2

print(set_1)
print(set_2)
print(set_3)

# .intersection()

set_4 = set_1.intersection(set_2)
# (alternative)
# set_4 = set_1 & set_2
print(set_4)

# .subtraction() and .difference()

set_5 = set_2 - set_1
print(set_5)

set_6 = set_1 - set_2
print(set_6)

set_7 = set_1.difference(set_2)
print(set_7)
