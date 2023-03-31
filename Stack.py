class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size

    def search(self, data):
        node = self.top
        position = 1
        while node is not None:
            if node.data == data:
                return position
            node = node.next
            position += 1
        return -1

    def clear(self):
        self.top = None
        self.size = 0
