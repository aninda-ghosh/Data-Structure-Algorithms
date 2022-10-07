

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, value):
        #Tree should have atleast 1 node
        self.root = Node(value)   #Initialize with the value for that node
    
    def insert(self, node, value):
        if node is None:    #Check if the node already exists, if it doesn't then create one
            # print("Storing value {0}".format(value))
            node = Node(value)
            return node

        if(value < node.value):
            # print("Left Insert")
            node.left = self.insert(node.left, value)
        else:
            # print("Right Insert")
            node.right = self.insert(node.right, value)
        
        return node

    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            
            if(lheight > rheight):
                return lheight + 1
            else:
                return rheight + 1

    def print_current_level(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.value)
        elif level > 1:
            self.print_current_level(node.left, level - 1)
            self.print_current_level(node.right, level - 1)

            


    def bfs_recursive(self, node):
        height = self.height(node)
        for i in range (1, height+1):
            self.print_current_level(node, i)
    
    def bfs_queue(self, node):        
        if node is None:
            return
        
        queue = []

        queue.append(node)

        while len(queue) > 0:
            print(queue[0].value)
            node  = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)        


    def dfs_inorder(self, node):
        if node is None:
            return
        self.dfs_inorder(node.left)
        print("Node Value {0}".format(node.value))
        self.dfs_inorder(node.right)

    def dfs_preorder(self, node):
        if node is None:
            return
        print("Node Value {0}".format(node.value))
        self.dfs_preorder(node.left)
        self.dfs_preorder(node.right)

    def dfs_postorder(self, node):
        if node is None:
            return
        self.dfs_postorder(node.left)
        self.dfs_postorder(node.right)
        print("Node Value {0}".format(node.value))




if __name__ == "__main__":
    tree = Tree(4)
    tree.insert(tree.root, 2)
    tree.insert(tree.root, 6)
    tree.insert(tree.root, 1)
    tree.insert(tree.root, 3)
    tree.insert(tree.root, 5)
    tree.insert(tree.root, 7)

    print("\nInorder")
    tree.dfs_inorder(tree.root)
    print("\nPreorder")
    tree.dfs_preorder(tree.root)
    print("\nPostorder")
    tree.dfs_postorder(tree.root)

    print("\nRecursive BFS")
    tree.bfs_recursive(tree.root)
    
    print("\nBFS using queue")
    tree.bfs_queue(tree.root)
