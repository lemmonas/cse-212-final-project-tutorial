class BST:
    #Class to actually build a binary search tree.
    # This class will contain all of the functions to manipulate a BST.
    class Node:
        #Class to set up nodes in the tree
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        #Inserts the first piece of data
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        #Inserts the rest of the data
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        elif data == node.data:
            pass
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

    def __iter__(self):
        #Allows each item in the tree to be printed
        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):
        #Visits each item in the tree
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

#Example ISBN numbers to insert
books = BST()
books.insert(32856)
books.insert(53973)
books.insert(14837)
books.insert(34869)
books.insert(87385)
for x in books:
    print(x)