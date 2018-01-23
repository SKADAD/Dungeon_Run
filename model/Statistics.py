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

    def monster_killed_toString(self):
        return_string = ""
        return_string += "\nSpiders killed: " + str(self.spiders_killed)
        return_string += "\nSkeletons killed: " + str(self.skeletons_killed)
        return_string += "\nOrchs killed: " + str(self.orchs_killed)
        return_string += "\nTrolls killed: " + str(self.trolls_killed)

        return return_string

    def treasures_collected(self, list_of_treasures):

        for var in list_of_treasures:
            self.treasures.append(var)

    def treasure_toString(self):
        return_string = ""
        for var in self.treasures:
            return_string +="\nTreasure: " + str(var[0])
            return_string +=" Value: " + str(var[1])
        return return_string

    def room_count(self):
        # not implemented/connected yet
        self.rooms_visited += 1