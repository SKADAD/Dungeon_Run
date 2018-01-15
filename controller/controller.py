from model.DungeonMap import *

class Controller:
    dungeonMap = DungeonMap

    def toPrint(string_to_print):
        os.system('cls')
        print(string_to_print)


    def player_movement(direction):
        if direction == "w" or "a" or "s" or "d":
            DungeonMap.move_player(direction)
        else:
            print("fool, wrong step")
