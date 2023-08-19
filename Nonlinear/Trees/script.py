# Define your "TreeNode" Python class below
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing" + child_node.value + "from" + self.value)

        new_children = [child for child in self.children if child != child_node]
        self.children = new_children

    def traverse(self):
        print("Traversing...")
        nodes_to_visit = [self] 
        while len(nodes_to_visit) > 0 :
          current_node= nodes_to_visit.pop()
          print(current_node.value)
          nodes_to_visit+= current_node.children

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)
root.remove_child(bad_seed)
root.traverse()
