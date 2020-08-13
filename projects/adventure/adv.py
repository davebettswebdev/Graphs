from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
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

# Create dictionary to store visited rooms
visited = {} 

# Add reverse path
reverse_path = [] 

# Add opposite directions
opposite_direction = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'} 

# Added starting locaiton to visited dictionary and get possible exits
visited[player.current_room.id] = player.current_room.get_exits()  

# If the rooms visited are less than the length of rooms graph
while len(visited) < len(room_graph):
    # Check to see if the room has been visited, if not...
    if player.current_room.id not in visited:
        # Add current room to visited and get exits
        visited[player.current_room.id] = player.current_room.get_exits() 
        # Access direction from reverse path
        prev_direction = reverse_path[-1]  
        # Remove pervious direction
        visited[player.current_room.id].remove(prev_direction)

    # If the length of the paths associated with the room is 0, then all the paths have been explored
    if len(visited[player.current_room.id]) == 0: 
        # Backtrack each previous room
        prev_direction = reverse_path[-1] 
        # Pop it from reverse path
        reverse_path.pop()
        # Append the previous direction to the traversal path   
        traversal_path.append(prev_direction) 
        # Move the plaer in the previous direction
        player.travel(prev_direction) 

    # If the lenght of the paths associated with the room is not 0, there are more directions to explore
    else: 
        # Assign the first available direction in the room to direction and pop it from the list
        direction = visited[player.current_room.id][-1] 
        visited[player.current_room.id].pop()
        # Append the direction to the traversal path 
        traversal_path.append(direction)
        # Append the opposite direction to the reverse path
        reverse_path.append(opposite_direction[direction])
        # Move the player in that direction 
        player.travel(direction) 
 

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
