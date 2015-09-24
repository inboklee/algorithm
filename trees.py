class node:
        def __init__(self, x):
                self.key = x
                self.left = None
                self.right = None
                self.parent = None

class tree:
        def __init__(self):
                self.root = None

        def insert(self, x):
                if (self.root is None):
                        self.root = node(x)

        def insert_node(self, current, x):
                if (current.key > x):
                        if (current.left is not None):
                                self.insert_node(current.left, x)
                        else:
                                current.left = node(x)
                                current.left.parent = current
                else:
                        if (current.right is not None):
                                self.insert_node(current.right, x)
                        else:
                                current.right = node(x)
                                current.right.parent = current
