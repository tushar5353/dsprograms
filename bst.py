"""

Binary Search Tree
Author(s): Tushar Sharma<tushar5353@gmail.com>
A Data structure with will contain a node or parent having atmost two children(left/right).
if child > node then right_child else left_child

Code
****
It'll contain two classes Node and Tree and the whole concept of writing a BST code
revolves around instances such that every node is an instance.

e.g
Root node is an instance of Node Class and the very next node(left or right based on comparision)
again will be an instance of the Node Class


"""

class Node:
"""
Node class to instantiate every node
"""

    def __init__(self, val):
        self.value = val
        self.rightchild = None
        self.leftchild = None


    def insert(self, data):
    """
    data is the value for the new node.
    insert fnction is called recursively and the node 
    is placed on either left/right based on comparision.
    """
        if self.value == data:
            return False

        if self.value > data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
                return True


    def find(self, data):
    """
    same strategy as that of insert
    """
        if self.data = self.value:
            return True
        if self.value > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                return False
        
class Tree:
"""
Tree class to create a new Tree
"""
    def __init__(self):
        self.root = None

    def insert(self, data):
    """
    Basically this method will insert the nodes in a tree
    if root node is not present it will assign it a value
    and that will be the very first instane of the class Node
    Remember else part will be executed only once for a new Tree
    """
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True


    def find(self, data):
    """
    Function to find if a node exists in a tree or not.
    follows the same strategy as that of insert function
    Starting from the root node it will traverse the whole tree
    using comparision and will return True if that node is the
    item we are looking for.
    """
        if self.root:
            return self.root.find(data)
        else:
            return False

