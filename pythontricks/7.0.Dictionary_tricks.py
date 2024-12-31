""" Dictionary tricks """
# To avoid KeyError when accessing dictionary values, you can use the get() method or a defaultdict from the collections module.
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",

}

def greeting(userid):
    return f"Hi {name_for_userid.get(userid, 'there')}!"
print(greeting(382))
print(greeting(333333))
#
# # Using defaultdict

from collections import defaultdict
name_for_userid = defaultdict(str, {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
})
print(name_for_userid[382])
print(name_for_userid[333333])

#------------------------------------------------------------------------
""" Sorting dictionaries for fun and profit """
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
# when you iterate over a dictionary using items(), it yields key-value pairs in an arbitrary order as tuples
print(sorted(xs.items(), key=lambda x: x[1]))  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
print(sorted(xs.items())) # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
print(list(x for x in xs.items()))
print(sorted(xs.items(), key=lambda x: x[0],reverse=True)) # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
print(sorted(xs.items(), key=lambda x: abs(x[1]))) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

#--------------------------------------------------------------------
""" Dictionary Comprehensions """
# Dictionary comprehensions are a way to build dictionaries using an expression.
# The key: value pairs are defined inside the {} braces.
# An optional if condition can filter items to include.
# The syntax is {key: value for key, value in iterable}
# The iterable can be any iterable object, like a list, tuple, set etc.
# The key and value can be any objects.
# The key and value can also be created using expressions.
# Dictionary comprehensions are a concise way to create dictionaries.
# Dictionary comprehensions are often more readable than using map() and filter() functions.

# Create a dictionary from a list of tuples
print({x: x**2 for x in (2, 4, 6)})

#----------------------------------------------------------------

""" Counting with dictionaries """
# Counting with dictionaries is a common task in data science.
# You can use a defaultdict from the collections module to count items in a sequence.
# The defaultdict is a subclass of the built-in dict class.
# It overrides one method and adds one writable instance variable.
# The defaultdict provides a default value for the key that does not exist.
# The default value is specified when creating the defaultdict.
# The default value is specified using a callable object.
# The callable object is called without arguments to provide a default value for the key.
# The output of the code is:
from collections import defaultdict
# Count the frequency of each letter in a string
s = "mississippi"
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d)  # defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})

# Best alterante for this is to use Counter from collections module
from collections import Counter
print(Counter(s)) # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# The Counter class from the collections module is a dictionary subclass that counts
# the frequency of each element in a sequence.
# The Counter class returns a dictionary with elements as keys and their counts as values.

""" Emulating switch/case statements with dictionaries """
# You can emulate switch/case statements in Python using dictionaries.
# The dictionary maps the case values to functions that implement the case logic.

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None

def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_if('add', 2, 8))  # 10
print(dispatch_dict('add', 2, 8))  # 10
print(dispatch_if('unknown', 2, 8))  # None
print(dispatch_dict('unknown', 2, 8))  # None

# The dispatch_if function uses if-elif-else statements to implement the case logic.
#-----------------------------------------------------------------------



