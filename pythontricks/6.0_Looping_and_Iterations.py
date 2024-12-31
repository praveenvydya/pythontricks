


#
my_items = ['a', 'b', 'c']
for item in my_items:
    print(item)
# Output:
for i,item in enumerate(my_items):
    print(i,item)

emails ={
    'Bob': 'bob@exmaple.com',
    'Alice': 'alice@example.com',

}
for name, email in emails.items():
    print(name,email)
#
for i in range(2,10,2):
    print(i)

# Comprehending comprehensions
# List comprehensions are a concise way to create lists. Common applications are to make new lists where each element is the result of
# some operation applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
# For example, assume we want to create a list of squares, like:
squares =[x*x for x in range(10)]
print(squares)
even_squares = [x*x for x in range(10) if x%2==0]
print(even_squares)

# Dict comprehensions are similar, but allow you to easily construct dictionaries. For example:
squares = {x:x*x for x in range(10)}
print(squares)
# Set comprehensions are also supported. For example:
squares = {x*x for x in range(10)}
# Generator comprehensions are a generator expression that returns a generator object. It is an alternative to list comprehensions, but with
# parentheses () instead of square brackets []. For example:
squares = (x*x for x in range(10))
print(squares)
# You can iterate over a generator comprehension like any other generator. For example:
for i in squares:
    print(i)
# Output:

# Generator comprehensions are especially useful for very large data sets, or when you don't want to allocate memory for a list that you're only going to iterate over.
# For example, the following code will sum the squares of the first 10 positive integers, but without creating a list of squares in memory:
squares = (x*x for x in range(10))
sum_of_squares = sum(squares)
print(sum_of_squares)


""" List Slicing """
# List slicing provides a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list with two colon-separated integers.

# The first integer is the index of the first element that you want to include in your selection.
# The second integer is the index of the first element that you want to exclude.
# If you don't include the first integer, Python will start at the beginning of the list.
# If you don't include the second integer, Python will go to the end of the list.
# You can also include a third integer when slicing a list. This third integer specifies the step size, which determines the frequency at which you take elements. For example, a step size of 2 takes every other element.
# Here's an example that selects the first three elements of a list:
my_list = ['a', 'b', 'c', 'd', 'e']
print(my_list[0:3])
# Output: ['a', 'b', 'c']
# If you don't include the first integer, Python starts at the beginning of the list. For example, to slice the first three elements of a list, you can use the following code:
print(my_list[:3])
# Output: ['a', 'b', 'c']
# If you don't include the second integer, Python goes to the end of the list. For example, to slice the last three elements of a list, you can use the following code:
print(my_list[2:])
# Output: ['c', 'd', 'e']
# You can use negative indices when slicing a list. For example, to slice all but the last element of a list, you can use the following code:
print(my_list[:-1])
# Output: ['a', 'b', 'c', 'd']
# To select every second element of a list, you can use the following code:
print(my_list[::2])
# Output: ['a', 'c', 'e']
# You can use a negative step size to return a list in reverse. For example, to reverse a list, you can use the following code:
print(my_list[::-1])
# Output: ['e', 'd', 'c', 'b', 'a']

""" Looping in reverse """
# To loop over a list in reverse, you can use the reversed() function. For example:
my_list = ['a', 'b', 'c', 'd']
for i in reversed(my_list):
    print(i)
# Output:
# d
# c


""" Looping over a sequence in reverse and getting the index """
# To loop over a sequence in reverse and also get the index of each element, you can use the following code:
my_list = ['a', 'b', 'c', 'd']
for i, e in reversed(list(enumerate(my_list))):
    print(i, e)
# Output:
# 3 d
# 2 c

for i,e in enumerate(reversed(my_list)):
    print(i,e)
# Output:
# 0 d
# 1 c

""" Looping over two sequences """
# To loop over two sequences at the same time, you can use the zip() function. For example:
my_list = ['a', 'b', 'c']
my_nums = [1, 2, 3]
for l, n in zip(my_list, my_nums):
    print(l, n)
# Output:
# a 1
# b 2

""" Looping over a sequence in sorted order """
# To loop over a sequence in sorted order, you can use the sorted() function. For example:
my_list = [3, 2, 1]
for i in sorted(my_list):
    print(i)
# Output:
# 1
# 2

""" Custom sort order """
# To loop over a sequence in a custom sort order, you can use the sorted() function with a custom key function. For example:
my_list = ['ccc', 'aaaa', 'd', 'bb']
for i in sorted(my_list, key=len):
    print(i)
# Output:
# d
# bb

var = [lambda x: print(x) for x in sorted(my_list, key=len)]
print(var)
# Output:
# d
# bb

""" Call a function until a sentinel value """
# To call a function until a sentinel value, you can use the iter() function with a callable and a sentinel value. For example:
import random
random.seed(1)
def random_gen():
    return random.randint(0, 10)

for i in iter(random_gen, 2):
    print(f'Random Val : {i}')
# Output:
# 9
# 1
# 7
# 6
# 9
# 10
# 1
# 7
# 6
# 9
# 10
# 1
# 7
# 6
# 9
# 10
# 1
# 7

""" Looping over a dictionary """
# To loop over a dictionary, you can use the items() method. For example:
my_dict = {'a': 1, 'b': 2, 'c': 3}
for k, v in my_dict.items():
    print(k, v)
# Output:
# a 1
# b 2

""" Looping over a dictionary keys """
# To loop over a dictionary keys, you can use the keys() method. For example:
for k in my_dict.keys():
    print(k)
# Output:
# a
# b

""" Looping over a dictionary values """
# To loop over a dictionary values, you can use the values() method. For example:
for v in my_dict.values():
    print(v)
# Output:
# 1
# 2

""" Construct a dictionary from pairs """
# To construct a dictionary from pairs, you can use the dict() function. For example:
pairs = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(pairs)
print(my_dict)
# Output:
# {'a': 1, 'b': 2, 'c': 3}

""" Counting with dictionaries """
# To count the occurrences of items in a list using a dictionary, you can use the following code:
my_list = ['a', 'b', 'a', 'c', 'b', 'a']
count = {}
for i in my_list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)
# Output:
# {'a': 3, 'b': 2, 'c': 1}

""" Grouping with dictionaries """
# To group items in a list by a certain key using a dictionary, you can use the following code:
my_list = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]
group = {}
for i in my_list:
    key = i['key']
    if key in group:
        group[key].append(i)
    else:
        group[key] = [i]
print(group)
# Output:
# {'a': [{'key': 'a', 'value': 1}, {'key': 'a', 'value': 3}], 'b': [{'key': 'b', 'value': 2}]}

from collections import defaultdict

my_list = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]

group = defaultdict(list)
for i in my_list:
    group[i['key']].append(i)

# Converting back to a regular dictionary if needed
group = dict(group)

print(group)
# Output:
# {'a': [{'key': 'a', 'value': 1}, {'key': 'a', 'value': 3}], 'b': [{'key': 'b', 'value': 2}]}

""" Is a list a subset of another list """
# To check if a list is a subset of another list, you can use the all() function. For example:
list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]
is_subset = all(i in list2 for i in list1)
print(is_subset)
# Output:
# True



""" Is a dictionary a subset of another dictionary """
# To check if a dictionary is a subset of another dictionary, you can use the items() method. For example:
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2, 'c': 3}
is_subset = all(k in dict2 and dict2[k] == v for k, v in dict1.items())
print(is_subset)
# Output:
# True

""" Find the most common elements """
# To find the most common elements in a list, you can use the Counter class from the collections module. For example:
from collections import Counter
my_list = ['a', 'a', 'a', 'b', 'b', 'c']
counter = Counter(my_list)
most_common = counter.most_common(1)
print(most_common)
# Output:
# [('a', 3)]

""" Find the most common element """
# To find the most common element in a list, you can use the Counter class from the collections module. For example:
from collections import Counter
my_list = ['a', 'a', 'a', 'b', 'b', 'c']
counter = Counter(my_list)
most_common = counter.most_common(1)[0][0]
print(most_common)
# Output:
# a

""" Remove duplicates from a list """
# To remove duplicates from a list, you can convert it to a set. For example:
my_list = ['a', 'a', 'b', 'b', 'c']
new_list = list(set(my_list))
print(new_list)
# Output:
# ['a', 'b', 'c']

""" Check if all elements in a list are equal """
# To check if all elements in a list are equal, you can use the all() function. For example:
my_list = ['a', 'a', 'a']
all_equal = all(x == my_list[0] for x in my_list)
print(all_equal)
# Output:
# True

""" Check if any elements in a list are equal """
# To check if any elements in a list are equal, you can use the any() function. For example:
my_list = ['a', 'a', 'b']
any_equal = any(x == my_list[0] for x in my_list)
print(any_equal)
# Output:
# True

""" Split a list into chunks """
# To split a list into chunks of a specific size, you can use the following code:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3
chunks = [my_list[i:i + size] for i in range(0, len(my_list), size)]
print(chunks)
# Output:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

""" Flatten a list of lists """
# To flatten a list of lists, you can use the following code:
my_list = [[1, 2], [3, 4], [5, 6]]
flat = [x for sublist in my_list for x in sublist]
print(flat)
# Output:
# [1, 2, 3, 4, 5, 6]

""" Flatten a list of lists using itertools.chain """
# To flatten a list of lists using itertools.chain, you can use the following code:
import itertools
my_list = [[1, 2], [3, 4], [5, 6]]
flat = list(itertools.chain(*my_list))
print(flat)
# Output:
# [1, 2, 3, 4, 5, 6]

""" Flatten a list of lists using itertools.chain.from_iterable """
# To flatten a list of lists using itertools.chain.from_iterable, you can use the following code:
import itertools
my_list = [[1, 2], [3, 4], [5, 6]]
flat = list(itertools.chain.from_iterable(my_list))
print(flat)
# Output:
# [1, 2, 3, 4, 5, 6]

""" Transpose a matrix """






