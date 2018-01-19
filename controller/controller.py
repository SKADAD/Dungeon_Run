from controller.CombatController import CombatController
from model.AccountManager import *
from model.DungeonMap import *


class Controller:

    def __init__(self):
        self.character = ""  # Object of character
        self.character_hero = "Hero type"
        self.character_name = "Name"
        self.starting_pos = "NW"
        self.size_of_map = 1
        self.account_manager = AccountManager()
        self.dungeon_map = DungeonMap(5, "NW")

    # First game menu and choices, validates input and finally calls for the next function
    def start_menu(self):
        clear_cmd()
        # Load characters to self.list_of
        while True:
            
            # Returns true if choice is valid
            print("\n* Main Menu *")
            choice = validate(["New Character", "Existing Character(s)", "Statistics", "Quit game"])
            # If the return is valid
            if choice:
                # If user selected 1
                if choice == 1:
                    # Sends the user to menu create new char
                    self.menu_char_new()
                # If user selected 2
                elif choice == 2:
                    # Sends the user to menu load existing
                    self.menu_char_existing()
                elif choice == 3:
                    print("Statistics not yet implemented.")
                    self.start_menu()
                elif choice == 4:
                    self.quit_game()
                break

    # Create new character intro and finally calls new player name
    def menu_char_new(self):
        print("\nSelect hero class:")
        choice = validate(["Warrior", "Wizard", "Thief", "Return to main menu."])
        if choice:
            if choice == 1:
                self.character_hero = "Warrior"
            elif choice == 2:
                self.character_hero = "Wizard"
            elif choice == 3:
                self.character_hero = "Thief"
            elif choice == 4:
                self.start_menu()
            else:
                print("Unexpected.")
            # Sends the user to next menu
            self.menu_new_player_name()
        else:
            self.menu_char_new()

    # Create new name for new character and then saves to disk
    def menu_new_player_name(self):
        self.character_name = input("\nCharacter name:\n")
        if self.character_name == "":
            print("Blank name not allowed")
            self.menu_new_player_name()
        elif self.account_manager.create_new_character(self.character_name, self.character_hero):
            clear_cmd()
            print("\nCharacter " + self.character_name + ", The " + self.character_hero + " was born!")
            self.start_menu()
        else:
            print("\nCharacter name already exists! Try again.")
            self.menu_new_player_name()

    # User selects map size and set position function starts
    def menu_map_size(self):
        print("Select dungeon size:")
        choice = validate(["4 x 4 Grid (16 rooms)", "5 x 5 grid (25 rooms)", "8 x 8 grid (64 rooms)", "Return to main menu"])
        if choice:
            if choice == 1:
                self.size_of_map = 4
            elif choice == 2:
                self.size_of_map = 5
            elif choice == 3:
                self.size_of_map = 8
            elif choice == 4:
                self.start_menu()
            print("\nNumber of rooms in dungeon: " + str(self.size_of_map * self.size_of_map))
            self.menu_player_position()

    # Position is selected and map started
    def menu_player_position(self):
            print("\nChoose starting corner:")
            choice = validate(["North West", "North East", "South West", "South East", "Return to main menu"])
            if not choice:
                print("NOT VALID")
                self.menu_player_position()
            if choice:
                if choice == 1:
                    self.starting_pos = "NW"
                elif choice == 2:
                    self.starting_pos = "NE"
                elif choice == 3:
                    self.starting_pos = "SW"
                elif choice == 4:
                    self.starting_pos = "SE"
                elif choice == 5:
                    self.start_menu()
                self.dungeon_map = DungeonMap(self.size_of_map, self.starting_pos)
                self.present_game_start_info()

    # Before starting game, shows game selected info:
    def present_game_start_info(self):
        clear_cmd()
        print("* Game Information. *\n")
        print("Name: " + self.character_name)
        print("Hero Class: " + self.character_hero)
        print("Rooms to explore: " + str(self.size_of_map * self.size_of_map))
        print("Starting in corner: " + self.starting_pos)
        test = input("\nPress Enter to enter the dungeon or 0 to return to main menu\n")
        if test == "0":
            clear_cmd()
            self.start_menu()
        else:
            clear_cmd()
            self.player_movement()

    def menu_char_existing(self):
        is_empty = self.account_manager.get_list_of_names()
        if is_empty == []:
            print("\nNo characters in this account exists! Please create your first now.")
            self.menu_char_new()
        print("\nPick one of your characters:")
        choice = validate(self.account_manager.get_list_of_names())
        if not choice:
            self.menu_char_existing()
        elif choice == 0:
            self.start_menu()
        else:
            try:
                self.character = self.account_manager.list_of_characters[choice - 1]
                self.character_name = self.character.name
                print("\nSelected character: " + self.character_name + "\n")
                self.menu_map_size()
            except TypeError:
                self.menu_char_new()

    def to_print(self, string_to_print):
        clear_cmd()
        print(string_to_print)

    def quit_game(self):
        raise SystemExit

    def player_movement(self):
        while True:
            clear_cmd()
            print(self.dungeon_map.print_map())
            direction = input("Choose direction to move:\nW - Up, A - Left, S - Down, D - Right:\n").lower()
            if direction == "w" or "a" or "s" or "d":
                room = self.dungeon_map.move_player(direction)
                self.room_handler(room)
            else:
                print("fool, wrong step")

    def room_handler(self, room):
        # Kolla om det finns en utgång. Ge isf valet att avsluta.
        # Kolla ifall det finns några monster i rummet. Isf starta combat.
        # Lever spelaren så får den skatterna som finns i rummet.

        if room.is_exit:
            while True:
                print("There is an exit in the room. Do you wish to leave? Y/N")
                choice = input().lower()
                if choice == "y":
                    self.quit_game()
                    break
                elif choice == "n":
                    break
                else:
                    print("Must choose yes or no!")
                    continue

        if len(room.list_of_monsters) > 0:
            print("The room is populated with monsters! Defend yourself!")
            combat = CombatController(self, room.list_of_monsters)
            if combat.start():
                if not self.character.is_alive:
                    self.handle_death()
                    return
            else:
                return

        if len(room.list_of_treasures) > 0:
            print("*" * 10)

            money = 0
            print("Room items:")
            for var in room.list_of_treasures:
                print("treasure: " + str(var[0]))
                print("value: " + str(var[1]))
                money += var[1]
            self.character.amount_of_gold += money
            print("your character has gathered: " + str(self.character.amount_of_gold) + " this adventure")
            room.list_of_treasures = []
        time.sleep(2)

    def handle_death(self):
        print("You died, sorry...")
        self.quit_game()


def clear_cmd():
    import os
    import platform
    try:
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear')
            # Used for debugging in Pycharm IDE:
            print('\n' * 10)
        else:
            print('\n' * 10)
    except Exception:
        print("Clear failed")


# def validate is called from different menus when user input needs validation, takes menu choices as arguments:
def validate(list_of_choices):
    while True:
        # Enumerates each menu choice and then waits for user input:
        try:
            for i, choice in enumerate(list_of_choices):
                print(str(i + 1) + ". " + choice)
            choice = input()
            choice = int(choice)
            # Only return the users choice if its valid within the menus numbered choices:
            if 0 < choice <= len(list_of_choices):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("\nNot a valid choice! Please try again.")
            return False
        except TypeError:
            return False


# start = Controller()
# clear_cmd()
# start.start_menu()
