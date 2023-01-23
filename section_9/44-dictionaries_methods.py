ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")
print(ex_1)


ex_2 = { "make":"Honda", "model":"Civic", "year":2016 }
popped = ex_2.pop("model")
print(ex_2)
print(popped)

popped_item = ex_2.popitem()
print(popped_item)

