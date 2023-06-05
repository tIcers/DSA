# Create a method that returns the nth last element of a singly linked list.  

# For example: given a linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5, return the 2nd to last element. The answer would be element 4.

# Two pointers movoing in parallel
def list_nth_last(linked_list, n):
    linked_list_as_list = [] # this is a empty list for appending nodes
    current_node = linked_list.head_node

    while current_node:
        linked_list_as_list.append(current_node)
        current_node = current_node.get_next_node()
    return linked_list_as_list[len(linked_list_as_list) - n]


# another approach

def nth_last_node(linked_list, n):
    tail_seeker = linked_list.head_node
    current = None
    count = 1

    while tail_seeker:
        tail_seeker = linked_list.get_next_node()
        count += 1
        if count >= n + 1:
            if current is None:
               current = linked_list.head_node
            else:
               current = current.get_next_node() 

    return current
