import model.DungeonMap
#import os

class AccountManager:

    def __init__(self):
        #self.character()
        self.character_new_name = "Name"
        self.character_load_name = "Name"
        self.select_starting_pos = "NW"
        self.select_char_type_new = "Class"
        self.select_size_of_map = 5

    # Wait for first input and print first menu:
    def start(self):
        self.choice_validator(input("Enter choice:\n 1. New Character \n 2. Existing Character\n"))

    # Try to validate user input and if OK send it to start_main_menu
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
            self.start()

    # Switch / Options in first menu:
    def start_main_menu(self, choice):
        switcher = {
            1: self.menu_char_new,
            2: self.menu_char_existing,
        }
        func = switcher.get(choice)
        return func()

    # Let the user create a new char:
    def menu_char_new(self):
        choice = int(input("Enter character number:\n1. Warrior\n2. Wizard\n3. Thief\n"))
        try:
            if not (1 <= choice <= 3):
                raise ValueError()
            else:
                if choice == 1:
                    self.select_char_type_new = "Warrior"
                elif choice == 2:
                    self.select_char_type_new = "Wizard"
                elif choice == 3:
                    self.select_char_type_new = "Thief"
                self.clear_cmd()
                self.character_new_name = input("Enter your characters name:\n")
# TODO1 check if user name already exists
# TODO2 save character after created
                controller.s
                s.load_character(TheUser)
                self.menu_map_size()
                return
        except ValueError:
            print("That isn't a valid choice.\nYou must enter a number from 0 to 4 to continue.")

    # User chooses map size before starting:
    def menu_map_size(self):
        self.clear_cmd()
        choice = int(input("Select size of map:\n1. Small\n2. Not too small and not too big\n3. Large\n"))
        try:
            if not(1 <= choice <= 3):
                raise ValueError()
            if choice == 1:
                self.select_size_of_map_input = 4
            elif choice == 2:
                self.select_size_of_map_input = 5
            elif choice == 3:
                self.select_size_of_map_input = 8
            self.menu_player_position()
        except ValueError:
            print("Not a valid number")
            self.menu_map_size()
# TODO3 Request map to be created etc with stored variables


    def menu_player_position(self):
        self.clear_cmd()
        select_starting_pos_input = int(input("Enter starting position:\n1. North West\n2. North East\n3. South West\n4. South East\n"))
        try:
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
        except:
            print("Wrong input")

        print(self.character_new_name)
        print(self.select_char_type_new)
        print(self.select_size_of_map)
        print(self.select_starting_pos)

    # Load existing character
    def menu_char_existing(self):
# TODO Look if char exists and if so load:

        self.clear_cmd()
        print("Choice 2, trying to load existing char..")

    # Clear CLI / GUI from lines when needed:
    def clear_cmd(self):
        try:
            print("\n\n\n\n\n\n\n\n\n\n\n")
            #os.system('CLR')
            #os.system('clear')
        except:
            print("Tried to clear CLI but failed")

start = AccountManager()
start.start()