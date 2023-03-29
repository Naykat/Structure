class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def get_max(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, i):
        while i > 0:
            parent = self.parent(i)
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def extract_max(self):
        if len(self.heap) > 1:
            max_item = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._percolate_down(0)
            return max_item
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            return None

    def _percolate_down(self, i):
        left = self.left(i)
        right = self.right(i)
        largest = i
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._percolate_down(largest)
