


def bfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    # create a queue
    q = Queue()

    q.enqueue([starting_vertex])

    visited = set()

    while q.size > 0:
        path = q.dequeue()    # dequeue the first path element
        v = path[-1]          # get the last vertex from the path

        if v not in visited:
            if v==destination_vertex:
                return path

            visited.add(v)

            for next_vertex in self.get_neighbors(v):
                new_path = path.copy()
                # bug where we reference the same path and we keep adding to the same path
                new_path.copy(next_vert)
            #   queue.enqueue([*path, neighbor])
                q.enqueue(new_path)
    return None
