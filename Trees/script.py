class TreeNode:
    def __init__(self, value) -> None:
        print("initializing node...")
        self.value = value
        self.children = []

    def add_child(self, children_node):
        print("Adding " + children_node.value)
        self.children.append(children_node)

    def remove_child(self, child_node):
        print("Removing " + child_node.value + "from" + self.value)
        new_children = []
        for child in self.children:
            if child != child_node:
                new_children.append(child)
            self.children = new_children

root = TreeNode("I am Root")
child = TreeNode("I am Child")

root.add_child(child)
