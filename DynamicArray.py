class DynamicArray:
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.array = self.create_array(self.capacity)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if not 0 <= index < self.length:
            return IndexError('Index is out of range!')
        return self.array[index]

    def append(self, item):
        if self.length == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.length] = item
        self.length += 1

    def resize(self, new_capacity):
        new_array = self.create_array(new_capacity)
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def create_array(self, capacity):
        return [None] * capacity
