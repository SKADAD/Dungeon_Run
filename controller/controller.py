from Account.AccountManager import AccountManager
from CombatController import CombatController
from model.DungeonMap import *


class Controller:

    def __init__(self):
        self.character = ""  # Object of character
        self.character_hero = "Hero Type"
        self.character_name = "Name"
        self.starting_pos = "NW"
        self.size_of_map = 1
        self.account_manager = AccountManager()
        self.dungeon_map = DungeonMap(5, "NW")

    # First game menu and choices, validates input and finally calls for the next function
    def start_menu(self):
        # Number of choices in the menu
        max_value_for_menu = 2
        # Clears the terminal:
        clear_cmd()
        print("Enter choice:\n 1. New Character \n 2. Existing Character\n")
        # Returns true if choice is valid
        choice = choice_validate_int(max_value_for_menu)
        if not choice:
            # Returns to start of this menu
            self.start_menu()
        # If the return is valid
        elif choice:
            # If user selected 1
            if user_input_number == 1:
                # Sends the user to menu create new char
                self.menu_char_new()
            # If user selected 2
            elif user_input_number == 2:
                # Sends the user to menu load existing
                self.menu_char_existing()

    # Create new character intro and finally calls new player name
    def menu_char_new(self):
        clear_cmd()
        max_value_of_menu = 3
        print("Choose hero by number:\n 1. Warrior\n 2. Wizard\n 3. Thief\n")
        choice = choice_validate_int(max_value_of_menu)
        if not choice:
            print("Invalid choice")
            self.menu_char_new()
        elif choice:
            if user_input_number == 1:
                self.character_hero = "Warrior"
            elif user_input_number == 2:
                self.character_hero = "Wizard"
            elif user_input_number == 3:
                self.character_hero = "Thief"
            else:
                print("Unexpected.")
            # Sends the user to next menu
            self.menu_new_player_name()
        else:
            print("Unexpected..")

    # Create new name for new character and starts map
    def menu_new_player_name(self):
        while True:
            self.character_name = input("Enter a character name:\n")
            if self.account_manager.create_new_character(self.character_name, self.character_hero):
                print("Character " + self.character_name + ", " + self.character_hero + " created!")
                self.start_menu()
                break
            else:
                print("Name already exists, try another")
# # TODO check if user name already exists
#         # If user doesnt exist already, initialize the player to save it:
#         newCharacter = Player(self.character_name, self.character_hero)
#         print(newCharacter.toString())
#         print(newCharacter)
# # TODO save character to account
#
#         print("Your new name is: " + self.character_name)
#         # Request next function, set map size
#         self.menu_map_size()

    # User selects map size and set position function starts
    def menu_map_size(self):
        while True:
            clear_cmd()
            max_value_of_menu = 3
            print("Select map size:\n 1. 16 rooms\n 2. 25 rooms \n 3. 64 rooms\n")
            choice = choice_validate_int(max_value_of_menu)
            # if not choice:
            #     clear_cmd()
            #     self.menu_map_size()
            # elif choice:
            if choice:
                if user_input_number == 1:
                    print("Choice =4")
                    self.size_of_map = 4
                elif user_input_number == 2:
                    self.size_of_map = 5
                elif user_input_number == 3:
                    print("Choice =8")
                    self.size_of_map = 8
                self.menu_player_position()
                break

    # Position is selected. The end is todo:
    def menu_player_position(self):
        while True:
            clear_cmd()
            max_value_of_menu = 4
            print("Enter starting position:\n 1. North West\n 2. North East\n 3. South West\n 4. South East\n")
            choice = choice_validate_int(max_value_of_menu)
            # if not choice:
            #     self.menu_player_position()
            # elif choice:
            if choice:
                if user_input_number == 1:
                    self.starting_pos = "NW"
                elif user_input_number == 2:
                    self.starting_pos = "NE"
                elif user_input_number == 3:
                    self.starting_pos = "SW"
                elif user_input_number == 4:
                    self.starting_pos = "SE"
                else:
                    print("Unexpected, selecting default:" + self.starting_pos)
                self.dungeon_map = DungeonMap(self.size_of_map, self.starting_pos)
                self.present_result()
                break


# TODO send character data from here

        else:
            print("Unexpected2")

    # Prints the choices made in menu, temporary fix:
    def present_result(self):
        print("Name: " + self.character_name)
        print("Hero Class: " + self.character_hero)
        print("Map Total Rooms: " + str(self.size_of_map * self.size_of_map))
        print("Map starting position: " + self.starting_pos)
        self.player_movement()

    # Load existing character
    def menu_char_existing(self):
        while True:
            name = input("Enter the name of you character or 0 to go back: \n")
            if name == "0":
                self.start_menu()
                break
            character = self.account_manager.get_character_by_name(name)
            if character:
                self.character = character
                print("Character " + name + " loaded.")
                self.menu_map_size()
                break
            else:
                print(name + " could not be found, please try again!")

# # TODO Look if char exists and if so load:
#
#         clear_cmd()
#         print("Choice 2, trying to load existing char..")

    def create_adventure(self, ):
        print("hi")


    def to_print(self, string_to_print):
        clear_cmd()
        print(string_to_print)

    def quit_game(self):
        raise SystemExit

    def player_movement(self):
        while True:
            print(self.dungeon_map.print_map())
            direction = input("Choose direction to go. w - up, a - left, s - down, d - right:\n")
            if direction == "w" or "a" or "s" or "d":
                room = self.dungeon_map.move_player(direction)
                self.room_handler(room)
            else:
                print("fool, wrong step")

    def room_handler(self, room):
        # Kolla om det finns en utgång. Ge isf valet att avsluta.
        # Kolla ifall det finns några monster i rummet. Isf starta combat. Lever spelaren så får den skatterna som finns i rummet.

        if room.is_exit:
            while True:
                print("There is an exit in the room. Do you wish to leave? y/n")
                choice = input()
                if choice == "y":
                    self.quit_game()
                    break
                elif choice == "n":
                    break
                else:
                    print("Must choose yes or no!")
                    continue

        if len(room.list_of_monsters) > 0:
            print("The room is populated with monsters! Defend youself!")
            combat = CombatController(self.character, room.list_of_monsters)
            combat.start()
            if not self.character.is_alive:
                self.handle_death()

        if len(room.list_of_treasures) > 0:
            print("You pick up treasures from the room: ")
            # TODO print out the treasures


# Clear CLI / GUI from lines when needed
def clear_cmd():
    # Import check type of OS win/lin
    try:
        print("\n\n\n\n")
    # disabled (debug mode on)
    # os.system('CLS')
    # os.system('clear')
    except:
        print("Tried to clear CLI but failed")


# Validates the users input when called
def choice_validate_int(highest_value_in_menu):
    # This global variable remembers the users selected number for menu if choice_validate first confirms True
    global user_input_number
    try:
        user_choice = int(input(""))
        # Choices in a menu is at minimum 1 and up to or as <number defined in the call to this function>
        if not (1 <= user_choice <= highest_value_in_menu):
            raise ValueError()
        else:
            # Else remember the number chosen (int)
            user_input_number = user_choice
            return True
    except ValueError:
        return False


start = Controller()
start.start_menu()
