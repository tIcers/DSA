from node import Node

class Queue:

    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def peek(self):
        if self.is_empty():
            print("Nothing to see here!")
        else:
            if self.head is None:
                return None
            return self.head.get_value()

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0
