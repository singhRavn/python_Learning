''' when a class can be derived from more than one base class this type of inheritance is called multiple inheritance. in multiple inheritance, 
all the features of base class are inherited into derived class
'''

class Mother:
    mother_name = ""
    def mother(self):
        print(self.mother_name)

class Father:
    father_name = ""
    def father(self):
        print(self.father_name)

class child(Mother,Father):
    def Parent(self):
        print("Father:", self.father_name)
        print("Mother:", self.mother_name)

value = child()
value.father_name = "test1"
value.mother_name = "test2"
value.Parent()
