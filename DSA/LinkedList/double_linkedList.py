'''
Doubly Linked List (DLL) is a special type of linked list in which each node contains a 
pointer to the previous node as well as the next node of the linked list. 
In a Doubly Linked List, we can traverse in forward and backward direction using the 
next and previous pointer respectively.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def traverse(head):
    current = head
    while current:
      # Print current node's data
        print(current.data, end=" <-> ")
        # Move to the next node
        current = current.next
    print("None")


def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node


# Driver Code
head = None
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)

traverse(head)

