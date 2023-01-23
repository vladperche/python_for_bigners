# delete itens from a list
# del remove item based on the index

planets = [ "pluto", "mars" , "earth", "venus" ]
del planets[0]

print(planets)

# remove method
# remove will remove item based on it's content

planets.remove("mars")
print(planets)

# will cause an error, because "uranus" isn't in the list
#planets.remove("uranus")

colors = [ "blue", "red", "white", "blue", "orange", "blue" ]
colors.remove("blue")
print(colors)

# append
# adds an element at the end of the list

pets = [ "cat", "dog", "parrot" ]
print(pets)

pets.append("fish")
print(pets)

# insert
# adds an element in any specific position

pets.insert(1, "turtle")
print(pets)

# sort
# don't work in mixed lists

num_list = [ 2.718, 4, -19, 10000, 0 ]
print(num_list)

num_list.sort()
print(num_list)

band_staff = [ "Ringo", "John", "George", "Paul" ]
print(band_staff)

band_staff.sort()
print(band_staff)

band_staff.sort(reverse=True)
print(band_staff)

# for strings, sort uses the ASCIIbetical order (order by the ASCII table)
ASCIIbetical = [ "Andy", "kiwi", "apple", "Karen", "Brian", "banana" ]
ASCIIbetical.sort()
print(ASCIIbetical)

# ignores Cases
ASCIIbetical.sort(key=str.lower)
print(ASCIIbetical)

# .index() returns the index number of an item
# .index() of an item that isn't in the list, will cause an error
metals = [ "copper", "gold", "silver", "iron" ]
print(metals.index("silver")) # 2

# .index() of an item that's have multiple values, only the first occurrence
numbers = [ 4, 3, 2, 1, 0, 1, 2, 3, 4 ]
print(numbers.index(3)) # 1

# .pop()
# pop methods remove and return from a list

bands = [ "Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead" ]
last = bands.pop()
print(bands)
print(last)

pop_by_index = bands.pop(3)
print(bands)
print(pop_by_index)

