birth_years = { 1994:"bill", 1969:"emily", 1982:"elizabeth", 2000:"turner" }

# .keys()
# shows all keys from a dictionarie

print(birth_years.keys())
for year in birth_years.keys():
    print(year)

# .values()
# gets all the values from a dictionary

print(birth_years.values())
for name in birth_years.values():
    print(name)

# .items()
# will return a list of 'tuples'

print(birth_years.items())
for tuple in birth_years.items():
    print(tuple)

for key, value in birth_years.items():
    print("{} : {}".format(key,value))

# in / not in
print("elizabeth" in birth_years.values())
print(1977 in birth_years.keys())

# .get() returns an specific element
# it has 2 arguments:
# - first, the key you want to find
# - second, the value that will be used, if the key isn't found

key = 1975
if key in birth_years.keys():
    print(birth_years[key])
else:
    print("{} is not a key in birth_years.".format(str(key)))

print(birth_years.get(key, "{} is not a key".format(str(key))))

# References
# When a dictionary is directly assigned to another variable,
# this new variables becomes a reference to the original dicitonary

people = birth_years # creates a reference

people[1982] = "madeline" # as the variable is a reference, not a new memory space, both variables are modified

print(birth_years)
print(people)

