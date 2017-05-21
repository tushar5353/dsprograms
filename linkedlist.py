"""
Simple linked list program.
"""


class Node:
    def __init__(self, data, n = None):
        self.data = data
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n)
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList:
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = root
        while this_node:
            if this_node.get_data() == d
                return d
            else:
                this_node = this_node.get_next()
        return None
