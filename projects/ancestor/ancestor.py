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
        # dequeue the first path
        curnent_path = queue.dequeue()
        # set the new path
        new_path = []
        # set changed to false 
        changed = False

        # start with node at the beginning of the path
        for node in curnent_path:
            # Loop through the ancestors 
            for ancestor in ancestors:
                # Look at each ancestor
                if ancestor[1] == node:
                    # append the ancestor to the new path
                    new_path.append(ancestor[0])
                    # set changed to true
                    changed = True
                    # enqueue out new path
                    queue.enqueue(new_path)

        # Loop through the final path to find value
        if changed is False:
            if curnent_path[0] == starting_node:
                return -1
            else:
                return curnent_path[0]
        

    
