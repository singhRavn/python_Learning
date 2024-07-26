'''
Searching in single linked list refers to process of 
looking for a specific elemnt or value within elements of the linked list.

Steps
    1. Traverse Linked List starting from the head
    2. check if current node data macthes the target value.
            if a match is founf, return True
    3. Otherwise, move to next node and repeat step 2
    4. if the end is reached without finding a match, return false
'''

def Search_linked_list(head,target):
    while head is not None:
        if head.data == target:
            return True
        head = head.next
    return False