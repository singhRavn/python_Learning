#enables dervived class to inherit properties from a single parent class, thus enabling code reusability and addition of new features to existing code

class Parent:
    def func(self):
        print("This is parent class")

# Derived Class

class Child(Parent):
    def func2(self):
        print("this is child class")

object = Child()
object.func()
object.func2()