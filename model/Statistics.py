class Statistics:

    def __init__(self):

        self.spiders_killed = 0
        self.skeletons_killed = 0
        self.orchs_killed = 0
        self.trolls_killed = 0

    def monster_killed(self, monster_type):

        if monster_type == "Giant_Spider":
            self.spiders_killed += 1

        elif monster_type == "Skeleton":
            self.skeletons_killed += 1

        elif monster_type == "Orch":
            self.orchs_killed += 1

        elif monster_type == "Troll":
            self.trolls_killed += 1