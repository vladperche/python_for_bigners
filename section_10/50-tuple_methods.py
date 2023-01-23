nested = ( 1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
print(nested[4])
print(nested[5][1])

repeat = ( 7, 3, 3, 3, 0, 0, 7, 0, 0)
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(0))

ints = ( 1, 1, 7 )
print(ints.index(7))
print(ints.index(1))
print(ints.index(8)) # will cause an error, because 8 isn't in the tuple

