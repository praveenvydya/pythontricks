### python functions are first class objects
# you can assign to a variable,
# store them in data structures
# pass them as arguments
# can return as values from other functions
def yell(text):
    return text.upper() + '!'
print(yell('praveen'))
bark = yell
print(bark('meenaa'))
del yell
#yell('Arjun')
# you cannot access yell as is undefined but still can access bark
print(bark('arjun'))
print(bark.__name__)

############### Functions can be stored in data structures  #######################
funcs = [bark,str.capitalize,str.lower]
print(funcs)
for f in funcs:
    print(f('Mounika'))

print(funcs[0]('raju'))

############### Functions can be passed to other functions #########################
def greert(func):
    greetings  = func('Hi, I\'m a python program')
    return greetings

print(greert(bark))

## higher order functions ##
li = list(map(bark,['hello','hey','hi']))
print(li)

############### Functions can be nested #########################

def speak(text):
    def whishper(t):
        return t.lower()+ '...'
    return whishper(text)

print(speak('Hello PRAVEEN'))

############### Functions can capture local State #########################
def get_speak_func(text, vol):
    def whisper():
        return text.lower()
    def yell():
        return text.upper()
    if vol==1:
        return whisper  # lexical closures or closures
    else:
        return yell

f = get_speak_func('Hello Praveen',0)
print(f())

# in practival terms this means not only can functions return behaviors but they can also pre-configure those behaviours .

def make_adder(n):
    def add(x):
        return x+n
    return add

# make_adder serves as factory
adder_3 = make_adder(3)
adder_5 = make_adder(5)

print(adder_5(50))
print(adder_3(30))

############### Objects can behave like functions #########################
# object can made callable by providing dunder __call__ method

class Adder:
    def __init__(self,n):
        self.n = n
    def __call__(self, x):
        return self.n+x

plus_3= Adder(3)
print(plus_3(30))

# chekc whether a object appears to be callable or not
print(callable(plus_3))



