
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

def vydya_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value


def bounded_repeater(value, max_repeats):
    count = 0
    while count < max_repeats:
        yield value
        count += 1

def bounded_repeater2(value, max_repeats):
    for i in range(max_repeats):
        yield value

for x in vydya_repeater('Hello',3):
    print(x)
    if len(x) > 5:
        break

print(vydya_repeater('Hello',4))
#yield is a keyword that is used like return, except the function will return a generator.
#Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:
# return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.

# The vydya_repeater function is a generator that yields the same value a maximum number of times.
# The generator function yields values instead of returning them.
# The for loop terminates when the length of the string is greater than 5.

""" Generator expressions """
# Generator expressions are a high-performance, memory-efficient generalization of list comprehensions and generators.
# They allow you to create a generator without the overhead of a full generator definition.
# Generator expressions are especially useful for very large datasets.
# You can create a generator expression by putting list comprehension syntax between () parentheses.

# Create a generator expression
iterator = ('Hello' for _ in range(3))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# this is much more efficient than using a list comprehension, because it doesn’t allocate memory for the whole list. It just keeps the expression in memory and generates the items on the fly.

# genexpr = (expression for item in collection if condition)
# The syntax for a generator expression is the same as for a list comprehension, except you use () parentheses instead of [] brackets.
# The genexpr syntax is more concise but less readable than the equivalent list comprehension.

print(sum(x * x for x in range(10)))  # sum of squares
print(max(x * x for x in range(10)))  # maximum of squares
print(min(x * x for x in range(10)))  # minimum of squares
print(all(x * x for x in range(10)))  # logical AND of squares
print(any(x * x for x in range(10)))  # logical OR of squares
# The sum function calculates the sum of the squares of the numbers from 0 to 9.
# The max function calculates the maximum of the squares of the numbers from 0 to 9.
# The min function calculates the minimum of the squares of the numbers from 0 to 9.
# The all function returns True if all the squares of the numbers from 0 to 9 are true.
# The any function returns True if any of the squares of the numbers from 0 to 9 are true.



""" Iterator chains """
# You can chain together multiple iterators using the chain() function from the itertools module.
# The chain() function takes a variable number of iterators and returns an iterator that produces the contents of all the input iterators sequentially.
# The chain() function is useful for treating multiple sequences as a single sequence.
# The chain() function returns an iterator that produces the values from the input iterators in order.
# The output of the code is:

def integers():
    for i in range(1, 9):
        yield i

chain = integers()
print(list(chain))  # [1, 2, 3, 4, 5, 6, 7, 8]

def squared(seq):
    for i in seq:
        yield i * i

chain = squared(integers())
print(list(chain))  # [1, 4, 9, 16, 25, 36, 49, 64]

#Favorite thing about chaining generators is that the data processing happens one element at a time. There is no buffering between the processing steps in tha chain.
#The chain() function is a generator that chains together multiple iterators into a single sequence.

integers_new = range(1, 9)
squared_new = (i * i for i in integers_new)
negated = (-i for i in integers_new)
print(list(negated))  # [-1, -4, -9, -16, -25, -36, -49, -64]
print(list(squared_new))  # []


