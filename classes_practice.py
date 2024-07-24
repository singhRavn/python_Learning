
class MyClass:
    number = 0
    name = "TestsName"
def Main():
    me = MyClass()
    me.number = 1234
    me.name = "Learning"

    print(me.name + " " + str(me.number))

if __name__ == '__main__':
        Main()
