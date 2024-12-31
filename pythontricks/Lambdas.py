# Lambdas are single expression functions

add = lambda x,y:x+y
print(add(3,5))

print((lambda x,y:x*2)(5 ,6))

# When should we use lambda?
# anytime you are expected to suply funciton object

tuples = [(1,'d'),(2,'b'),(4,'a'),(3,'c')]
sorted_tuples = sorted(tuples,key=lambda x:x[1])
print(sorted_tuples)

sorted_numbers = sorted(range(-5,6),key= lambda x:x*x)
print(sorted_numbers)

dict_lambda = {'add':lambda x,y:x+y}
print(dict_lambda['add'](3,7))


# Just like nested function, lambdas also work as lexical-closures

def make_adder(n):
    return lambda x:x+n

adder_5 = make_adder(5)
adder_3 = make_adder(3)

print(adder_3(30))

# lambda functions cannot use regular statements and always include an implicit return statement
