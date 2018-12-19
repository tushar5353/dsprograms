"""
simple binary tree
"""
"""
class BinaryTree():
    def __init__(self, rootid):
        self.rootid = rootid
        self.left = None
        self.right = None

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getRoot(self):
        return self.rootid

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = newNode
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left

    def insertRight(self, newNode):
        if self.right == None:
            self.right = newNode
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree


def traverseTree(tree):
    if tree != None:
        traverseTree(tree.getLeft())
        print(traverseTree(tree.getRoot()))
        traverseTree(tree.getRight())

myTree = BinaryTree('root')
myTree.insertLeft('Left1')
myTree.insertRight('Right1')
myTree.insertRight('Left2')

traverseTree(myTree)

"""

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())
            


# test tree

def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    myTree.insertRight("Steven1")
    printTree(myTree)

testTree()
