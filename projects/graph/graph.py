"""
Simple graph implementation
"""
from .util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()   # create a set for vertices
        # add a vertex to the graph and we initialize it to empty set
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if the nodes do exist in the vertices
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)     # add something to a set.
        else:
            print('Error')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("ERROR: Vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        # Enqueue the starting vertex
        # create a set to store visited vertices
        # while the queue is not empty
            # queue the first vertex
            # check if it's been visited
                # mark it as visited
                # enqueue all it's neighbors

        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()
        while q.size() > 0:     # as long as the size is greater than 0, we continue dequeueing
            v = q.dequeue()     # dequeue the first element,
            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):     # add the neighbors in the queue
                    q.enqueue(neighbor)                    # then, we return to the queue since the size is greater than 0
# q = [3, 7, 6]
# we dequeue the 3 first, then, 7 and then, 6. and add the neighbors in the end of the list

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

            # create a stack
            # Push the starting vertex
            # create a set to store visited vertices
            # while the stack is not empty
                # stack the first vertex
                # check if it's been visited
                    # mark it as visited
                    # enqueue all it's neighbors
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # recursion: check if visited is empty, only then create a set.
        # otherwise we will be creating set throughout
        if visited is None:
            visited = set()

        # now check if the index is not in visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)        # add the index
            print(starting_vertex)              # print it
            for next_vertex in self.get_neighbors(starting_vertex):   # go to the next vertex i.e. in neighbors
                self.dft_recursive(next_vertex, visited)              # do recursion
        # let's set some base cases:



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        q = Queue()
        # put the starting_vertex in the queue
        q.enqueue([starting_vertex])
        # we create a set of visited, this ensures there is no repetition
        visited = set()
        # while the list size is greater than 0
        while q.size() > 0:
            path = q.dequeue()    # dequeue the first path element
            v = path[-1]          # get the last vertex from the path
            # check if it has been visited
            if v not in visited:
                if v==destination_vertex:   # if the last element in the path is equal to destination
                    return path             # we simply return the path
                # mark as visited
                visited.add(v)

                for next_vertex in self.get_neighbors(v):
                    new_path = path.copy()
                    # bug where we reference the same path and we keep adding to the same path
                    new_path.append(next_vertex)
                #   queue.enqueue([*path, neighbor])
                    q.enqueue(new_path)
                    # the new path contains the next_vertex's neighbors of v
                    # so we put
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a new stack
        s = Stack()
        # push the starting_vertex to the stack
        s.push([starting_vertex])
        # now stacks works with first in last out
        visited = set()
        # so while the size of the stack is greater than 0
        while s.size() > 0:         # while stack is not empty
            path = s.pop()        # we pop it out
            v = path[-1]          # take the last item from the path
            # check if it is not in visited
            if v not in visited:
                print(v)
                if v==destination_vertex:
                    return path
                # otherwise:
                visited.add(v)
                # for the neighbors now, unlike DFT, we will
                # add a path to its neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    new_path = path.copy()
                    new_path.append(next_vertex)
                    # add the new neighbors to the top of the stack and
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # init visited,
        # init path
        # add vertex to the path
        # if not in visited
        # we add it to visited
        # since recursion, we need to have base cases
        if visited is None:
            visited = set()

        # create a new path
        if path is None:
            path = []    # we do an array because it needs to be ordered.
            # set does not store the list in order
        # start with checking
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            # Add starting vertex to the path
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            # Check if starting vertex is equal to destination_vertex,
            if starting_vertex == destination_vertex:           # we return copied path
                return path_copy
            # Find neighbors of starting vertex
            for neighbor in self.get_neighbors(starting_vertex):
                # here's the recursive part comes in
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None
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

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
#    graph.bft(1)
    #
    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    graph.dft_recursive(1)
    #
    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))
    #
    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
