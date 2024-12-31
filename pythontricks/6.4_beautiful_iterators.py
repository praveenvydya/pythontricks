from scipy.special import factorial


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

repeater = Repeater('Hello')
iterator = iter(repeater)
print(next(iterator))
print(next(iterator))

# for item in repeater:
#     print(item)
#     if len(item) > 5:
#         break

# The Repeater class is an iterator that returns the same value every time its __next__ method is called.
# The __iter__ method returns the iterator object itself.
# The for loop terminates when the length of the string is greater than 5.
# The output of the code is:

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater = BoundedRepeater('Hello', 3)
for item in repeater:
    print(item)

# The BoundedRepeater class is a bounded iterator that returns the same value a maximum number of times.
# The __next__ method raises a StopIteration exception when the maximum number of repeats is reached.
# The output of the code is:
# Hello
# Hello
# Hello

while True:
    try:
        item = next(repeater)
        print(item)
    except StopIteration:
        break


# The itertools module in the Python standard library contains a collection of functions that return iterators.
# The itertools.count function returns an iterator that produces consecutive integers indefinitely.
# The itertools.cycle function returns an iterator that repeats the values in a sequence indefinitely.
# The itertools.repeat function returns an iterator that produces the same value indefinitely.
# The itertools.chain function returns an iterator that combines multiple iterators into a single sequence.
# The itertools.islice function returns an iterator that produces a slice of the values from an iterable.
# The itertools.tee function returns multiple independent iterators from a single input iterable.
# The itertools.zip_longest function returns an iterator that aggregates elements from multiple iterables.
# The itertools.product function returns an iterator that computes the Cartesian product of multiple iterables.
# The itertools.permutations function returns an iterator that produces all possible permutations of the input iterable.
# The itertools.combinations function returns an iterator that produces all possible combinations of the input iterable.
# The itertools.combinations_with_replacement function returns an iterator that produces all possible combinations of the input iterable with replacement.
# The itertools.groupby function returns an iterator that groups elements from an iterable based on a key function.
# The itertools.accumulate function returns an iterator that produces accumulated sums or other binary functions.
# The itertools.filterfalse function returns an iterator that filters elements from an iterable based on a predicate function.
# The itertools.dropwhile function returns an iterator that drops elements from an iterable while a predicate function is true.
# The itertools.takewhile function returns an iterator that produces elements from an iterable while a predicate function is true.
# The itertools.islice function returns an iterator that produces a slice of the values from an iterable.
# The itertools.starmap function returns an iterator that computes a function using arguments obtained from a sequence.

from itertools import permutations

# Characters to use in the password
chars = ['v', 'y', 'd','a','1','2','3','4','5','6','7','8','9','0']
# Generate all possible 8-character passwords
passwords = permutations(chars, 8)
print(factorial(len(chars)) / factorial(len(chars) - 8))
# print(len(list(passwords)))

# for password in passwords:
#     print(''.join(password))

#---------------------------------------------

from itertools import product
# Generate all possible 2-letter combinations
pairs = product(chars, repeat=2)
# for pair in pairs:
#     print(''.join(pair))
#---------------------------------------------

