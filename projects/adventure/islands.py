# write a function that takes a 2D binary array and
# return the number of 1 islands.
# an island consists of 1s that are connected to the
# north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]]

# island_counter(islands)   # returns 4

# 1. Translate the problem into terminology
# build the Graph
# traverse or search the graph

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

def island_counter(matrix):
    # create a visited matrix
    visited = []
    # height is based on the

    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))   # create a matrix that has all the nodes at False
        # because we have not visited any of the nodes yet.
    island_count = 0
    # for all nodes:
    for col in range(len(matrix[0])):    # walking through each column since matrix[0] returns each row so we get columns from [0, 0, 0, 0, 0]
        for row in range(len(matrix)):      # go through each row
            if not visited[row][col]:     # first stands for the row index and the second is for column index
                if matrix[row][col] == 1:
                    visited = dft(row, col, matrix, visited)
                    island_count +=1
    return island_count
        # id node is not visited:
            # if we hit a 1 that has not been visited:
                # mark visited
                # increment visited count
                # traverse all connected nodes, marking as visited
def dft(start_row, start_col, matrix, visited):
    # do a df traversal
    s = Stack()
    s.push((start_row, start_col))

    while s.size() > 0:
        v = s.pop()
        row = v[0]
        col = v[1]

        if not visited[row][col]:
            visited[row][col] = True

            # then push all the neighbors to the stack
            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)
    return visited
    # return an update visited matrix with all the marked visited boxes
def get_neighbors(row, col, matrix):
    '''
    Return a list of neighboring 1 tuple in the form of ([row, col])
    '''
    neighbors = []
    # check north
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append( (row-1, col) )
    # check south
    if row < len(matrix)-1 and matrix[row+1][col] == 1:
        neighbors.append( (row+1, col) )
    # check east
    if col < (len(matrix[0]) - 1) and matrix[row][col+1] == 1:
        neighbors.append( (row, col+1) )
    # check west
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append( (row, col-1) )

    return neighbors

print(island_counter(islands))
