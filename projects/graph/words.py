from util import Queue
# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
#
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

# what are the nodes and what are the edges?
# nodes are the words in the list, edges are the one word that would be changed.
# undirected graph because we can go back and forth
# dense or sparse? Sparse because there are so many words and have connections to only so many words_are_neighbors
# dense is when every word is connected to a majority of other words

# planning
# build our graph
# words are nodes, one-letter-apart edges
# Do a BFS from start word to end word

f = open('words.txt', 'r')    # r is for reading
words = f.read().split("\n")
f.close()

word_set =set()
for word in words:
    word_set.add(word.lower())
# print(len(word_set))
def get_neighbors(word):
    """
    return all words from word_list that are one letter different
    """

    neighbors = []
#    string_word = list(word)
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # foe each letter in the word,
    for i in range(len(word)):
        # for each letter in the alphabet
        for letter in alphabets:
            # change the word letter to the alphabet letter
            list_word = list(word)
            list_word[i] = letter
            w = "".join(list_word)
            if w != word and w in word_set:
                    neighbors.append(w)
            # if the new word is in word_set:
    return neighbors

print(get_neighbors("danish"))


def find_ladders(begin_word, end_word):
    # create a Queue
    # enqueue the starting word
    # create the visited set
    q = Queue()
    q.enqueue([begin_word])

    visited = set()

    # while the queue is not empty
    while q.size() > 0:
        # dequeue the next path
        path = q.dequeue()
        # grab the last word from the path
        v = path[-1]
        # check if the word is our end word, if so return path
        if v not in visited:
        # if it has not been visited
            if v== end_word:
                return path
        # mark it as visited
            visited.add(v)
        # enqueue a path to each neighbor
        for next_word in get_neighbors(v):
            next_path = path.copy()
            next_path.append(next_word)
            q.enqueue(next_path)

# find_ladders('sail', 'boat')
print(find_ladders("Elon", "Musk"))

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

# build the graph:
# load words from dictionary
# words = f.read().lower().split("\n")
# f.close()
#
# def get_neighbors(self):
#
#     result  =[]
#     pass
#
# def words_are_neighbors(w1, w2):
#
#     list_words = list(w1)
#
#     for i in range(len(list_word)):
