import os
from model.DungeonMap import *


dungeonMap = DungeonMap()

def toPrint(string_to_print):
    os.system('cls')
    print(DungeonMap.string_to_print)


def player_movement(direction):
    if direction.lower == "w" or "a" or "s" or "d":
        dungeonMap.move_player(direction)
    else:
        print("fool, wrong step")
