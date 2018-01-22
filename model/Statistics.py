class Statistics:

    def __init__(self):

        self.spiders_killed = 0
        self.skeletons_killed = 0
        self.orchs_killed = 0
        self.trolls_killed = 0
        self.treasures = []
        self.rooms_visited = 0

    def monster_killed(self, monster_type):

        if monster_type == "Giant_Spider":
            self.spiders_killed += 1

        elif monster_type == "Skeleton":
            self.skeletons_killed += 1

        elif monster_type == "Orch":
            self.orchs_killed += 1

        elif monster_type == "Troll":
            self.trolls_killed += 1

    def print_monster_killed(self):
        print("Spiders killed: " + str(self.spiders_killed))
        print("Skeletons killed: " + str(self.skeletons_killed))
        print("Orchs killed: " + str(self.orchs_killed))
        print("Trolls killed: " + str(self.trolls_killed))

    def treasures_collected(self, list_of_treasures):

        for var in list_of_treasures:
            self.treasures.append(var)

    def print_treasure(self):
        for var in self.treasures:
            print("Treasure: " + str(var[0]))
            print("Value: " + str(var[1]))

    def room_count(self):
        # not implemented/connected yet
        self.rooms_visited += 1