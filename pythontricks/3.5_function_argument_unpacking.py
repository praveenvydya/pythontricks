#
"""Function arguments unpacking """

def print_vector(x,y,z):
    #print(f'<{x}, {y}, {z}>')
    #print('<%s, %s , %s>'.format(x,y,z))
    print('<%s, %s , %s>' % (x, y, z))

print_vector(1,2,3)

tuple_vec = (4,5,6)
list_vec= [7,8,9]

print_vector(tuple_vec[0],tuple_vec[1],tuple_vec[2])

# much nicer code here
print_vector(*tuple_vec)
print_vector(*list_vec)

""" putting * before an iterable in a function call will unpack it and pass its elements as separate positional arguments to the called function"""
# this technique works for any kind of iterable including generator expressions.
gen  = (x * x for x in range(3,6))
print_vector(*gen)

dict_vec = {'y':11,'z':12,'x':13}

# The * and ** operators can be used to "unpack" functions arguments from sequences and dictionaries

print_vector(*dict_vec)
print_vector(**dict_vec)