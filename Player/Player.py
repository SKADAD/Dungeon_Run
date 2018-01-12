class Player:

    def __init__(self):
        self.name = ""
        self.className = ""
        self.initiative = 0
        self.durability = 0
        self.attack = 0
        self.agility = 0

    def toString(self):
        return "|--------------|" + "\n"\
               "|Character Name|" + "\n" +\
               "|    " + self.name + "     |" + "\n"+ \
               "|    STATS     | " +"\n" \
               "| initiative: " + str(self.initiative) + "|"+"\n"+ \
               "| durability: " + str(self.durability) + "|"+"\n" + \
               "| Attack:     " + str(self.attack) + "|" +"\n"+ \
               "| Agility:    " + str(self.agility) + "|"

    def CharacterCreation(self, characterName_, choiceOfClass_):

        if choiceOfClass_ == "Warrior":
            self.name = characterName_
            self.className = choiceOfClass_
            self.initiative = 5
            self.durability = 9
            self.attack = 6
            self.agility = 4
            return "Welcome to Dungeon Run brave Warrior"

        elif choiceOfClass_ == "Wizard":
            self.name = characterName_
            self.className = choiceOfClass_
            self.initiative = 6
            self.durability = 4
            self.attack = 9
            self.agility = 5
            return "Welcome to Dungeon Run wise Wizard"

        elif choiceOfClass_ == "Thief":
            self.name = characterName_
            self.className = choiceOfClass_
            self.initiative = 7
            self.durability = 5
            self.attack = 5
            self.agility = 7
            return "Welcome to Dungeon Run you sneaky Thief"

        return "No class chosen"

    def SpecialAbility(self, typeOfClass):
        print("Special damage as " + typeOfClass)


Player1 = Player()
Player2 = Player()

EntryForName = input("Character Name")
EntryForClass = input("Classname")

print(Player1.className)
ReturnValue = Player1.CharacterCreation(EntryForName, EntryForClass)


#print(Player1.className)
print(ReturnValue)

print(Player1.toString())
