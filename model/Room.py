import random


class Room:

    def __init__(self, x, y):

        self.mapPosX = x
        self.mapPosY = y
        self.list_of_monsters = [self.generate_treasures()]
        self.list_of_treasures = [self.generate_monsters()]
        self.visitedRoom = bool
        self.isExit = bool

    ''' Adjust for later:
    def generate_treasures(self):
        while True:
            # Create treasures by commoness:
            # random.randrange(0, self.size)
            generate_treasures = ["treasures"]
            self.list_of_treasures.append(generate_treasures)
            return self.list_of_treasures

    def generate_monsters(self):
        while True:
            generate_monster = ["monsters"]
            self.list_of_monsters = [generate_monster]
            return self.list_of_monsters
            '''

