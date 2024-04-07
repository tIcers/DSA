class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def reverse(head):
        prev, curr = None, head

        while curr:
            nxt = curr.nextnode
            curr.nextnode = prev
            prev = curr
            curr = nxt
        return prev
