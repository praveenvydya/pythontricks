# Python decorators allow you to extend and modify the behaviour of callable (functions , methods and classes) without perminantly modifying callable itself
# Logging
# enforcing access control and authentication
# instrumentation and timing
# rate-limiting
# caching and more
#
#
import functools


# The payoff for the understanding of decorators is enormous
#
# Functions are objects: they can be assigned to variables and passed to and returned from other functions
#
#  can be defined inside other functions and child function can capture the parent function's local state (lexical closures)

# Decorator is a callable that takes callable as input and returns another callable.

def null_decorator(func):
    return func

def greet():
    return 'Hello'

greet_fuc = null_decorator(greet)
print(greet_fuc())

@null_decorator
def greet_new():
    return 'Hello New'

print(greet_new())


# Decorators can modify behaviors
def uppercase(func):
    def wrapper():
        original_text = func()
        modfied_text = original_text.upper()
        return  modfied_text
    return wrapper

@uppercase
def sometext():
    return 'Hello Praveen'

print(sometext())

# Applying multiple decorators to a function
def header_appender(func):
    def wrapper():
        return '<h1>'+func() +'</h1>'
    return wrapper

@header_appender
@uppercase
def append():
    return 'Hi Meenaa'

print(append())

## Decorating functions that accept arguments
def proxy(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

#args = arguments collects extra positional arguments as tuple
#**kwargs = key word arguments ex: name='Meenaa' age='10' in functions as dictionary

def trace(func):
    def wrapper(*args,**kwargs):
        print(f'TRACE: calling {func.__name__}() ' 
              f' with  args:{args}  and kwargs:{kwargs}')
        original_result = func(*args,**kwargs)
        print(f'TRACE: function {func.__name__}() '
              f' returned {original_result}')
        return original_result;
    return wrapper

@trace
def say_name(f,name,line,special):
    return f'{name} : {line}   special: {special} and function   :{f}'

a = append()
# function should be passed as the first param
#print(say_name(a,'Praveen','Hello, World',special='Meenaa'))

#============================================================
def greet2(name,age):
    return f"Hello, {name} age: {age}!"

def call_func(func,*args,**kwargs):
    result = func(*args,**kwargs)
    return result

res  = call_func(say_name,a,'Praveen','Hello, World',special='Meenaa')
res = call_func(greet2,'Arjun',4)
print(res)

#============================================================
# Debuggable decorators


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet3():
    """Return a friendly greeting."""
    return 'Hello..'
g = greet3
print(g.__doc__)

#--------------------------------------------------
def func3(*args,**kwargs):
    if 'age' in kwargs:
        print(kwargs['age'])

def func2(*args,**kwargs):
    if 'name' in kwargs:
        print(kwargs['name'])
    func3(*args,**kwargs)

def func1():
    func2(age='5')

func1()
#-----------------------------------






