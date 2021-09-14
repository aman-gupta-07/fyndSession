# Sets
# Sets ---> {},, mutable, indexing not allowed

# Set is not the ordered/indexed data structure

set1 = {1, 2, 3, 5, 6}
set2 = {5, 6, 7, 4, 8}
set3 = {2, 4, 6, 8, 10}

# Set follows mathematical/ theoretical definitions in Python
# Set Operations
# | ---> Union, ^ ---> Symmetric Difference
# - ---> set difference, & ----> intersection
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2 | set3))
print(set2.difference(set3.intersection(set1)))

# Duplication
set4 = {2, 4, 5, 6, 3, 4, 5}
print(set4)
# Will return {2, 3, 4, 5, 6} as output
# Empty set is a dictionary.
