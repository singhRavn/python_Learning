'''
Similar to lists but tuples are immutable in nature i.e
once created it cannot be modified. like list, tuple can also conatin various types of elemnts
'''

Tuple = ("Value","for")
print(Tuple)

# Creating a tuple with use of List
list1 = [1,2,3,4,5,4]
print(tuple(list1))
Tuple = tuple(list1)

# accessing the elemnts using indexing
print(Tuple[0])

# Accessing elents from last negative indexing
print(Tuple[-1])
print(Tuple[-4])