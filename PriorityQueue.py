class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((priority, item))

    def dequeue(self):
        if len(self.queue) > 0:
            min_index = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min_index][0]:
                    min_index = i
            return self.queue.pop(min_index)[1]
        else:
            return None

    def size(self):
        return len(self.queue)
