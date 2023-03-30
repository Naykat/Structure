class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class Heap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                curr = queue.pop(0)
                if curr.left is None:
                    curr.left = node
                    node.parent = curr
                    break
                elif curr.right is None:
                    curr.right = node
                    node.parent = curr
                    break
                else:
                    queue.append(curr.left)
                    queue.append(curr.right)
            self.heapify_up(node)

    def extract_min(self):
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            min_value = self.root.value
            self.root = None
            return min_value
        else:
            queue = [self.root]
            min_node = self.root
            while queue:
                curr = queue.pop(0)
                if curr.left is not None:
                    if curr.left.value < min_node.value:
                        min_node = curr.left
                    queue.append(curr.left)
                if curr.right is not None:
                    if curr.right.value < min_node.value:
                        min_node = curr.right
                    queue.append(curr.right)
            min_value = min_node.value
            self.delete(min_node)
            return min_value
        
    def delete(self, node: Node) -> None:
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            self.root = None
        else:
            queue = [self.root]
            while queue:
                curr = queue.pop(0)
                if curr is node:
                    last_node = self.get_last_node()
                    curr.value = last_node.value
                    self.delete_last_node(last_node)
                    break
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            self.heapify_down(curr)

    def get_last_node(self) -> Node:
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            return self.root
        else:
            queue = [self.root]
            last_node = self.root
            while queue:
                curr = queue.pop(0)
                if curr.left is not None:
                    last_node = curr.left
                    queue.append(curr.left)
                if curr.right is not None:
                    last_node = curr.right
                    queue.append(curr.right)
            return last_node

    def delete_last_node(self, node: Node) -> None:
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            self.root = None
        else:
            if node.parent.left is node:
                node.parent.left = None
            else:
                node.parent.right = None

    def heapify_up(self, node: Node) -> None:
        curr = node
        while curr is not self.root and curr.value < curr.parent.value:
            curr.value, curr.parent.value = curr.parent.value, curr.value
            curr = curr.parent

    def heapify_down(self, node: Node) -> None:
        curr = node
        while curr.left is not None or curr.right is not None:
            if curr.right is None or curr.left.value < curr.right.value:
                if curr.left is not None and curr.left.value < curr.value:
                    curr.value, curr.left.value = curr.left.value, curr.value
                    curr = curr.left
                else:
                    break
            else:
                if curr.right is not None and curr.right.value < curr.value:
                    curr.value, curr.right.value = curr.right.value, curr.value
                    curr = curr.right
                else:
                    break
