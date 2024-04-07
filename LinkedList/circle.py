class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def check_circle(node):
        slower = node
        faster = node

        while faster != None and faster.nextnode != None:
            slower = slower.nextnode
            faster = faster.nextnode.nextnode

            if slower == faster:
                return True
        return False
