'''
It is linear data structure, in which the elements are not sorted at contiguous memory locations. 
The elemnts in linked list are linked using pointers

A linked list is represented by a pointer to the first node of the linked list. the first node is called the head. if 
the linked list is empty then the balue of head is NULL. each node in a list consists of at least two parts
Data
Pointer to the next node
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None # initialize next as none

class LinkedList:
    # function to initialize Head
    def __init__(self):
        self.head = None

if __name__ == "main":
    # start emoty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head,next = second
    second.next = third

