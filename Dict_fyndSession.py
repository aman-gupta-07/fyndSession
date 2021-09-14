# Dictionary -----> {}, mutable(Hybrid), duplication not allowed
# No indexing present

# Creation Part
# {key : value}

dict1 = {1: 100}
print(dict1)

# float and strings as key
dict2 = {0.23: 100, "two": 23}
print(dict2)
# list as a key
# We can't as lists can be modified.
# Same is the case for dictionaries.
# We can give lists, tuples or anything as values.

# dict3 = {{1: 100}: 34}
# print(dict3)
# We cannot give Dictionaries or lists as keys.
# dict4 = {[1, 2]: 1000}
# print(dict4)
# Accessing the
# popitem method Removes arbitrary key,value pair.
# print(dict.popitem())
# Hybrid ---> key -----> immutable, value ----> mutable
dictNew = {1: 200, 2: 300, "Key": [2, "Value", 4]}
print(dictNew["Key"][1][2])  # Will give l as an output
# First we need to remove the key,value pair
dictNew.pop(2)
# Now we can update the key to the value assigned as before.
dictNew.update({4: 300})
print(dictNew)
# Concatenation of two dictionaries
dict2 = {0.23: 100, "two": 23}
dictNew = {1: 200, 2: 300}
dictConcatenate = dictNew
for (key, value) in dict2.items():
    dictNew.update({key: value})

print(dictConcatenate)
# Tuple as a key is acceptable.
dict7 = {(1, 2, 3): 345}
print(dict7)
print(dict7[(1, 2, 3)])

dict7[2] = 345
print(dict7)
dict7[2] = 453
# Overhead previous value assigned to key : 2
print(dict7)
# Removing key value pairs
# pop(key)
dict7.pop(2)
print(dict7)

print(dictNew.items())

#  We would store keys an values in lists and we can create the dictionaries
# using zip over a loop.
listKey = [1, 2, 3, 4, 5]
listValues = [10, 20, 30, 40, 50]

dictResultant = {}
for key, value in zip(listKey, listValues):
    dictResultant[key] = value

print(dictResultant)

dictResultant = {key: value for key, value in zip(listKey, listValues)}

# print(dict1 + dict2) will not give  us anything.
# print(dict1 + dict2)

