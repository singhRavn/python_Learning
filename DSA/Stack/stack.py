'''
Linear data dtructure that stores items in Lastin Last out(LIFO) or first in Last out(FILO) Manner, in stack
a new element is added at one end and an element is removed from that end only.
the inset and delete operations are called push and pop

functions assocaited with stack are
empty() - Returns whether the stack is empty  - time complexity : O(1)
size()- Returns the size of the stack - Time Complexity :O(1)
top() - 
Push() - 
Pop - ()
'''

stack = []

stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)