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
