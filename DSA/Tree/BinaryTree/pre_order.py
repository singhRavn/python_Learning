'''
Pre-order Traversal is done by visiting the root node first,
then recursively do a pre-order traversal of the left subtree, 
followed by a recursive pre-order traversal of the right subtree.
It's used for creating a copy of the tree, prefix notation of an expression tree, etc.

'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
preOrderTraversal(root)
