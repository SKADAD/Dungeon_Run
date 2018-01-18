import sys
sys.path.append('../')
from controller.controller import Controller
from model.DungeonMap import DungeonMap

dungeon = DungeonMap(8, "NE")

# while True:
#     dungeon.print_map()
#     direction = input("Enter a direction, w a s d: ")
#     if direction == "quit":
#         break
#     dungeon.move_player(direction)

controller = Controller()
controller.start_menu()
