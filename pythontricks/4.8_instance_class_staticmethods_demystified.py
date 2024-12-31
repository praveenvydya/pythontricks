
class MyClass:
    cls_name = 'Lotus'
    def __init__(self):
        self.count = 50

    def method(self):
        return 'instance method called',self, self.cls_name , self.count

    @classmethod
    def class_method(cls):
        return 'class method called',cls.cls_name

    @staticmethod
    def static_method():
        return 'static method called'

    # instance method: take one parameter , self, which points to an instance of MyClass when the method is called.
    #                    can accept more than one parameter
    #                   self parameter can easily access all attributes and methods on the same object.
    #                   this gives lot power when it comes to modifying an object's state

    """
    Class Method:
            @classmethod decorator
            instead of accepting self , it takes cls parameter that points to that class not the object instance when method is called.
            since class method only has access to this cls argument , it can't modify object instance state.
            This would requires access to self. However class method can still modify class state that applies acros all instance of the class
            
    Static method:
            this method doesn't take self or cls parameter , it can made to accept arbitrary number of other parameters
            
    """

obj = MyClass()
print(obj.method()) # instance method called method has access to the object instance via the self argument

print(MyClass.method(obj)) #('instance method called', <__main__.MyClass object at 0x000001FBADF33A10>, 'Lotus')
print(obj.class_method())  # ('class method called', <class '__main__.MyClass'>)  * Python automatically passing class argument as first parameter

print(obj.static_method())

#print(MyClass.method()) # MyClass.method() missing 1 required positional argument: 'self'
print(MyClass.class_method())
print(MyClass.static_method())

