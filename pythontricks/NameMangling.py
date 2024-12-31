
_ManglingTest__g_mangled = 100

class ManglingTest:
    def __init__(self):
        self.__mangled='hello'
        self.__age = 42

    def get_mangled(self):
        return self.__mangled

    def __method_age(self): # ;like private
         return self.__age

    def get_age(self): # pubic and can be accessed in extended class
        return self.__method_age()

    def get_global(self):
        return __g_mangled


class ExtendedManglingTest(ManglingTest):
    def __init__(self):
        super().__init__()


t1 = ManglingTest()

t2 = ExtendedManglingTest()
print(dir(t1))

print(t1.get_age())
print(t2.get_age())
print(t2.get_mangled())
print(t1.get_global())

for _ in range(10):
    print(_, 'Yes')


