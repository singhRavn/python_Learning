'''
1. initalize the counter length to 0.
2. Start from the head of the list, assign it to current
3. Traverse the list:
    increment lenght for each node.
    Move to the next node(current = current->next)
4. Return final value of length
'''

def find_length(head):
    length = 0
    current = head
    # traverse the list and increment the length for each
    while current is not None:
        length += 1
        current = current.next
        
    # return the final length of linked list
    return length