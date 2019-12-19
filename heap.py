CAPACITY = 10


class Heap():
    def __init__(self):
        self.heap = [0] * CAPACITY
        self.heap_size = 0

    def insert(self, item):
        if CAPACITY == self.heap_size:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1

        self.fix_up(self.heap_size - 1)

    def fix_up(self, index):
        parent_index = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def fix_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        index_largest = index

        if index_left < self.heap_size and self.heap[index_left] > self.heap[
            index]:
            index_largest = index_left

        if index_right < self.heap_size and self.heap[index_right] > self.heap[
            index_largest]:
            index_largest = index_right

        if index != index_largest:
            self.swap(index, index_largest)
            self.fix_down(index_largest)

    def get_max(self):
        return self.heap[0]

    def poll(self):

        max = self.get_max()

        self.swap(0, self.heap_size - 1)
        self.heap_size -= 1

        return max

    def heap_sort(self):

        size = self.heap_size

        for i in range(0, size):
            max = self.poll()
            print(max)

    def swap(self, index1, index2):
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[
            index2]
