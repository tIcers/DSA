class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1


    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Heapifying up")
        idx = self.count
        while self.parent_idx(idx) > 0:
            parent = self.heap_list[self.parent_idx(idx)]
            child = self.heap_list[idx]

            if parent > child:
                print(f"swapping {parent} with {child}")
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
            print(f'Heap Restored {self.heap_list}')

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None 
        min = self.heap_list[1]
        print(f"Removing {min} from {self.heap_list}")

        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list.pop()
        self.count -= 1
        print(f"Last element moved to first {self.heap_list}")
        self.heapify_down()
        return min

    def heapify_down(self):
        print("Heapifying down!")
        idx = 1

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        left_child = self.heap_list[self.left_child_idx(idx)]
        right_child = self.heap_list[self.right_child_idx(idx)]

        if left_child < right_child:
            print('left child is smaller than right child')
            return self.left_child_idx(idx)
        else:
            print('Right child is smaller')
            return self.right_child_idx(idx)

