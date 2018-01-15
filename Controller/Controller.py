import os
from model.DungeonMap import *

class Controller:

    def __init__(self):


    dungeonMap = DungeonMap()

    def toPrint(string_to_print):
        os.system('cls')
        print(string_to_print)


    def player_movement(direction):
        if direction.lower == "w" or "a" or "s" or "d":
            dungeonMap.move_player(direction)
        else:
            print("fool, wrong step")

    toPrint(dungeonMap.print_map())