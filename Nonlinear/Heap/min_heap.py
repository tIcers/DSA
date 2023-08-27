class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def add(self, element):
        print(f"Adding {element} to {self.heap_list}")
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Restoring the heap property...")
