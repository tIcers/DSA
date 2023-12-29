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
