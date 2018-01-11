import model.DungeonMap



class AccountManager:

    def __init__(self):
        self.character_new_name = "NewChar"
        self.character_load_name = "LoadChar"
        self.select_starting_pos = "NW"
        self.select_size_of_map = 5

    def select_new_or_existing_char(self):
        choice = int(input("Enter choice:\n 1. New Character \n 2. Existing Character"))
        if choice == 1:
            self.newChar()
        if choice == 2:
            self.existingChar()
        else:
            print("something wrong")

    def newChar(self):
        self.character_new_type = int(input("Enter character number:\n1. Knight\n2. Wizard\n3. Mage\n4. Thief\n"))
        self.character_new_name = input("Enter character name:\n")
        self.select_starting_pos = int(input("Enter starting position:\n1. North West\n2. North East\n3. South West\n4. South East\n"))
        if self.select_starting_pos == 1:
            self.select_starting_pos = "NW"
            print("NW")
        if self.select_starting_pos == 2:
            self.select_starting_pos = "NE"
            print("NE")
        if self.select_starting_pos == 3:
            self.select_starting_pos = "SW"
            print("SW")
        if self.select_starting_pos == 4:
            self.select_starting_pos = "SE"
            print("SE")
        self.select_size_of_map = int(input("Select size of map:\n1. Small\n2.Not too small and not too big\n3.Large"))
        if self.select_size_of_map == 1:
            self.select_size_of_map = 4
        if self.select_size_of_map == 2:
            self.select_size_of_map = 5
        if self.select_size_of_map == 3:
            self.select_size_of_map = 8

        print(self.character_new_type)
        print(self.character_new_name)
        print(self.select_starting_pos)
        print(self.select_size_of_map)

    def existingChar(self):
        print("Create new")

start = AccountManager()
start.select_new_or_existing_char()
