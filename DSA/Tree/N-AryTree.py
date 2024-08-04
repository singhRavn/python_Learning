'''
Algorithm
Here is the algorithm for finding the depth of an N-Ary tree:

1)Define a struct for the nodes of the N-ary tree with a key and a vector of pointers to its child nodes.
2)Create a utility function to create a new node with the given key.
3)Define a function depthOfTree that takes in a pointer to a Node and returns the depth of the tree.
4)If the pointer to the Node is null, return 0.
5)Initialize a variable maxdepth to 0.
6)Iterate through the vector of child nodes of the current Node and for each child node,
     recursively call depthOfTree function on the child and find the maximum depth.
7)Update the maxdepth variable to be the maximum of the current maxdepth and the depth of the child node.
8)Return the maxdepth plus 1 as the depth of the tree.
9)In the main function, create an N-ary tree and call depthOfTree function on the root node of the tree to get the depth.
10)Print the depth of the tree.
'''

class Node: 
	def __init__(self, key): 
		self.key = key 
		self.child = [] 

def new_node(key): 
	temp = Node(key) 
	return temp 

def depth_of_tree(ptr): 
	if ptr is None: 
		return 0

	maxdepth = 0
	for child in ptr.child: 
		maxdepth = max(maxdepth, depth_of_tree(child)) 

	return maxdepth + 1

# Driver program 
if __name__ == '__main__': 

	root = new_node('A') 
	root.child.extend([new_node('B'), new_node('F'), new_node('D'), new_node('E')]) 
	root.child[0].child.extend([new_node('K'), new_node('J')]) 
	root.child[2].child.append(new_node('G')) 
	root.child[3].child.extend([new_node('C'), new_node('H'), new_node('I')]) 
	root.child[0].child[0].child.extend([new_node('N'), new_node('M')]) 
	root.child[3].child[2].child.append(new_node('L')) 

	print(depth_of_tree(root)) 
