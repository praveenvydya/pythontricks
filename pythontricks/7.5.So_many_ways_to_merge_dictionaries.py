xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
ys = {'d':4,'e': 1, 'f': 2, 'g': 3,}

# merge two dictionaries in a single expression
zs = {**xs, **ys}
print(zs)# {'a': 4, 'b': 3, 'c': 2, 'd': 4, 'e': 1, 'f': 2, 'g': 3}
zs2 = {**ys, **xs}
print(zs2) # {'d': 1, 'e': 1, 'f': 2, 'g': 3, 'a': 4, 'b': 3, 'c': 2}

# In Python 3.5 and earlier, you can merge dictionaries using the built-in dict.update method:
zs3 = xs.copy()
zs3.update(ys)
print(zs3) # {'a': 4, 'b': 3, 'c': 2, 'd': 4, 'e': 1, 'f': 2, 'g': 3}

# In Python 3.9 and later, you can use the union operator (|) to merge dictionaries:
zs4 = xs | ys
print(zs4) # {'a': 4, 'b': 3, 'c': 2, 'd': 4, 'e': 1, 'f': 2, 'g': 3}

# The union operator (|) was introduced in Python 3.9. It is equivalent to the dict.update method, but it returns a new dictionary instead of updating an existing one in place.
# The union operator (|) can be used to merge multiple dictionaries in a single expression:
# zs5 = xs | ys | zs
# print(zs5) # {'a': 4, 'b': 3, 'c': 2, 'd': 4, 'e': 1, 'f': 2, 'g': 3}
# The union operator (|) can also be used to update dictionaries with keyword arguments:
# zs6 = {**xs, **ys, d=4, e=5}
# print(zs6) # {'a': 4, 'b': 3, 'c': 2, 'd': 4, 'e': 5, 'f': 2, 'g': 3}
# The union operator (|) can be used to merge dictionaries with different key types:
# zs7 = {1: 'a'} | {'b': 2}
# print(zs7) # {1: 'a', 'b': 2}
# The union operator (|) can be used to merge dictionaries with different value types:
# zs8 = {'a': 1} | {'a': 'b'}
# print(zs8) # {'a': 'b'}
# The union operator (|) can be used to merge dictionaries with different key and value types:
# zs9 = {1: 'a'} | {'b': 2}
# print(zs9) # {1: 'a', 'b': 2}

#