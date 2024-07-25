class Pet:
    #__init__ is an constructor in python
    def __init__(self,name,age):
        self.name = name
        self.age = age

#Class newClass inheriting from the class Pet
# mechanism of inhereting properties of base class to child class.

class newClass(Pet):
    def __init__(self,name,age):
        #calling the super-class function __init__
        #using the super() function
        super().__init__(name,age)

def Main():
    value1 = Pet("Pet",1)
    value2 = newClass("Name",2)

    #isinstance() function to check whether a class is inherited from another class
    print("Is value2 a newclass?" +str(isinstance(value2,newClass)))
    print("Is value2 pet?" +str(isinstance(value2,Pet)))
    print("Is value1 a newclass?" +str(isinstance(value1,newClass)))
    print("Is value1 a Pet?" +str(isinstance(value1,Pet)))
    print(value2.name)

if __name__== '__main__':
    Main()