class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


my_node = Node(44)

print(my_node.get_value())

class LinkedList:
    def __init__(self, value = None):
        self.head_node = Node(value)
    def get_head_node(self):
        return self.head_node