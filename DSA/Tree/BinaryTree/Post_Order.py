'''
Postorder traversal is defined as a type of tree traversal which follows the Left-Right-Root policy such 
that for each node:

The left subtree is traversed first
Then the right subtree is traversed
Finally, the root node of the subtree is traversed


Postorder(root):

Follow step 2 to 4 until root != NULL
Postorder (root -> left)
Postorder (root -> right)
Write root -> data
End loop

'''

class Node:
	def __init__(self, v):
		self.data = v
		self.left = None
		self.right = None

def printPostorder(node):
	if node == None:
		return

	printPostorder(node.left)

	printPostorder(node.right)

	print(node.data, end=' ')


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(6)

	print("Postorder traversal of binary tree is:")
	printPostorder(root)
