class Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, node, newData):
        if node is None:
            node = Binary_Tree(newData)
            return node

        if newData < node.data:
            node.leftChild = node.insert(node.leftChild, newData)
        else:
            node.rightChild = node.insert(node.rightChild, newData)
        return node

    def contains(self, node, data):
        if node is None:
            return False
        else:
            if node.data == data:
                return True

            if data < node.data:
                node.contains(node.leftChild)
            else:
                node.contains(node.rightChild)

    def traverse_InOrder(self, node):
        if node is None:
            return
        else:
            node.traverse_InOrder(node.leftChild)
            print(node.data, end=" ")
            node.traverse_InOrder(node.rightChild)

    def traverse_PreOrder(self, node):
        if node is None:
            return
        else:
            print(node.data, end=" ")
            node.traverse_PreOrder(node.leftChild)
            node.traverse_PreOrder(node.rightChild)

    def traverse_PostOrder(self, node):
        if node is None:
            return
        else:
            node.traverse_PostOrder(node.leftChild)
            node.traverse_PostOrder(node.rightChild)
            print(node.data, end=" ")


if __name__ == "__main__":
    root = Binary_Tree(4)

    root.insert(root, 2)
    root.insert(root, 1)
    root.insert(root, 3)

    root.insert(root, 5)
    root.insert(root, 6)
    root.insert(root, 7)

    print("In-Order Traversal: [", end=" ")
    root.traverse_InOrder(root)
    print("]")

    print("Pre-Order Traversal: [", end=" ")
    root.traverse_PreOrder(root)
    print("]")

    print("Post-Order Traversal: [", end=" ")
    root.traverse_PostOrder(root)
    print("]")
