'''
inheirtance consisting of multiple types of inheritance is called hybrid inheritance
'''


class school:
    def func(self):
        print("This is func for school")

class student1(school):
    def func2(self):
        print("This is func2 for student1")
    
class student2(school):
    def fucn3(self):
        print("This is func3 for student2")
    
class student3(student1,student2):
    def func4(self):
        print("This is func4 for student3")
    
value = student3()
value.func()
value.func2()