# Set  unordered collections
# doesnot allow duplicates

vowels = {'a','e','i','o','u',4}
print(vowels)

squares = {x*x for x in range(10)}
print(squares)
new_set = set()
new_set.add(3)
new_set.add('x')
print(new_set)

print(3 in new_set) #True

# -----------------------------
""" frozenset """
#immutable version of set that cannot be changed once it has been constructed

vowels = frozenset( {'a','e','i','o','u',4})
print(vowels)
# vowels.add not available

# forzenset are hashable and can be used as dictionary keys
d = {frozenset({1,2,3}):'hello'}
print(d[frozenset({1,2,3})])
#---------------------------------
"""  collections.Counter - Multisets """
# standard library implements a multiset( or bag) type that allows elements in the set to have more than one occurrence

# this is to track of not only if an element is present , but also how many times

from collections import Counter

inventory = Counter()
loot = {'sword':1, 'bread': 3}
inventory.update(loot)
print(inventory)
loot_2 = {'sword':1, 'apple': 1}
inventory.update(loot_2)
print(inventory)

print(len(inventory)) #3
print(sum(inventory.values())) #6
#---------------------------------------------

# simple built in stacks
s = ['a', 'b', 'c']
print(s)

s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
#s.pop() #IndexError: pop from empty list

# stack with performance characteristic of linked-list implementation

from collections import deque
s = deque()
s.append('a')
s.append('b')
s.append('c')
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
#s.pop()  #IndexError: pop from an empty deque

#----------------------------------------------

""" queue.LifoQueue - locking semantic for parallel computing  """
"""  
    This stack implementation is python standard library is synchronized and provides locking semantic to support 
    multiple concurrent producers and consumers 

    queue module contains several other classes that implement multi-producer/multi-consumer queues that use full for parallel programming 
"""

from queue import LifoQueue

s = LifoQueue()
s.put('a')
s.put('b')
s.put('c')
print(s)

s.get()
s.get()
s.get()
#val = s.get() # Blocks/waits forever...
#print(val)
#--------------------------

stack = LifoQueue(maxsize=1)

# Push items onto the stack
stack.put(1)

# Check if the stack is full
print(stack.full())  # Output: True
#--------------------------------

import time

stack = LifoQueue()

# Try to pop from an empty stack with a timeout
try:
    print(stack.get(timeout=2))  # Waits for 2 seconds and raises `queue.Empty` if no item is available
except Exception as e:
    print(f"Exception Occured while fetching from empty stack: {e}")  # Output: Exception:
#-------------------------------------------------

"""  Using LifoQueue in a Multithreaded Environment  """

from threading import Thread

# Shared stack
stack = LifoQueue()

# Producer thread
def producer():
    for i in range(5):
        print(f"Producing: {i}")
        stack.put(i)

# Consumer thread
def consumer():
    for _ in range(5):
        item = stack.get()
        print(f"Consuming: {item}")

# Start threads
producer_thread = Thread(target=producer)
consumer_thread = Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()







