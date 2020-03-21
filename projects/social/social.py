import random
import time


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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # to create N random friendship,s create a list of all the possible avg_friendships
        # shuffle the list of friendships, and grab the first N elements.

        for i in range(num_users):
            self.add_user(f"Users{i+1}")    # creates empty adjacency list for 10 users

        # to  populate the graph
        # we create friendships
        # to create n random friendships,
        # we could create a list of all possible friendship combinations,
        # shuffle the list, and then graph the first few elements from the list .

        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

    #    print(possible_friendships)
        random.shuffle(possible_friendships)
    #    print(possible_friendships)
        # create_friendships create two friendships.

        # 1, 2, 3
        # would have :
        # (1, 2), (1, 3), (2, 3)
        # friendships
        # Add users
        # NOW, Let's slice friendships
        # create n friendships where n = avg_friendships * num_users//2
        for i in range(num_users * avg_friendships //2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # Write a for loop that calls create user the right amount of times
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            # Pick a random user
            user_id = random.randint(1, num_users)
            # Pick another random user
            friend_id = random.randint(1, num_users)
            # Try to create the friendship
            if self.add_friendship(user_id, friend_id):
                # If it works, increment a counter
                total_friendships += 2
            else:
                # If not, try again
                collisions += 1
        print(f"NUM COLLISIONS: {collisions}")



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # let's do the basic stuff we always start with:
        # we walk through every user and doing a traversal
        # and we also store the path from one user to the user we are going to

        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            new_id = path[-1]

            if new_id not in visited:

                visited[new_id] = path  # everything in the graph is a path
                # from the starting code.

                for neighbor in self.friendships[new_id]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

        return visited


# questions:
# 1. log(1000)/log(5)

if __name__ == '__main__':
    # sg = SocialGraph()
    # sg.populate_graph(1000, 5)
    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
    # print(len(connections) / 1000)
    # total = 0
    # for path in connections.values():
    #     total += len(path)
    # print(f"Avg degrees of separation = {total / len(connections) - 1}")
    num_users = 2000
    avg_friendships = 5
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    end_time = time.time()
    print("\n\n-----")
    print(f"Quadratic populate: {end_time - start_time} seconds")
    print("-----\n\n")
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph_linear(num_users, avg_friendships)
    end_time = time.time()
    print(f"Linear populate: {end_time - start_time} seconds")
