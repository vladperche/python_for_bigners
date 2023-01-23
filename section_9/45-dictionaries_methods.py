# .clear()

ex_1 = { 1:"England", 2:"Scotland", 3:"Wales", 4:"Northen Ireland" }
print(ex_1)

ex_1.clear()
print(ex_1)

# .copy()

birth_years = { 1994:"bill", 1969:"emily", 1982:"elizabeth", 2000:"turner" }

people = birth_years.copy()
people[1982] = "madeline"

print(birth_years)
print(people)

# .update()

city_info = { "country":"Canada", "province":"Ontario", "city":"Toronto" }
population = { "population": 2930000 }
city_info.update(population) # population will be addded to city_info

print(city_info)

population["population"] = 3000000 # city_info remains unchanged
print(city_info)

city_info.update(population) # city_info will be updated
print(city_info)

