def Reverse(data):
    #tcounitng from 100 to 1 by taking one(-1) step backward
    for i in range(len(data)-1,-1,-1):
        yield data[i]

def Main():
    rev  = Reverse("TestCase")
    for j in rev:
        print(j)
    data = "TestCase"
    print(list(data[i] for i in range(len(data)-1,-1,-1)))

if __name__=="__main__":
    Main()