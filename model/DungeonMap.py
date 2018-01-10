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
                room = Room(i, j)
                # If the position is the same as the starting position, set no monsters and no treasure
                if i == self.playerPosX and j == self.playerPosY:
                    room.list_of_monsters = []
                    room.list_of_treasure = []
                self.list_of_rooms.append(room)

    def generate_exit(self):
        # Generate a random index in list range. Set exit to true, no monsters and no treasure
        while True:
            int_index = random.randrange(0, len(self.list_of_rooms))
            room = self.list_of_rooms[int_index]
            if not room.get_position == (self.playerPosX, self.playerPosY):
                break

        room.is_exit = True
        room.list_of_monsters = []
        room.list_of_treasure = []

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

