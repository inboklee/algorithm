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
                else:
                        self.insert_node(self.root, x)

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
        def search(self, x):
                return self.search_node(self.root, x)

        def search_node(self, current, x):
                if (current is None):
                        return False
                else:
                        if (current.key == x):
                                return True
                        elif (current.key > x):
                                return self.search_node(current.left, x)
                        else:
                                return self.search_node(current.right, x)

