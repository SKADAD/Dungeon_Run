import random


class DungeonMap:

    def __init__(self, size_):
        self.list_of_rooms = []
        self.playerPosX = 0
        self.playerPosY = 0
        self.size = size_

    def generate_rooms(self):
        for i in range(self.size):
            for j in range(self.size):
                self.list_of_rooms.append(Room(i, j))

    def generate_exit(self):
        int_index = random.randrange(0, len(self.list_of_rooms))
        self.list_of_rooms[int_index].is_exit = True

    def generate_starting_pos(self, position):
        if position is "NW":
            self.playerPosX = 0
            self.playerPosY = 0
        elif position is "NE":
            self.playerPosX = self.size
            self.playerPosY = 0
        elif position is "SW":
            self.playerPosX = 0
            self.playerPosY = self.size
        elif position is "SE":
            self.playerPosX = self.size
            self.playerPosY = self.size
