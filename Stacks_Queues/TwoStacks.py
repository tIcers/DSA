class Queue2Stacks(object):
    
    def __init__(self):
        
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        self.stack1.insert(0,element)
        self.stack2.insert(0,element)
    
    def dequeue(self):
        self.stack1.pop(0)
        self.stack2.pop(0)
        
