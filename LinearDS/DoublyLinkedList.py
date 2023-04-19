class Node:
    def __init__(self, value, next_node=None, prev_node=None, head_node=None, tail_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
        self.head_node = head_node
        self.tail_node = tail_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value


class DoublyLinkedList:
    def __init__(self, head_node=None, tail_node=None):
        self.head_node = head_node
        self.tail_node = tail_node

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        else:
            self.tail_node == None
            self.tail_node = new_head
        self.head_node = new_head 
