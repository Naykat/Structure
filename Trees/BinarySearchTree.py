class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else:
            print("Value already exists in the tree.")

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)

    def _search(self, value, current_node):
        if current_node is None:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

    def delete(self, value):
        if self.root is None:
            return

        self.root = self._delete(value, self.root)

    def _delete(self, value, current_node):
        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left = self._delete(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self._delete(value, current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                temp = self._find_min_node(current_node.right)
                current_node.value = temp.value
                current_node.right = self._delete(temp.value, current_node.right)

        return current_node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
