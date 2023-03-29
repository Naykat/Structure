class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def search(self, data):
        if self.root is None:
            return False
        else:
            return self._search(data, self.root)

    def _search(self, data, node):
        if node is None:
            return False
        elif data == node.data:
            return True
        elif data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)
