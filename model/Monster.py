
class Monster:

    def __init__(self, monster_type):
        self.monster_type = monster_type

        if monster_type == "Giant_Spider":
            self.initiative = 7
            self.durability = 1
            self.attack = 2
            self.agility = 3

        elif monster_type == "Skeleton":
            self.initiative = 4
            self.durability = 2
            self.attack = 3
            self.agility = 3

        elif monster_type == "Orch":
            self.initiative = 6
            self.durability = 3
            self.attack = 4
            self.agility = 4

        elif monster_type == "Troll":
            self.initiative = 2
            self.durability = 4
            self.attack = 7
            self.agility = 2

    def toString(self):
        print("Monster type: " + self.monster_type + " Initiative: "+ str(self.initiative) +
              " toughness: "+ str(self.durability) + " attack: "+ str(self.attack)+ " agility: "+ str(self.agility))

    def short_string(self):
        return_string = self.monster_type + " (INI = " + str(self.initiative) +\
                        ", DUR = " + str(self.durability) +\
                        ", ATT = " + str(self.attack) +\
                        ", AGI = " + str(self.agility) + ")"

        return return_string
