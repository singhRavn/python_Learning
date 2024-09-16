'''
Dict is unordered collection of Data that stores data in format of key:value pair.
it is like hash tables in any other language with time complexity O(1).
indexing of python dictonary is done with help of keys. these are of any hashable type i.e 
an object whose can never change like strings, number, tuples etc. 
'''

Dict = {"Name":"Value",
1:[1,2,3,4]}
print(Dict)

print(Dict["Name"])

print(Dict.get(1))

myDict = {x:x**2 for x in [1,2,3,4] }
print(myDict)

'''Nested Dict'''
Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(Dict)