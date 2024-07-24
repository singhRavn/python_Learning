
class Vector2D:
    x = 0.0
    y = 0.0

    #creating a method names Set
    def Set(self,x,y):
        self.x = x 
        self.y = y

def Main():
    #Vec is an object of class Vector2D
    vec = Vector2D()

    #Passing values to the function set
    vec.Set(5,6)
    print("X: " + str(vec.x) + ", Y: " + str(vec.y))

if __name__ == '__main__':
    Main()