class Player:

    def __init__(self, name, characterClass ):
        self.name = name
        self.characterClass = characterClass
        self.initiative = 0
        self.durability = 0
        self.attack = 0
        self.agility = 0
        self.warrior = False
        self.wizard = False
        self.thief = False


        if characterClass == "Warrior":
            self.initiative = 5
            self.durability = 9
            self.attack = 6
            self.agility = 4
            self.warrior = True

        elif  characterClass == "Wizard":
            self.initiative = 6
            self.durability = 4
            self.attack = 9
            self.agility = 5
            self.wizard = True

        elif  characterClass == "Thief":
            self.initiative = 7
            self.durability = 5
            self.attack = 5
            self.agility = 7
            self.thief = True


    def toString(self):
        return "|--------------|" + "\n"\
               "|Character Name|" + "\n" +\
               "|" + "t" + self.name + "|" + "\n"+ \
               "|Character class|" + "\n" + \
               "|" + "t" + self.characterClass + "|" + "\n" + \
               "|    STATS     | " +"\n" \
               "| initiative: " + str(self.initiative) + "|"+"\n"+ \
               "| durability: " + str(self.durability) + "|"+"\n" + \
               "| Attack:     " + str(self.attack) + "|" +"\n"+ \
               "| Agility:    " + str(self.agility) + "|"

