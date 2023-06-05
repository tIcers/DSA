# we have to find nodes to swap first

# I am going to start by setting node 1 equal to the head of the list, and then creating while 
# loop that runs while node 1 is not None
# inside we will check if node1's value mathces val1, if so we can break out of the loop 
# as we have found the correct node. if there is no match we update node1_prev to be node1 and move node1 to its next node


def swap_nodes(input_list, val1, val2):
    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev = None
    node2_prev = None

    while node1 is not None:
        if node1.get_value() = val1:
            break
        node1_prev = node1
        node1 = node1.get_next_value()

    while node2 is not None:
        if node2.get_value() = val2:
            break
        node2_prev = node2
        node2 = node2.get_next_value()
