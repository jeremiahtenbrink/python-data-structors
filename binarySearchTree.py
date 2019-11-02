class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data)

        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.remove_node(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.remove_node(data, node.rightChild)
        else:

            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return None

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)

        return node.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)

        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print("%s " % node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)
bst.insert(23)

bst.traverse()
