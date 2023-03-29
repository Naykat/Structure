Код реализации Red-Black tree на Python:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        node.parent = None
        node.value = value
        node.left = None
        node.right = None
        node.color = "RED"

        if self.root is None:
            self.root = node
            node.color = "BLACK"
            return

        current = self.root
        parent = None
        while current is not None:
            parent = current
            if node.value < current.value:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def search(self, value):
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            elif current.value > value:
                current = current.left
            else:
                current = current.right

        return False

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is not None:            
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")

    def level_order_traversal(self):
        if self.root is None:
            return

        queue = []
        queue.append(self.root)

        while len(queue) > 0:
            current = queue.pop(0)
            print(current.value, end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    def delete(self, value):
        self.delete_node_helper(self.root, value)

    def delete_node_helper(self, node, value):
        # find the node containing the value
        z = None
        while node is not None:
            if node.value == value:
                z = node

            if node.value <= value:
                node = node.right
            else:
                node = node.left

        if z is None:
            print("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left is None:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is None:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = "BLACK"

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def maximum(self, node):
        while node.right is not None:
            node = node.right
        return node
