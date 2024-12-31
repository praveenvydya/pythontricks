""" ABC abstract base class"""
from abc import ABCMeta,abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

assert(issubclass(Concrete,Base))
print(issubclass(Concrete,Base))

c = Concrete()
"""TypeError: Can't instantiate abstract class Concrete without an implementation for abstract method 'bar'"""
# Abstract base ensures that derived classes implement particular methods from the base class at instantiation time