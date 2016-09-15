import time

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def is_empty(self):
        return self.items == []

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class TowerOfHanoi:

    def towerOfHanoi(self, numberofdisks, startPeg=1, endPeg=3):
        time.sleep(0.70)
        if numberofdisks:
            self.towerOfHanoi(numberofdisks - 1, startPeg, 6-startPeg-endPeg)
            print("move disk %d from peg %d to peg %d"%(numberofdisks, startPeg, endPeg))
            self.towerOfHanoi(numberofdisks - 1, 6-startPeg-endPeg, endPeg)
