from node import Node

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        if self.head is None:
            return None
        return self.head.get_value()
