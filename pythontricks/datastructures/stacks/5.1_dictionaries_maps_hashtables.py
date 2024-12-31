"""
Dictionaries store an arbitrary number of objects, each identified by a unique dictionary key
Example : phonebook

"""

phonbook = {
    "bob":78984,
    "alice":8745,
    "jack":2578,
}

squares = {x:x*x for x in range(6)}

print(phonbook['alice'])
print(squares)

"""
Python dictionaries are indexed by keys that can be of any hashable type.  
A hashable object has a hash value which never changes during its life time.see (__hash__)
and it can be compared to other objects(see __eq__). 
In addition, hashable objects which compare as equal must have same hash value

Immutable types like strings and numbers are hashable and works well as dictionary keys. you can also use tuple as dictionary keys as long as they contain only hashable types themselvs
Besides plain dict onjects Python's standard library also includes a number of specialized dictionary implementations.
"""
from collections import OrderedDict
# collections.OrderedDict - Remember the insertion Order of keys
d = OrderedDict(one=1,two=2,three=3)
print(d)
d['four'] =4
print(d)
print(d.keys())
#-----------------------------
#collections.defaultdict - return default values for missing keys
from collections import defaultdict
dd = defaultdict(list)
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
print(dd)
print(dd['dogs'])

di = defaultdict(int)
di['one'] = 1
di['two'] =2

print(di)
#di['three'] ='three' #cannot add
#-------------------------------------

# collections.ChainMap - search Multiple Dictionaries as single Mapping
# chainMap data structure groups multiple dictionaries into single mapping.
# lookups search the underlying mapping one by one until a key found.
# Insertion,update,and deletions only affect the first mapping added to the chain
from collections import ChainMap

dict1= {'one':1,'two':2}
dict2 ={'three':3,'four':4}

chain = ChainMap(dict1,dict2)
print(chain)
print(chain['one'],chain['four'])  # *****

chain['one'] = 12
print(chain)
chain['four'] = 40 #Insertion,update,and deletions only affect the first mapping added to the chain
#'four' added to the first map only not updating second map
print(chain)
print(chain['four']) # prints 40
#----------------------------------------

"""
All these dictionary implementations listed here are valid implementations 
that are built into the Python standard library

"""

