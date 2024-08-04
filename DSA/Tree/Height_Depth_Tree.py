'''
Follow the steps below to find the depth of the given node:

If the tree is empty, print -1.
Otherwise, perform the following steps:
    Initialize a variable, say dist as -1.
    Check if the node K is equal to the given node.
    Otherwise, check if it is present in either of the subtrees, by recursively checking for the left and right subtrees respectively.
    If found to be true, print the value of dist + 1.
    Otherwise, print dist.


Follow the steps below to find the height of the given node:

If the tree is empty, print -1.
Otherwise, perform the following steps:
    Calculate the height of the left subtree recursively.
    Calculate the height of the right subtree recursively.
    Update height of the current node by adding 1 to the maximum of the two heights obtained in the previous step. Store the height in a variable, say ans.
    If the current node is equal to the given node K, print the value of ans as the required answer.
'''

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        
def findDepth(root, x):
  
    if (root == None):
        return -1

    dist = -1

    if (root.data == x):
        return dist + 1

    dist = findDepth(root.left, x)
    if dist >= 0:
        return dist + 1
    dist = findDepth(root.right, x)
    if dist >= 0:
        return dist + 1
    return dist

# Helper function to find the height
# of a given node in the binary tree
def findHeightUtil(root, x):
    global height

    if (root == None):
        return -1

    # Store the maximum height of the left and right subtree
    leftHeight = findHeightUtil(root.left, x)

    rightHeight = findHeightUtil(root.right, x)

    # Update height of the current node
    ans = max(leftHeight, rightHeight) + 1

    # If current node is the required node
    if (root.data == x):
        height = ans

    return ans

# Function to find the height of a given node in a Binary Tree
def findHeight(root, x):
    global height

    maxHeight = findHeightUtil(root, x)

    return height

if __name__ == '__main__':
  
    height = -1
    root = Node(5)
    root.left = Node(10)
    root.right = Node(15)
    root.left.left = Node(20)
    root.left.right = Node(25)
    root.left.right.right = Node(45)
    root.right.left = Node(30)
    root.right.right = Node(35)

    k = 25

    # Function call to find the depth of a given node
    print("Depth: ",findDepth(root, k))

    # Function call to find the height of a given node
    print("Height: ",findHeight(root, k))
