"""
Simple Queue implementation
"""

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

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

"""
Simple Graph Implementation
"""


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
        # self.vertices[vertex_id] = set()
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


def earliest_ancestor(ancestors, starting_node):
    """
    returns the earliest known ancestor - the one at the farthest distance from
    input individual
    """
    # would this be a traversal or search?
    # we are looking for the ancestor so maybe a search?

    # let's start with the beginning part
    # let's make the graph first :
    graph = Graph()

    for pair in ancestors:
        # add both vertices
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # add_edges in light of the pairs that are added at vertex
        graph.add_edge(pair[1], pair[0])
        # since we go from child to parent

    q = Queue()
    q.enqueue([starting_node])

    # since the connection between each node is exactly 1
    # initial length of 1
    max_connection_len = 1
    # also, if the ancestor does not have parents, that means that is the earliest_ancestor
    earliest_ancestor = -1

    # the queue has something in it
    while q.size() > 0:
        # we initialize the path
        path = q.dequeue()
        # get the node
        current_vertex = path[-1]
        # if the lenght of path is euqal to 1 i.e. path == max_connection_len
        if len(path) == max_connection_len:            # if it equal 1
            # if the value of the current vertex i.e. parent node in path is less than
            # the earliest_ancestor, then we update the earliest_ancestor to be the current vertex
            if current_vertex < earliest_ancestor:     # then check if the current value is less than -1
                earliest_ancestor = current_vertex
                max_connection_len = len(path)
        # if the length of the path is greater than the 1
        if len(path) > max_connection_len: #and v < earliest_ancestor) or (len(path) > max_connection_len):
            earliest_ancestor = current_vertex
            max_connection_len = len(path)
            # if there are two parents, we go to the lower one
# do not forget the adding neighbors part
        for neighbor in graph.vertices[current_vertex]:
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)

    return earliest_ancestor
    # we input a number
    # we check the neighbors of the number
    # if there  are neighbors
