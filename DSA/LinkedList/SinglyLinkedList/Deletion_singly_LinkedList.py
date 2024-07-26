'''
Steps-by-step approach:

Check if the head is NULL.
    If it is, return NULL (the list is empty).
Store the current head node in a temporary variable temp.
Move the head pointer to the next node.
Delete the temporary node.
Return the new head of the linked list
'''

def removeFirstNode(head):
    if not head:
        return None
    temp = head

    head = head.next
    temp = None
    return head


'''
Deletion at the End of Singly Linked List:

Step-by-step approach:

Check if the head is NULL.
    If it is, return NULL (the list is empty).
Check if the heads next is NULL (only one node in the list).
    If true, delete the head and return NULL.
Traverse the list to find the second last node (second_last).
Delete the last node (the node after second_last).
Set the next pointer of the second last node to NULL.
Return the head of the linked list.

'''

def removeLastNode(head):
    if head is None:
        return None

    # If the list has only one node, delete it and return None
    if head.next is None:
        head = None
        return None

    # Find the second last node
    second_last = head
    while second_last.next.next is not None:
        second_last = second_last.next

    # Remove the last node
    second_last.next = None

    # Return the modified list
    return head

'''
Deletion at a Specific Position of Singly Linked List:

Step-by-step approach:

Check if the list is empty or the position is invalid, return if so.
If the head needs to be deleted, update the head and delete the node.
Traverse to the node before the position to be deleted.
If the position is out of range, return.
Store the node to be deleted.
Update the links to bypass the node.
Delete the stored node.

'''

def delete_at_position(head, position):
    if head is None or position < 1:
        return head

    # If the head needs to be deleted
    if position == 1:
        temp = head
        head = head.next
        temp = None
        return head

    # Traverse to the node before the position to be deleted
    current = head
    for i in range(1, position - 1):
        if current is not None:
            current = current.next
    # If the position is out of range
    if current is None or current.next is None:
        return head
    # Store the node to be deleted
    temp = current.next
    # Update the links to bypass the node to be deleted
    current.next = current.next.next
    # Delete the node
    temp = None
    return head
