# sets look like lists
# - cannot have duplicated values
# - itens are unorderd

set_1 = { 9, 8, 7, 6 }
set_2 = set({ "a", "b", "c", "d", "e" })
print(set_1)
print(set_2)

set_3 = set(range(1, 12, 2))
print(set_3)

set_4 = { "a", 3.14, 18, True }
print(set_4)

set_5 = { 3, 6, 9, 12, 15 }
for num in set_5:
    print(num)

print(12 in set_5)
print(13 in set_5)

