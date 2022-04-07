# Trees

## Introduction

The last section we'll cover is trees. A good example of a tree is your family tree on FamilySearch, where you are at the top of the tree and all of your ancestors are below you. There are 2 different kinds of trees: normal trees and binary search trees.

## How it works

The places where data is stored in trees are called nodes. Nodes can also be called root, parent, child, and leaf nodes. A root node is the node at the top of the tree. A parent node has at least one node below it and a child node has at least one node above it, but will only be directly connected to one parent node. A leaf node is a node that has no child nodes.

Normal trees, or binary trees, are trees where each node only has 2 child nodes. Binary search trees also only allow up to two child nodes per parent node, but will also balance the tree when necessary. A balanced tree means that each sub tree has pretty close to the same number of nodes.

The performance of a function using a tree can be improved through the use of recursion. Recursion is where you call back to the start of the function using the value previously calculated and either one more or one less of the original value used, depending on what your function is.

## Applicable Functions

These functions are not native to python, but they can either be downloaded from other developers who have created them, or you can write functions to implement them yourself.

**Insert**: The insert function adds data to the tree. The O notation for this function is O(log n) because each time a node is looked at to determine where the new one should go, half of the remaining tree is eliminated.

**Remove**: The remove function deletes data from the tree. The O notation for this function is O(log n) because you have to search the tree to find the node to remove, but half of the remaining tree is eliminated with each node looked at.

**Contains**: The contains function looks through the tree to see if certain data is in the tree. The O notation for this function is O(log n) because while searching through the tree to find the specified node, half of the remaininf tree is eliminated and doesn't have to be searched through.

**Traverse Forward**: The traverse forward function goes through every node on the tree from smallest to largest, typically using recursion. The O notation for this function is O(n) because you have to go through the entire tree.

**Traverse Reverse**: The traverse reverse function goes through every node on the tree from largest to smallest, also typically using recursion. The O notation for this function is also O(n) because you're still going through the whole tree, just in reverse.

**Height**: The height function returns the distance from the root to the furthest node. The O notation for this function is O(n) because you have to go through the entire tree to find out which node is the furthest from the root.

**Size**: The size function returns how many nodes there are in the tree. The O notation for this function is O(1) because the size of the tree is self contained.

**Empty**: The empty function returns whether there are any nodes in the tree or not. The O notation for this function is O(1) because you only have to check for the root node.

## Big O Notation

Trees are highly efficient because they allow you to eliminate half of the leftover tree at each node when you are searching for a specific number.

## Example code

Let's say you have a list of numbers that you need organized in the most effiecient way possible, so you decide to put them all into a BST. First, you'll need to make the BST and node classes, and then you'll need to write the insertion function.

```python
class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)
```

The first insert function adds the root node to the tree, while the second insert function adds all of the other nodes. However, you won't be able to print out each node in the tree without the traversal function.

## Example problem

You've been tasked with creating a tree to store the ISBN numbers of books that a library already has. You've been given the binary search tree base class and insertion function, but you'll need to write the function for traversal, and you'll need to modify the insertion function so that duplicate numbers won't be added to the tree. You'll also need this function for recursion to work:

```python
def __iter__(self):
    yield from self._traverse_forward(self.root)
```

If you decide to name your traversal function something different, don't forget to rename it in the `__iter__` function.

[Example solution file](tree-ex-solution.py)

[Previous section](2-sets.md)

[Back to start](0-welcome.md)