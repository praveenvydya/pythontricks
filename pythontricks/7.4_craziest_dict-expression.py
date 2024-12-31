
print(True==1)

print({True: 'yes', 1: 'no', 1.0: 'maybe'}) # {True: 'maybe'}
print({True: 'yes', 1: 'no', 1.0: 'maybe'}[True]) # maybe
print({True: 'yes', 1: 'no', 1.0: 'maybe'}[1]) # no
print({True: 'yes', 1: 'no', 1.0: 'maybe'}[1.0]) # maybe
#
print({True: 'yes', 1: 'no'}[True])#


dic = { 'a': 1, 'b': 2, 'c': 3,1:'x',1.0:'vydy',True:'Meena' }
print(dic['a'])
print(dic[True])

#it prints x if 1 is not present in the dictionary
#it prints vydy if 1.0 is not present in the dictionary
#it prints Meena if True is not present in the dictionary
print(True==1==1.0) #True
print((hash(True),hash(1),hash(1.0))) # (1, 1, 1)

# dictionaries check for equality and compare the hash value of the keys to determine if two keys are same or not.
# In this case, True, 1, 1.0 all have the same hash value of 1. So, they are considered equal keys and the last one wins.
