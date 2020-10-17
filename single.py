class Singleton(object):
    __instance  = None
    
    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
        
        
a = Singleton(18, "yuanGe")
b = Singleton(8, "yuanGe")

print(id(a))
print(id(b))

a.age = 19
print(b.age)
