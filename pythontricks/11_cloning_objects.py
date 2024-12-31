
import gc
import copy
# Cloning objects for fun and profit
"""Assignment statements in python do not create copies of objects, they only bind names to an object.  For Immutable also """

# Python's built in collections like lists,dicts and sets can be copied by their factory functions on an existing collections
# Shallow copying
org_list = [1,2,3,4,5]
org_dict = {'1':1,'2':2}
org_set = (1,2,3,4,5)
new_list = list(org_list)
new_dict = dict(org_dict)
new_set = set(org_set)
# Shallow copy means constructing a new collection object and the populating it with reference to the child objects found in the original - One level up
# The copying process doesn't recurse and therefore won't create copies of the child objects themselves.

# Deep copy makes copying process recursive

xs = [[1,2,3],[4,5,6],[7,8,9]]
ys = copy.copy(xs) #list(xs) # shallow copy

print(xs)
print(ys)

xs.append(['new list']) # modifies original object only not reference

print(xs)
print(ys) # ys is independent from original

xs[1][0] = 'Y' # updating object is updating reference and both objects share the same child objects
print(xs) #[[1, 2, 3], ['Y', 5, 6], [7, 8, 9], ['new list']]
print(ys) #[[1, 2, 3], ['Y', 5, 6], [7, 8, 9]]

print(gc.get_referents(xs))
print(gc.get_referents(ys))

#============================================================================
"""Making Deep copies"""
print('======================= " Making Deep copies " =======================')

xs = [[1,2,3],[4,5,6],[7,8,9]]
zs = copy.deepcopy(xs)

xs[1][0] = 'X'
print(xs) #[[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
print(ys) #[[1, 2, 3], [0, 5, 6], [7, 8, 9]]
# both xs and ys are independent