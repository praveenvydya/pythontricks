#

class Dog:
    num_legs = 4  # <- class variable
    def __init__(self,name):
        self.name = name  # <- instance variable

    def __repr__(self):
        return f'Dog({self.name},{self.num_legs})'

d1 = Dog('Lucy')
d2 = Dog('Jack')
d3 = Dog('Jill')
print(d1, d2) # Dog(Lucy,4) Dog(Jack,4)
d1.num_legs = 2
print(d1, d2) # Dog(Lucy,2) Dog(Jack,4)

print(Dog.num_legs) # but not Dog.name
# Dog.num_legs = 6 modifies all objects
Dog.num_legs = 6
print(d1, d2,d3 ) # Dog(Lucy,6) Dog(Jack,6)
print(d1.__class__.num_legs,d2.__class__.num_legs,d3.__class__.num_legs )  #6 6 6
#===============================================================================

class CountedObject:
    num_instances = 0
    def __init__(self):
        self.__class__.num_instances+=1

print(CountedObject().num_instances) #1
print(CountedObject().num_instances) #2
print(CountedObject().num_instances) #3
print(CountedObject().num_instances) #4
print(CountedObject().num_instances) #5
print(CountedObject.num_instances) #6

class BuggyCountedObject:
    num_instances = 0
    def __init__(self):
        self.num_instances +=1

print(BuggyCountedObject().num_instances) #0
print(BuggyCountedObject().num_instances) #1
print(BuggyCountedObject().num_instances) #1
print(BuggyCountedObject().num_instances) #1
print(BuggyCountedObject.num_instances) # 0
# it correctly calculates the new value for the counter(going from 0 to 1). But then stores the result in an instance variable.
# which means other instance of the class never even see the updated counter value

# class variables can be "shadowed" by instance variables of the same name.


