'''when more than one derived class are created from a single base
 this type of inheritance is called hierarchical inheritance.
'''

class Parent:
    def func1(self):
        print("This is func1")

class child1(Parent):
    def func2(self):
        print("This is func2")

class Child2(Parent):
    def func3(self):
        print("This is func3")
    
val1 = child1()
val2 = Child2()
val1.func1()
val1.func2()
val2.func1()
val2.func3()