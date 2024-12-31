import dis

 ####  Old Style  ####
errorno = 50159747054
name = 'Praveen'

s = 'Hey %s there is an 0x%x error' %(name,errorno) #Hey Praveen there is an 0xbadc0ffee error
print(s)
s = 'Hey %(name)s there is an 0x%(error)x error' %{"name":name,"error":errorno}
print(s)

###  New Style  #### Python 3
s = 'Hey {} there is an 0x{:x} error'.format(name,errorno)
print(s)
s = 'Hey {name} there is an 0x{error:x} error'.format(name=name,error=errorno)   # format spec :x
print(s)


############################ New Styte Python 3.6+   ###
s = f'Hey {name} there is an 0x{errorno:x} error'

# behind scenes formated string literals are a python parser feature that converts f-strings into series of string constants and expressions.
# They get joined up to build final string
def greet(name,question):
    return f'Hello, {name}!. How it {question}?'

def greet_error(nam,error):
    return f'Hey {nam} there is an 0x{error:x} error'

# this similar to   "Hello,"+"name"+"!. How it "+"question"+"?"
#
print(greet_error(name,errorno))
print(greet('praveen','going'))
#Hello, praveen!. How it going?
# the real implemention is slitly faster than that because it uses the BUILD_STRING opcode as an optimization But functionally they are same

print(dis.dis(greet))
print(dis.dis(greet_error))



########################## Template Strings ###
from string import Template
t = Template('Hey $name there is an 0x$error error')
print(t.substitute(name=name,error=hex(errorno)))

