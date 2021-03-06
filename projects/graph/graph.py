"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue a starting vertex
        queue = Queue()
        queue.enqueue(starting_vertex)

        # create a set to store the visited vertices
        visited = {starting_vertex}

        # while the queue is not empty
        while queue.size() > 0:
            u = queue.dequeue()
            print(u)
            for v in self.get_neighbors(u):
                # if vertex has not been visited
                if v not in visited:
                    queue.enqueue(v)
                    # mark the vertex as visited
                    visited.add(v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push a starting vertex
        stack = Stack()
        stack.push(starting_vertex)

        # create a set to store the visited vertices
        visited = {starting_vertex}

        # while the stack is not empty
        while stack.size() > 0:
            # pop the first vertex
            u = stack.pop()
            print(u)
            for v in self.get_neighbors(u):
                # if vertex has not been visited
                if v not in visited:
                    stack.push(v)
                    # mark the vertex as visited
                    visited.add(v)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # create a set to store the visited vertices
        visited = {starting_vertex}

        def dft_print(starting_vertex):
            print(starting_vertex)
            for v in self.get_neighbors(starting_vertex):
                # if vertex has not been visited
                if v not in visited:
                    # mark the vertex as visited
                    visited.add(v)
                    dft_print(v)

        dft_print(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue PATH To the Starting Vertex ID
        queue = Queue()
        
        queue.enqueue([starting_vertex])
        
        # create a set to store visited vertices
        visited = set()
        
        # while the queue is not empty
        while queue.size() > 0:
            # dequeue the first PATH
            path = queue.dequeue()
            # grab the last vertex from the Path
            vert = path[-1]
            
            # is this vertex the target?
            if vert == destination_vertex:
                return path
            else:
                # check if the vertex has not been visited
                if vert not in visited:
                    print(vert)
                    # mark the vertex as visited
                    visited.add(vert)
                    # then add A Path to its neighbors to the back of the queue
                    back = self.get_neighbors(vert)
                    for next_vert in back:
                        # make a copy of the path
                        path_copy = list(path)
                        # append the neighbor to the back of the path
                        path_copy.append(next_vert)
                        # enqueue out new path
                        queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stck and push PATH To the Starting Vertex ID
        stack = Stack()
        stack.push([starting_vertex])
        
        # create a set to store visited vertices
        visited = set()
        
        # while the stack is not empty
        while stack.size() > 0:
            # pop off the first PATH
            path = stack.pop()
            # grab the last vertex from the Path
            vert = path[-1]
            
            # is this vertex the target?
            if vert == destination_vertex:
                return path
            else:
                # check if the vertex has not been visited
                if vert not in visited:
                    print(vert)
                    # mark the vertex as visited
                    visited.add(vert)
                    # then add A Path to its neighbors to the back of the queue
                    back = self.get_neighbors(vert)
                    for next_vert in back:
                        # make a copy of the path
                        path_copy = list(path)
                        # append the neighbor to the back of the path
                        path_copy.append(next_vert)
                        # push out new path
                        stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create a set to store visited vertices
        visited = set()
        # set empty path list
        path = []

        def search(starting_vertex, destination_vertex):
            # is this vertex the target?
            if starting_vertex == destination_vertex:
                path.insert(0, starting_vertex)
                return True
            
            for v in self.get_neighbors(starting_vertex):
                # check if the vertex has not been visited
                if v not in visited:
                    # add v to visited
                    visited.add(v)
                    if search(v, destination_vertex):
                        # Insert into path list
                        path.insert(0, starting_vertex)
                        return True
        
        search(starting_vertex, destination_vertex)
        return path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
