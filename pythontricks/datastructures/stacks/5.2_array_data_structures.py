#Arrays consistes of fixed-size data records that allow each element to be efficiently located based on its index
# because arrays store information in adjoining blocks of memory, they are considered contiguous data structures (as opposed to linked data structure like linked list)

"""

You can look at the parking lot as a whole and treat it as a single object, but inside the lot there are parking spots
indexed by a unique number. parking spots are containers for vehicles - each parking spot can either be empty or have
a car,bike or some other vehicle parked on it.

"""


# list  - mutable dynamic arrays

arr = ['one','two','three']
print(arr)
del arr[1]
print(arr)
arr.append(43)

#--------------------------------
# tuple  - Immutable containers

tup = 'one','two','three'
print(tup)
#tup[1] = 'hello'  #TypeError: 'tuple' object does not support item assignment
#del tup[1] #TypeError: 'tuple' object doesn't support item deletion

new_tup = tup+(23,)
print(new_tup)
print(tup)
#-----------------------------------
## array.array - Basic Typed Arrays
# mutable
import array

tarry = array.array('f',(1,2,3,4,5))
print(tarry)
tarry[1] = 23
print(tarry)
del tarry[1]
print(tarry)
tarry.append(66)
print(tarry)

#tarry[1]='hello' #TypeError: must be real number, not str

"""
Type Code	C Type	Python Type	Description
'b'	signed char	int	1-byte signed integer
'B'	unsigned char	int	1-byte unsigned integer
'u'	Py_UNICODE	str	Unicode character (deprecated)
'h'	signed short	int	2-byte signed integer
'H'	unsigned short	int	2-byte unsigned integer
'i'	signed int	int	2-byte or 4-byte signed int
'I'	unsigned int	int	2-byte or 4-byte unsigned int
'l'	signed long	int	4-byte signed integer
'L'	unsigned long	int	4-byte unsigned integer
'q'	signed long long	int	8-byte signed integer
'Q'	unsigned long long	int	8-byte unsigned integer
'f'	float	float	4-byte floating-point number
'd'	double	float	8-byte floating-point number

Notes:
1. array.array is particularly useful when memory efficiency is critical.
2. For general-purpose array handling, consider using numpy as it provides more flexibility and additional functionality.
"""
arr = array.array('b', [-125,-10, 0, 10, 16,125])
print(arr)  # array('b', [-10, 0, 10])

arr = array.array('B', [0, 255, 100]) #8 bit
print(arr)  # array('B', [0, 255, 100])

arr = array.array('u', 'hello')
print(arr)  # array('u', 'hello')

arr = array.array('h', [-32768, 0, 32767])
print(arr)  # array('h', [-32768, 0, 32767])

arr = array.array('H', [0, 65535]) # 16 bit
print(arr)  # array('H', [0, 65535])

arr = array.array('i', [-2147483648, 2147483647])
print(arr)  # array('i', [-2147483648, 2147483647])

arr = array.array('I', [0, 4294967295]) # 32 bit
print(arr)  # array('I', [0, 4294967295])

arr = array.array('l', [-2147483648, 2147483647])
print(arr)  # array('l', [-2147483648, 2147483647])

arr = array.array('L', [0, 4294967295]) # 32 bit
print(arr)  # array('L', [0, 4294967295])

arr = array.array('q', [-9223372036854775808, 9223372036854775807])
print(arr)  # array('q', [-9223372036854775808, 9223372036854775807])

arr = array.array('Q', [0, 18446744073709551615]) # 64 bit
print(arr)  # array('Q', [0, 18446744073709551615])

arr = array.array('f', [1.5, 2.5, 3.5])
print(arr)  # array('f', [1.5, 2.5, 3.5])

arr = array.array('d', [1.123456789, 2.987654321])
print(arr)  # array('d', [1.123456789, 2.987654321])


#---------------------------------------
import math

print(math.log2(4294967295)) #32
print(math.log2(18446744073709551615)) #64

""" Immutable array of strings """
arr = 'abcd' # Immutable
print(arr[1])
#arr[1]='x' #TypeError: 'str' object does not support item assignment
print(list(arr)) #['a', 'b', 'c', 'd']
print(type(list(arr)))
print(','.join(list(arr)))


# bytes array Immutable array of single byte
arr = bytes([0,1,2,3,4])  # only valid range(0,256)

# bytearray Mutable array
arr_m = bytearray([0,1,2,3,4])
arr_m[1] = 9
print(arr_m)
#----------------------------------------




