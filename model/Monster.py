class Monster:

    def __init__(self, monster_type):
        self.monster_type = monster_type
        self.initiative = 0
        self.toughness = 0
        self.attack = 0
        self.agility = 0

        if monster_type == "Giant_Spider":
            self.monster_type = monster_type
            self.initiative = 7
            self.toughness = 1
            self.attack = 2
            self.agility = 3

        if monster_type == "Skeleton":
            self.monster_type = monster_type
            self.initiative = 4
            self.toughness = 2
            self.attack = 3
            self.agility = 3

        if monster_type == "Orch":
            self.monster_type = monster_type
            self.initiative = 6
            self.toughness = 3
            self.attack = 4
            self.agility = 4

        if monster_type == "Troll":
            self.monster_type = monster_type
            self.initiative = 2
            self.toughness = 4
            self.attack = 7
            self.agility = 2
