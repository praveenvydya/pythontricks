"""
Compared to arrays , record data structures provide a fixed number of fields where each field con have a name and may have different type


"""
import types

# dict

# also called as maps or associative array.
Car1 ={
    'color':'red',
    'mileage':42.4,
    'automatic':True,
}
Car2 = {'color': 'white', 'mileage': 32.4, 'automatic': False}

#Dicts are mutable
Car1['mileage'] = 33
# no protection against wrong filed names, or missing/extra fields
Car2['windshield']='borken'
print(Car2)

# tuple  - Immutable groups of objects
# Python's tuples are simple data structures for grouping arbitrary objects.
# performance wise tuple takes up slightly less memory than list. but in practice this will offen negligible.
import dis
dis.dis(compile("(23,'a','c')",'','eval'))
dis.dis(compile("[23,'a','c']",'','eval'))

"""
Writing custom classes: More work more control
"""
class Car:
    def __init__(self,color,mileage,automatic):
        self.color=color
        self.mileage=mileage
        self.automatic=automatic

    def __repr__(self):
        #return f'Car({self.color},{self.mileage},{self.automatic})'
        attributes = ','.join(f"{key}={value}" for key,value in self.__dict__.items())
        return f'Car({attributes})'


car1 = Car('red',324.3,True)
car2 = Car('black',42.432,False)
# classes are mutable
car1.mileage=80.9
print( car1)

car1.windshield = 'broken'
print(car1)
print( car1.__dict__.items())
print(f"{key}={value}" for key,value in car1.__dict__.items())
#---------------------------------------------------------------
"""  Named Tuple  """ #Immutable
# better than regular class in memory usages
from collections import namedtuple
from sys import getsizeof
Point = namedtuple('Point', 'x y z')
p1 = Point(x=1,y=2,z=3)
p2 = (1,2,3)
print(getsizeof(p1))
print(getsizeof(p2))
p3 =Point('Yes',2.8,False)
print(p3)
#---------------------------------------

"""   typing NamedTuple """

from typing import NamedTuple

class CarNew(NamedTuple):
    color:str
    mileage:float
    automatic:bool

car_new = CarNew('red',34.2,True)
print(car_new)

#car_new.mileage = 44  # AttributeError: can't set attribute
print(car_new)
#------------------------------------------------------
"""    struct.Struct serialized C structs """
#It can be used to handle binary data stored in files or coming in from network connections
# packing primitive data into structs may use less memroy than keeping it in other data types.

from struct import Struct
MyStruct = Struct('i?f')   #

"""
i: Represents a 4-byte integer (e.g., int).
?: Represents a 1-byte boolean (True/False).
f: Represents a 4-byte float.
"""""
data = MyStruct.pack(34,False,45.09)
print(data)  # all you get is blob of data
info = MyStruct.unpack(data)
print(info)  #(34, False, 45.09000015258789)
#-------------------------------------------------------

"""   types.SimpleNamespace  """

from types import SimpleNamespace

car_2 = SimpleNamespace(color='Red',automatic = True,mileage=23.3)
print(car_2)
print(car_2.color)
print(car_2.mileage)
print(car_2.automatic)
del car_2.color
print(car_2)

#-----------------------------------------------------------

















