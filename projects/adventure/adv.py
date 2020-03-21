from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()


player = Player(world.starting_room)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# keep track of all the moves the player makes:
path_traveled = []
# the most important dictionary!!!
reverse_directions = {'s':'n', 'n':'s', 'w':'e', 'e':'w'}

visited_rooms = {}
visited_rooms[0] = player.current_room.get_exits()
# let's add rooms to the visited_rooms dictionary
while len(visited_rooms) < len(room_graph)-1:
    # add the ids and exits:
    if player.current_room.id not in visited_rooms:
        # create adjacency lists for all the room ids
        visited_rooms[player.current_room.id] = player.current_room.get_exits()
        # print(visited_rooms)
        # get the last_move, since we initiated with room 0, the player can travel
        # in all four directions, so we get 'n' for last_move
        last_move = path_traveled[-1]
#        print(last_move)
        # remove this direction from the exits so that the stupid player would not move there anymore
        visited_rooms[player.current_room.id].remove(last_move)
        # print(visited_rooms)
    # after we have added all the rooms in the visited_rooms:
    while len(visited_rooms[player.current_room.id]) < 1:
        # get the last_direction
        reversal = path_traveled.pop()
        # we will want to put that in traversal path to keep track of moves we need to makes
        traversal_path.append(reversal)
        # then, we move in that direction
        player.travel(reversal)

    moving_dir = visited_rooms[player.current_room.id].pop(0)
    traversal_path.append(moving_dir)
    path_traveled.append(reverse_directions[moving_dir])
    player.travel(moving_dir)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
