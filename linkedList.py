class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # O(1) !!!
    def insert_start(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def remove(self, data):
        if self.head is None:
            return

        self.size = self.size - 1

        current_node = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.nextNode

        if previous_node is None:
            self.head = current_node.nextNode
        else:
            previous_node.next_node = current_node.nextNode

    # O(1) !!!
    def get_size(self):
        return self.size

    # O(N) !!!
    def insert_end(self, data):
        self.size = self.size + 1
        new_node = Node(data)
        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def traverse_list(self):
        actual_node = self.head

        while actual_node is not None:
            print("%d " % actual_node.data)
            actual_node = actual_node.nextNode


linkedList = LinkedList()

linkedList.insert_start(12)
linkedList.insert_start(122)
linkedList.insert_start(13)
linkedList.insert_end(31)

linkedList.traverse_list()
