# tuple
# Cahracteristics : ( ) , immutable, indexing, duplication, hetero, slice
tup0 = ()
print(tup0)
tup1 = (2, 3, 4, 6)
tup2 = (3, 3, 4, 2)

tup3 = (tup1[i]+tup2[i] for i in range(len(tup1)))
print(set(tup3))
# printing a single entry tuple without comma in the end will not give us tuple as an output but just that entry

# list inside tuple
tup_list = (1, [2,3])
print(tup_list)

# Accessing through index is possible.
print(tup_list[1])

del tup_list

# Methods
tup4  = (10, 23, 20, 30, 23, 10)
print(tup4.count(23))

print(tup4.index(30))
print(tup4.index(10))
# Concatenate two tuples
tup5 = (1, 3, 5)
tup6 = (2, 4, 6)
print(tup5 + tup6)
# Chaining is possible in tuples

tup7 = tup5
print(tup5 + tup7)


