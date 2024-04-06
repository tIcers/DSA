class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
print(a.nextnode.value)

# Pros
# Linked Lists have constant-time insertions and deletions in any positions, in comparison, arrays require O(n) time to do the same thing
# Linked Lists can continue to expand without having to specify their sieze ahead of time

# Cons
# To access an element in a linked list, you need to take O(k) time to go from the head of the list to the kth element.
# In contrast, arrays have constant time operations to access elements in an array
