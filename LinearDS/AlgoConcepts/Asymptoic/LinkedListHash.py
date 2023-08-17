from hashmap import HashMap
from linkedlist import LinkedList

N = 6

#Insert Data Into HashMap
my_hashmap = HashMap(N)
my_hashmap.assign("Zachary", "Sunburn Sickness")
my_hashmap.assign("Elise", "Severe Nausea")
my_hashmap.assign("Mimi", "Stomach Flu")
my_hashmap.assign("Devan", "Malaria")
my_hashmap.assign("Gary", "Bacterial Meningitis")
my_hashmap.assign("Neeknaz", "Broken Cheekbone")

#Insert Data into LinkedList
my_linked_list = LinkedList(["Zachary", "Sunburn Sickness"])
my_linked_list.insert_beginning(["Elise", "Severe Nausea"])
my_linked_list.insert_beginning(["Mimi", "Stomach Flu"])
my_linked_list.insert_beginning(["Devan", "Malaria"])
my_linked_list.insert_beginning(["Gary", "Bacterial Meningitis"])
my_linked_list.insert_beginning(["Neeknaz", "Broken Cheekbone"])

hashmap_zachary_disease = my_hashmap.retrieve("Zachary")
print("Zachary's disease is {0}".format(hashmap_zachary_disease))
hashmap_runtime = "1"
print("The runtime of retrieving a value from a hashmap is O({0})\n\n".format(hashmap_runtime))


traverse = my_linked_list.get_head_node()

while traverse.get_value()[0] != "Zachary":
    traverse = traverse.get_next_node()
linked_list_zachary_disease = traverse.get_value()[1]
print("Zachary's disease is {0}".format(linked_list_zachary_disease))
linked_list_runtime = "N"
print("The runtime of retrieving the first value added to a linked list is O({0})\n\n".format(linked_list_runtime))
