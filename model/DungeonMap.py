import random
import os, sys, time
sys.path.append('../')
from model.Room import Room


class DungeonMap:

    def __init__(self, size_, start_position):
        self.list_of_rooms = []
        self.playerPosX = 0
        self.playerPosY = 0
        self.size = size_
        self.last_position = () # last position as a tuple

        # print("Generating starting pos..")
        self.generate_starting_pos(start_position)
        # print("Generating rooms..")
        self.generate_rooms()
        # print("Generating exits..")
        self.generate_exit()

    def generate_rooms(self):
        for i in range(self.size):
            self.list_of_rooms.append([])
            for j in range(self.size):
                room = Room()
                # If the position is the same as the starting position, set no monsters and no treasure
                if i == self.playerPosY and j == self.playerPosX:
                    room.list_of_monsters = []
                    room.list_of_treasure = []
                    room.visited_room = True
                self.list_of_rooms[i].append(room)

    def generate_exit(self):
        # Generate a random index in list range. Set exit to true, no monsters and no treasure
        while True:
            int_x = random.randrange(0, self.size)
            int_y = random.randrange(0, self.size)
            if not self.playerPosX == int_x and not self.playerPosY == int_y:
                break

        room = self.list_of_rooms[int_y][int_x]
        room.is_exit = True
        room.list_of_monsters = []
        room.list_of_treasure = []

    def generate_starting_pos(self, position):
        if position is "NW":
            self.playerPosX = 0
            self.playerPosY = 0
        elif position is "NE":
            self.playerPosX = self.size - 1
            self.playerPosY = 0
        elif position is "SW":
            self.playerPosX = 0
            self.playerPosY = self.size - 1
        elif position is "SE":
            self.playerPosX = self.size - 1
            self.playerPosY = self.size - 1

    def print_map(self):
        string_to_print = ""
        for row in range(len(self.list_of_rooms)):
            for element in range(len(self.list_of_rooms[row])):
                if self.playerPosX == element and self.playerPosY == row:
                    string_to_print += "P "
                    continue
                room = self.list_of_rooms[row][element]

                if room.is_exit and room.visited_room:
                    string_to_print += "E "
                elif room.visited_room:
                    string_to_print += "O "
                else:
                    string_to_print += "X "
            string_to_print += "\n"
        return string_to_print
      
    def move_player(self, direction):

        # self.last_position = tuple(self.list_of_rooms[self.playerPosX][self.playerPosY])
        self.last_position = (self.playerPosY, self.playerPosX)

        if direction == "w":
            if self.playerPosY - 1 >= 0:
                self.playerPosY -= 1
        elif direction == "a":
            if self.playerPosX - 1 >= 0:
                self.playerPosX -= 1
        elif direction == "s":
            if self.playerPosY + 1 < self.size:
                self.playerPosY += 1
        elif direction == "d":
            if self.playerPosX + 1 < self.size:
                self.playerPosX += 1

        room = self.get_player_room()
        room.visited_room = True

        return room

    def get_player_room(self):
        return self.list_of_rooms[self.playerPosY][self.playerPosX]