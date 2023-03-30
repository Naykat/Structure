class Node:
    def __init__(self, value: int):
        self.value = value
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
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

    def fix_insert(self, node: Node):
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

    def left_rotate(self, node: Node):
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

    def right_rotate(self, node: Node):
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


    def search(self, value: int) -> Node:
        current = self.root
        while current is not None:
            if current.value == value:
                return current
            elif current.value > value:
                current = current.left
            else:
                current = current.right
        else:
            return None


    def traversal(self, node: Node):
        if node is not None:
            self.traversal(node.left)
            print(node.value, end=" ")
            self.traversal(node.right)

    def delete(self, value: int) -> None:
        node = self.root
        while node is not None:
            if value == node.value:
                break
            elif value < node.value:
                node = node.left
            else:
                node = node.right

        if node is None:
            return

        if node.left is not None and node.right is not None:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            node = successor

        if node.color == "RED":
            if node.left is None and node.right is None:
                if node.parent is not None:
                    if node == node.parent.left:
                        node.parent.left = None
                    else:
                        node.parent.right = None
                else:
                    self.root = None
            else:
                if node.left is not None:
                    child = node.left
                else:
                    child = node.right

                if node.parent is not None:
                    if node == node.parent.left:
                        node.parent.left = child
                    else:
                        node.parent.right = child
                    child.parent = node.parent
                else:
                    self.root = child
                    child.parent = None
                child.color = "BLACK"
        else:
            if node.left is None and node.right is None:
                if node.parent is not None:
                    self.__fix_double_black(node)
                    if node == node.parent.left:
                        node.parent.left = None
                    else:
                        node.parent.right = None
                else:
                    self.root = None
            else:
                if node.left is not None:
                    child = node.left
                else:
                    child = node.right

                if node.parent is not None:
                    if node == node.parent.left:
                        node.parent.left = child
                    else:
                        node.parent.right = child
                    child.parent = node.parent
                    self.__fix_double_black(child)
                else:
                    self.root = child
                    child.parent = None
                    child.color = "BLACK"
                    
    def __fix_double_black(self, node: Node) -> None:
        if node.parent is None:
            return

        sibling = self.__get_sibling(node)
        if sibling is None:
            self.fix_double_black(node.parent)
        else:
            if sibling.color == "RED":
                node.parent.color = "RED"
                sibling.color = "BLACK"
                if sibling == sibling.parent.left:
                    self.right_rotate(sibling)
                else:
                    self.left_rotate(sibling)
                self.fix_double_black(node)
            else:
                if (sibling.left is None or sibling.left.color == "BLACK") and \
                   (sibling.right is None or sibling.right.color == "BLACK"):
                    sibling.color = "RED"
                    if node.parent.color == "BLACK":
                        self.__fix_double_black(node.parent)
                    else:
                        node.parent.color = "BLACK"
                else:
                    if sibling == sibling.parent.left:
                        if sibling.right is not None and sibling.right.color == "RED":
                            sibling.right.color = "BLACK"
                            sibling.color = node.parent.color
                            self.left_rotate(sibling)
                            node.parent.color = "BLACK"
                        else:
                            sibling.color = "RED"
                            if sibling.left is not None:
                                sibling.left.color = "BLACK"
                            self.right_rotate(sibling)
                            self.__fix_double_black(node)
                    else:
                        if sibling.left is not None and sibling.left.color == "RED":
                            sibling.left.color = "BLACK"
                            sibling.color = node.parent.color
                            self.right_rotate(sibling)
                            node.parent.color = "BLACK"
                        else:
                            sibling.color = "RED"
                            if sibling.right is not None:
                                sibling.right.color = "BLACK"
                            self.left_rotate(sibling)
                            self.__fix_double_black(node)

    def __get_sibling(self, node: Node) -> Node:
        if node.parent is None:
            return None
        if node == node.parent.left:
            return node.parent.right
        else:
            return node.parent.left

    def minimum(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node

    def maximum(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node
