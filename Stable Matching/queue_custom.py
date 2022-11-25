class MyQueue():
    # Using Python Lists as a Queue
    def __init__(self):
        self.queue = []
    
    def empty(self):
        if(len(self.queue) == 0):
            return 1
        else:
            return 0

    def enqueue(self, value):
        # Inserting to the end of the queue
        self.queue.append(value)
 
    def dequeue(self):
         # Remove the furthest element from the top,
         # since the Queue is a FIFO structure
         return self.queue.pop(0)
    
    def printall(self):
        for data in self.queue:
            print(data)