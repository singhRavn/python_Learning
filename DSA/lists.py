'''
Ordered collection of data, It allows to store different types of elements in list
Costliest Operation is inserting or deletion of element from begining of list as elements are needed to be shifted
'''

List = [1,2,3,"abc",6]
print(List)

'''
List elemnts can be accessed by assigned index. starting index of list is 0 and ending is N-1
'''

#Use of multiple values
List = ["value","for","money"]
print(List)

# Creating Multi Dimensional List (By nesting a list inside a List)
List2 = [["Values","for"],["money"]]
print(List2)

# Accessing a element from list using index number
print(List[0])
print(List[2])

# Accessing value using negative index
print(List[-1])

# print third last elemnt of List
print(List[-3])