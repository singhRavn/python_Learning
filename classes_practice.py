
class MyClass:
    #assign values to MyClass attributes
    number = 0
    name = "TestsName"
def Main():
    #create object of MyClass
    #me is the object
    me = MyClass()
    
    # use . to acess attributes
    me.number = 1234
    me.name = "Learning"

    print(me.name + " " + str(me.number))

if __name__ == '__main__':
        Main()
