class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None
  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)

  
  
root = BinarySearchTree(100)

root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)
