""" *** Named tuples  *** """
import json

# Named tuples is one of the amazing featues in Python that is hidden in plain sight
# Immutable - they cannot be modified once they have been created

tup = ('hello',object(),42)
print(tup)
#tup[2] = 24 "'TypeError: Can't instantiate abstract class Concrete without an implementation for abstract method 'bar'"

# namedtuple is write once, read many
from collections import namedtuple

# below creates class Car with fields color and mileage
Car = namedtuple('Car','color mileage')
# here first param - typename -> name of the class to be created
# 'color mileage'.split() -> ['color','mileage']
my_car = Car(color='Red',mileage=43)
print(my_car)

color, mileage = my_car
print(color,mileage)

#my_car.color = 'Green' #AttributeError: can't set attribute

"""Named tuples objects are implemented as regular Python classes internally. When it comes to memory usage, they also "better" than regular classes and just as memory efficient as regular tuples"""

# subc classing named tuple
class MyCar(Car):
    def hexcolor(self):
        if self.color== 'Red':
            return '#ff0000'
        else:
            return '#000000'

my_car = MyCar('Red',43)
print(my_car.hexcolor())

#ElectricCar = namedtuple('ElectricCar',Car._fields+('charge,')) # fields not comming something wrong here

# print(my_car._asdict()) not working

#========================NamedTuple working==============================
from typing import NamedTuple

# Define NamedTuple class
class Person(NamedTuple):
    name: str       # A string for the name
    age: int        # An integer for the age
    height: float   # A float for the height

# Create an instance
person = Person(name="Bob", age=25, height=5.8)
print(Person._fields)
print(person.name)  # Bob
print(person.age)   # 25
print(person.height)  # 5.8

print(person._asdict()) # {'name': 'Bob', 'age': 25, 'height': 5.8}

# Very useful method to convert object data to json
print(json.dumps(person._asdict())) #{"name": "Bob", "age": 25, "height": 5.8}

# creates shallow copy of object
new_person = person._replace(age=44)
print(new_person) #Person(name='Bob', age=44, height=5.8)

# _make() creates new instance of a namedtuple from a sequence or iterable
new_person2 = Person._make(['Praveen',40,167])
print(new_person2)
#======================================================
#   NamedTuple with Mixed and Optional Types

from typing import NamedTuple, Optional, List

class Employee(NamedTuple):
    name: str
    id: int
    skills: List[str]                 # List of skills
    manager: Optional[str] = None    # Optional manager field, defaults to None

# Create instances
employee1 = Employee(name="Charlie", id=101, skills=["Python", "SQL"])
employee2 = Employee(name="Diana", id=102, skills=["Java", "C++"], manager="Bob")

print(employee1)
# Employee(name='Charlie', id=101, skills=['Python', 'SQL'], manager=None)

print(employee2)
# Employee(name='Diana', id=102, skills=['Java', 'C++'], manager='Bob')

#===========================================================================
#  Adding Methods to NamedTuple

class Rectangle(NamedTuple):
    length: float
    width: float

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


# Create an instance
rect = Rectangle(length=5.0, width=3.0)

print(f"Area: {rect.area()}")  # Area: 15.0
print(f"Perimeter: {rect.perimeter()}")  # Perimeter: 16.0

"""
Key Benefits of typing.NamedTuple
    Explicit type annotations make the code self-documenting.
    You can add default values, methods, and custom behavior.
    Plays well with modern IDEs, linters, and type checkers like mypy.
"""









