from model.Statistics import Statistics

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
        self.is_alive = True
        self.amount_of_gold = 0
        self.statistics = Statistics()

        if characterClass == "Warrior":
            self.initiative = 5
            self.durability = 9
            self.attack = 6
            self.agility = 4
            self.warrior = True

        elif characterClass == "Wizard":
            self.initiative = 6
            self.durability = 4
            self.attack = 9
            self.agility = 5
            self.wizard = True

        elif characterClass == "Thief":
            self.initiative = 7
            self.durability = 5
            self.attack = 5
            self.agility = 7
            self.thief = True

    def update_money(self):
        collected_money = self.amount_of_gold



    def toString(self):
        return "|" + "\t" + "Character Name" + "\t" + "|" + "\n" +\
               "|" + "\t" + self.name + "\t"  + "\t" + "\t" + "|" + "\n"+ \
               "|" + "Character class"+ "\t" + "|" + "\n" + \
               "|" + "\t" + self.characterClass + "\t" + "\t" + "\t" + "|" + "\n" + \
               "|" + "\t" + "STATS" + "\t" + "\t" + "\t" + "|" +"\n" \
               "|" + "Initiative:" + str(self.initiative) + "\t" + "\t" "|"+"\n"+ \
               "|" + "Durability:" + str(self.durability) + "\t" + "\t" "|"+"\n" + \
               "|" + "Attack:" + str(self.attack) + "\t"+ "\t"+ "\t" "|" +"\n"+ \
               "|" + "Agility:" + str(self.agility) + "\t"+ "\t"+ "\t" + "|"

    def short_string(self):
        return_string = "(INI = " + str(self.initiative) +\
                        ", DUR = " + str(self.durability) +\
                        ", ATT = " + str(self.attack) +\
                        ", AGI = " + str(self.agility) + ")"

        return return_string

