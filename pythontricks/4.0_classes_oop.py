#1) object comparisons : "is"  vs "=="

# is => identical check -- expression evaluates to True if two variables point to the same(identical) object
# ==  > equality check - same content

a = [1,2,3]
b=a
print(a==b)#True
print(a is b) # False
c = [1,2,3]
print(c==a)#True
print(c is a) # False


d = list(c)
print(d==c) #True
print(d is c) # False

#=======
x = a
y = a
print(x==y) #True
print(x is y) #True
#==========================================

# Default 'to String method'

class Car:
    def __init__(self,name,color):
        self.name= name
        self.color = color

    def __str__(self): ## default dunder method
        return f'It is a {self.name} in {self.color} color'

    def __repr__(self): ## default dunder method
        return f'{self.__class__.__name__}({self.name!r},{self.color!r})'


car1 = Car('Honda','Red')
print(car1)
print(str(car1))
print(repr(car1)) # containers like lists and dicts always use the result of __repr__ to represent the object they contain
print('{}'.format(car1))
#============================================

import datetime
today = datetime.date.today()

print(str(today)) #2024-12-15
print(repr(today)) # datetime.date(2024, 12, 15)
print('{}'.format(str(today)))

# If you dont add __str__ method Python fals back on the result of __repr__ when looking for __str__ . It is recommended that always add at least __repr__ method to your classes.

"""result of __str__ should be readable
   result of __repr__ should be unambiguous """


