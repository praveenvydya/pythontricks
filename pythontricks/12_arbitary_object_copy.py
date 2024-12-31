rimport copy


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r},{self.y!r})'

class Rectangle:
    def __init__(self,top_left,bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __repr__(self):
        return f'Rectangle({self.top_left!r},{self.bottom_right!r})'

p1 = Point(2,3)
p2 = Point(5,9)

rc = Rectangle(p1,p2)
print(rc)

rc1 =copy.copy(rc)
print(rc1==rc)
print(rc1 is rc)

print('----Changing point rc1 with shallow copy')
rc1.top_left.x = 99
print('rc: ',rc)
print('rc1: ',rc1)  # rc and rc1  are shallow copied both pointing to same reference


rc = Rectangle(p1,p2)
rc2 = copy.deepcopy(rc) # deep copy both rc and rd2 are independent objects
print('rc2: ',rc2)

print('')
print('----Changing point rc2 with deep copy')
rc2.top_left.x = 88
print('rc: ',rc)
print('rc2: ',rc2)

"""A deep copy of an object will be recursively clone child objects. The clone is fully independent of the original, but creating a deep copy is slower"""


