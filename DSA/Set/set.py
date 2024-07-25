'''
mutaubale collection of data that does not allow duplication. Sets are basically used to include membership
testing and eliminate duplicate entries. The data structure used id Hashingm a popular technique to perform insetion, 
deletion and Traversal in O(1) an average

if multiple values are present at same position, then the value is appended to that index position ,
to form a Linked list. In CPython Sets are implemented using a dictionary with dummy variable, where key
being the members set with greater optimization to the time complexity
'''

Set  = set([1,2,3,"Value",4,"for",5,"Money"])
print(Set)

# accessing elements using for Loop
for i in Set:
    print(i,end = " ")
print()

# checking elements using "in" keyword
print("Value" in Set)
print("output" in Set)