""" Convert a dictionary to a JSON string """

# You can convert a dictionary to a JSON string using the json.dumps function.
# The json.dumps function returns a JSON string representation of the dictionary.
# The json.dumps function accepts the following arguments:
# The dictionary to convert to a JSON string.
# The indent argument specifies the number of spaces to use for indentation.
# The sort_keys argument specifies whether to sort the keys of the dictionary.
# The json.dumps function returns a JSON string representation of the dictionary.
# The output of the code is:

import json
mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(json.dumps(mapping, indent=4, sort_keys=True))

# {
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }

# other example supported built in types are:
# dict
# list
# tuple
# str
# int
# float
# True
# False
# None
# The JSON format is commonly used for serializing and transmitting structured data over a network connection.

mapping['d'] = {1, 2, 3}
print(mapping) # {'a': 23, 'b': 42, 'c': 12648430, 'd': {1, 2, 3}}
# print(json.dumps(mapping)) # TypeError: Object of type set is not JSON serializable

import pprint
pprint.pprint(mapping) # {'a': 23, 'b': 42, 'c': 12648430, 'd': {1, 2, 3}}
# The pprint module provides a capability to pretty-print arbitrary Python data structures in a format that can be used as input to the interpreter.


