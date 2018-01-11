import model.DungeonMap



class AccountManager:

    def __init__(self):
        self.character_new_name = "NewChar"
        self.character_load_name = "LoadChar"
        self.select_starting_pos = "NW"
        self.select_char_type_new = ""
        self.select_size_of_map = 5


    def select_new_or_existing_char(self):
        choice = int(input("Enter choice:\n 1. New Character \n 2. Existing Character"))
        if choice == 1:
            self.newChar()
        elif choice == 2:
            self.existingChar()
        else:
            print("Something wrong in select new or existing char")

    def newChar(self):
        select_char_new_type = int(input("Enter character number:\n1. Knight\n2. Wizard\n3. Mage\n4. Thief\n"))
        print(select_char_new_type)
        if select_char_new_type == 1:
            self.select_char_type_new = "Knight"
        elif select_char_new_type == 2:
            self.select_char_type_new = "Wizard"
        elif select_char_new_type == 3:
            self.select_char_type_new = "Mage"
        elif select_char_new_type == 4:
            self.select_char_type_new = "Thief"
        else:
            print("Something wrong in new Char")

        self.character_new_name = input("Enter character name:\n")

        select_size_of_map = int(input("Select size of map:\n1. Small\n2. Not too small and not too big\n3. Large\n"))
        print(select_size_of_map)
        if select_size_of_map == 1:
            self.select_size_of_map = 4
        elif select_size_of_map == 2:
            self.select_size_of_map = 5
        elif select_size_of_map == 3:
            self.select_size_of_map = 8
        else:
            print("Something wrong selecting map size")

        select_starting_pos = int(input("Enter starting position:\n1. North West\n2. North East\n3. South West\n4. South East\n"))
        if select_starting_pos == 1:
            self.select_starting_pos = "NW"
            print("NW")
        elif select_starting_pos == 2:
            self.select_starting_pos = "NE"
            print("NE")
        elif select_starting_pos == 3:
            self.select_starting_pos = "SW"
            print("SW")
        elif select_starting_pos == 4:
            self.select_starting_pos = "SE"
            print("SE")
        else:
            print("Something wrong selecting starting pos")

        print(self.character_new_name)
        print(self.select_char_type_new)
        print(self.select_size_of_map)
        print(self.select_starting_pos)

    def existingChar(self):
        print("Create new")

start = AccountManager()
start.select_new_or_existing_char()
