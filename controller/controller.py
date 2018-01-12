import model.DungeonMap
#import os

class AccountManager:

    def __init__(self):
        self.character_new_name = "Name"
        self.character_load_name = "Name"
        self.select_starting_pos = "NW"
        self.select_char_type_new = "Class"
        self.select_size_of_map = 5

    def start(self):
        self.choice_validator(input("Enter choice:\n 1. New Character \n 2. Existing Character\n"))

    def choice_validator(self, choice):
        self.clear_cmd()
        try:
            choice_input = int(choice)
            if not (1 <= choice_input <= 2):
                raise ValueError()
            else:
                self.start_main_menu(choice_input)
                return
        except ValueError:
            print("Not a valid choice. You must enter 1 or 2 to continue.")
            return False

    def start_main_menu(self, choice):
        switcher = {
            1: self.menu_char_new,
            2: self.menu_char_existing,
        }
        func = switcher.get(choice)
        return func()

    def menu_char_new(self):
        choice = int(input("Enter character number:\n1. Knight\n2. Wizard\n3. Mage\n4. Thief\n"))
        try:
            if not (1 <= choice <= 4):
                raise ValueError()
            else:
                if choice == 1:
                    self.select_char_type_new = "Knight"
                elif choice == 2:
                    self.select_char_type_new = "Wizard"
                elif choice == 3:
                    self.select_char_type_new = "Mage"
                elif choice == 4:
                    self.select_char_type_new = "Thief"
                self.clear_cmd()
                self.character_new_name = input("Enter your characters name:\n")
            # TODO save character
                self.menu_map_size()
                return
        except ValueError:
            print("That isn't a valid choice.\nYou must enter a number from 0 to 4 to continue.")

    def menu_map_size(self):
        self.clear_cmd()
        choice = int(input("Select size of map:\n1. Small\n2. Not too small and not too big\n3. Large\n"))
        try:
            if choice == 1:
                self.select_size_of_map_input = 4
            elif choice == 2:
                self.select_size_of_map_input = 5
            elif choice == 3:
                self.select_size_of_map_input = 8
            else:
                print("Not a valid input")
        except ValueError:
            print("Not a valid input")

        self.clear_cmd()
        select_starting_pos_input = int(input("Enter starting position:\n1. North West\n2. North East\n3. South West\n4. South East\n"))
        if select_starting_pos_input == 1:
            self.select_starting_pos = "NW"
            print("NW")
        elif select_starting_pos_input == 2:
            self.select_starting_pos = "NE"
            print("NE")
        elif select_starting_pos_input == 3:
            self.select_starting_pos = "SW"
            print("SW")
        elif select_starting_pos_input == 4:
            self.select_starting_pos = "SE"
            print("SE")
        else:
            print("Not a valid input")

        print(self.character_new_name)
        print(self.select_char_type_new)
        print(self.select_size_of_map)
        print(self.select_starting_pos)

    def menu_char_existing(self):
        # TODO this
        self.clear_cmd()
        print("Choice 2, trying to load existing char..")

    def clear_cmd(self):
        try:
            print("\n\n\n\n\n\n\n\n\n\n\n")
            #os.system('CLR')
            #os.system('clear')
        except:
            print("Tried to clear CLI but failed")

start = AccountManager()
start.start()