import random
from model.Monster import Monster

class Room:

    def __init__(self):

        #self.mapPosX = x
        #self.mapPosY = y
        self.list_of_monsters = self.generate_monster()
        self.list_of_treasures = self.generate_treasure()
        self.visited_room = False
        self.is_exit = False
        # self.generate_treasure()
        # self.generate_monster()

    def generate_monster(self):
                                    # The rooms are populated with monsters accoring to occurance percent
        list_of_monsters = []
        value1 = random.randrange(0, 4)  # giant spider, 20% chance to apear
        if value1 == 0:
            spider = Monster("Giant_Spider")
            list_of_monsters.append(spider)

        value2 = random.randrange(0, 99)    # skeleton, 15%
        if value2 < 15:
            skeleton = Monster("Skeleton")
            list_of_monsters.append(skeleton)

        value3 = random.randrange(0, 9) # orch, 10%
        if value3 == 0:
            orch = Monster("Orch")
            list_of_monsters.append(orch)

        value4 = random.randrange(0, 19)    # troll, 5%
        if value4 == 0:
            troll = Monster("Troll")
            list_of_monsters.append(troll)

        return list_of_monsters

    def generate_treasure(self):
        list_of_treasure = []               # The placement of treasures are also calculated with correct randomness

        value1 = random.randrange(0, 99)    # 40% chance to apear in room
        if value1 < 40:
            cash = {"cash":2}
            list_of_treasure.append(cash)

        value2 = random.randrange(0, 4)     # 20% chance
        if value2 == 0:
            cash_bag = {"cash_bag": 6}
            list_of_treasure.append(cash_bag)

        value3 = random.randrange(0, 100)   # 15%
        if value3 < 15:
            gold = {"gold": 10}
            list_of_treasure.append(gold)

        value4 = random.randrange(0, 9)     # 10%
        if value4 == 0:
            gem = {"gem": 14}
            list_of_treasure.append(gem)

        value5 = random.randrange(0, 19)    # 5 %
        if value5 == 0:
            treasure_chest = {"treasure_chest": 20}
            list_of_treasure.append(treasure_chest)

        return list_of_treasure









