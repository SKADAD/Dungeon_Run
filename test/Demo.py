import sys
sys.path.append('../')
from model.DungeonMap import DungeonMap

dungeon = DungeonMap(8, "NE")

while True:
    dungeon.print_map()
    direction = input("Enter a direction, w a s d: ")
    if direction == "quit":
        break
    previous_room = dungeon.get_player_room()
    dungeon.move_player(direction)
    current_room = dungeon.get_player_room()

