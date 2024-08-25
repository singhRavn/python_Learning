class GFG:
    
    class Node:
        def __init__(self,n,data):
            self.children = [None]*n
            self.data = data
    
    def inorder(self, node):
        if node == None:
            return
        
        total = len(node.children)
        
        for i in range(total-1):
            self.inorder(node.children[i])
        
        print(node.data,end=" ")
        
        self.inorder(node.children[total-1])
    
    def main(self):
        
        n = 3
        root = self.Node(n, 1)
        root.children[0] = self.Node(n, 2)
        root.children[1] = self.Node(n, 3)
        root.children[2] = self.Node(n, 4)
        root.children[0].children[0] = self.Node(n, 5)
        root.children[0].children[1] = self.Node(n, 6) 
        root.children[0].children[2] = self.Node(n, 7)
        
        self.inorder(root)
        
ob = GFG()
ob.main() 

