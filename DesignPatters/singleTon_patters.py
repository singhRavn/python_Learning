'''
it ensures a class only has one instance and provides point of access to it.
'''

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    
#usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
