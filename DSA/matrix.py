'''
2D array where each element is strictly the same size. to create a matrix we will be using numpy
'''

import numpy as np
a = np.array([[1,2,3,4],[4,55,1,2],[8,2,30,19],[11,2,33,21]])
m = np.reshape(a,(4,4))
print(m)

print("\nAccessing elements")
print(a[1])
print(a[2][0])

# adding element
m = np.append(m,[[1,15,13,11]],0)
print("\n Adding element")
print(m)

# Deleting element
m = np.delete(m,[1],0)
print("\n Deleting Element")
print(m)