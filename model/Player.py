from model.Statistics import Statistics


class Player:

    def __init__(self, name, characterClass):
        self.name = name
        self.characterClass = characterClass
        self.initiative = 0
        self.durability = 0
        self.attack = 0
        self.agility = 0
        self.is_warrior = False
        self.is_wizard = False
        self.is_thief = False
        self.is_alive = True
        self.amount_of_gold = 0
        self.statistics = Statistics()

        if characterClass == "Warrior":
            self.initiative = 5
            self.durability = 9
            self.attack = 6
            self.agility = 4
            self.is_warrior = True

        elif characterClass == "Wizard":
            self.initiative = 6
            self.durability = 4
            self.attack = 9
            self.agility = 5
            self.is_wizard = True

        elif characterClass == "Thief":
            self.initiative = 7
            self.durability = 5
            self.attack = 5
            self.agility = 7
            self.is_thief = True

        self.max_durability = self.durability
        
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
        return_string = " INI = " + str(self.initiative) +\
                        " | DUR = " + str(self.durability) +\
                        " | ATT = " + str(self.attack) +\
                        " | AGI = " + str(self.agility) + " |"
        return return_string


def attributes(character_hero):
    if character_hero == "Warrior":
        return "\t| Initiative = 5 | Durability = 9 | Attack = 6 | Agility = 4 | Special = Shield Block |"
    elif character_hero == "Wizard":
        return "\t| Initiative = 6 | Durability = 4 | Attack = 9 | Agility = 5 | Special = Light Shine  |"
    elif character_hero == "Thief":
        return "\t| Initiative = 7 | Durability = 5 | Attack = 5 | Agility = 7 | Special = Critical hit |"
