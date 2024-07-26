'''
Steps:

Create a new node with the given value
Set the next pointer of the new node to the current head
Move the head to point to the new node
Return the new head of the linked list
'''

def insert_at_beginning(head,value):
    new_node = Node(value)
    # set the pointer to new node to the current
    new_node.next = head
    # move the head to point to new node
    head = new_node
    #  Return the new head of the linked list
    return head


'''
INSERT AT THE END OF SINGLY LINKED LIST

Steps:
 
Cretae a new node with the hiven value
check if the list is empty: 
     if it is, make the new node the head and return
Traverse the list until the last node is reached
Link the new node to current last node by setting the last node's next pointer to the new node    
'''

def insert_at_end(head,value):
    new_node = Node(value)

    # if the list is empty, make the new node the head
    if head is None:
        return new_node
    
    # Traverse the list until the last node is reached
    current = head
    while current.next is not None:
        current = current.next
    # Link the new node to current last node
    current.next = new_node
    return head

'''
INSERTION AT SPECIFIC POSITION OF SINGLY LINKED LIST
Steps:
Check if given position is valid
    if invalid, print "invalid position!" and exit.
Loop until pos reaches 0:
    if pos is 0:
        Create a new node with the given data.
        Set new node's next pointer to the current node.
        Update the current node to the new node
    else, move to the next node by updating the double pointer.
increment the size of linked list
'''

def insert_pos(current, pos, data):
  
    if pos < 1 or pos > size + 1:
        print("Invalid position!")
    else:
      
        # Keep looping until the pos is zero
        while pos > 1:
            if pos == 1:

                # adding Node at required position
                temp = Node(data)

                temp.next = current

                current = temp
            else:

                current = current.next
            pos -= 1
        size += 1
    return current
