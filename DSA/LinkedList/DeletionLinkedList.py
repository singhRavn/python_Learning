class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def delete_head(head):
  
    if head is None:
        return None

    temp = head
    head = head.next

    del temp

    return head


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list: ")
    print_list(head)
    head = delete_head(head)
    print("List after deleting the head: ")
    print_list(head)
