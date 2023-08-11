from LinkedList import LinkedList

my_list = LinkedList()

my_list.insert_beginning("Node 1")
my_list.insert_beginning("Node 2")
my_list.insert_beginning("Node 3")
my_list.insert_beginning("Node 4")

found_node = my_list.find_node_iteratively("Node 3")
print(found_node.value)
