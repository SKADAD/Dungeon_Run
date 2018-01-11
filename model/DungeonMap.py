import random


class DungeonMap:

    def __init__(self, size_, start_position):
        self.list_of_rooms = []
        self.playerPosX = 0
        self.playerPosY = 0
        self.size = size_

        self.generate_starting_pos(start_position)
        self.generate_rooms()
        self.generate_exit()

    def generate_rooms(self):
        for i in range(self.size):
            self.list_of_rooms.append([])
            for j in range(self.size):
                room = Room()
                # If the position is the same as the starting position, set no monsters and no treasure
                if i == self.playerPosX and j == self.playerPosY:
                    room.list_of_monsters = []
                    room.list_of_treasure = []
                self.list_of_rooms[i].append(room)

    def generate_exit(self):
        # Generate a random index in list range. Set exit to true, no monsters and no treasure
        while True:
            int_x = random.randrange(0, self.size)
            int_y = random.randrange(0, self.size)
            if not self.playerPosX == int_x and self.playerPosY == int_x:
                break

        room = self.list_of_rooms[int_x][int_y]
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

