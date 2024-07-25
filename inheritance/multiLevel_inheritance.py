'''
features of base class and derived class are further inherited into new derived class.
This is similar to relationship representing a child and a grandfather.
'''

class Grand:
    def __init__(self,g_name):
        self.g_name = g_name

class Father(Grand):
    def __init__(self,f_name,g_name):
        self.f_name = f_name
        #invoking constructor of Grand
        Grand.__init__(self,g_name)

class Son(Father):

    def __init__(self,son_name,f_name,g_name):
        self.son_name = son_name

        #invoking constructor of father class
        Father.__init__(self,f_name,g_name)
    def print_name(self):
        print("gname", self.g_name)
        print("fname", self.f_name)
        print("son", self.son_name)

value1  = Son("test1","test2","test3")
print(value1.g_name)
value1.print_name()