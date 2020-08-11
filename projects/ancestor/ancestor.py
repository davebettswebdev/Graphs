class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    
    # create an empty queue and set path to list with starting node
    queue = Queue()

    path = [starting_node]

    # add path to queue
    queue.enqueue(path)

    # while the queue is not empty
    while queue.size() > 0:
        

    
