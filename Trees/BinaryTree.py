class BinarySearchTree:
    def __init__(self, value, depth=1) -> None:
        self.value = value
        self.depth = depth
        self.left = None
        self.right= None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value, self.depth + 1)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value, self.depth + 1 )
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if self.value == value:
            return self

        elif self.left and self.value > value:
            return self.left.get_node_by_value(value)
        elif self.right and self.value < value:
            return self.right.get_node_by_value(value)
        else:
            return None
    
    def depth_first_traversal(self):
        if self.left:
            self.left.depth_first_traversal()
        print(f'Depth={self.depth}, Value={self.value}')

        if self.right:
            self.right.depth_first_traversal()


tree = BinarySearchTree(48)
tree.insert(24)
tree.insert(55)
tree.insert(26)
tree.insert(38)
tree.insert(56)
tree.insert(74)

# Print depth-first traversal:
tree.depth_first_traversal()
