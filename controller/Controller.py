from controller.CombatController import CombatController
from model.AI import Ai
from model.AccountManager import *
from model.DungeonMap import *
from model.Player import *

class Controller:

    def __init__(self):
        self.character = None  # Object of character
        self.character_hero = "Hero type"
        self.character_name = "Name"
        self.starting_pos = "NW"
        self.size_of_map = 1
        self.account_manager = AccountManager()
        self.dungeon_map = DungeonMap(5, "NW")

    # First game menu and choices, validates input and finally calls for the next function
    def start_menu(self):
        # Load characters to self.list_of
        while True:
            # Returns true if choice is valid
            print("\n* Main Menu *")
            choice = validate(["New Character", "Existing Character(s)", "AI Auto Play", "Statistics", "High Scores",
                               "Quit game"])
            # If the return is valid
            if choice:
                # If user selected 1
                if choice == 1:
                    # Sends the user to menu create new char
                    clear_cmd()
                    self.menu_char_new()
                # If user selected 2
                elif choice == 2:
                    # Sends the user to menu load existing
                    clear_cmd()
                    self.menu_char_existing()
                elif choice == 3:
                    clear_cmd()
                    player_ai_start()
                    if self.create_ai_class():
                        wait_time = self.select_wait_time_for_ai()
                        if wait_time == "exit":
                            continue
                        self.character = Ai(self.character_hero, wait_time)
                        self.character_name = self.character.name
                        self.menu_map_size()
                elif choice == 4:
                    clear_cmd()
                    statistics()
                elif choice == 5:
                    clear_cmd()
                    statistics_high_scores()
                elif choice == 6:
                    self.quit_game()
                break

    # Create new character intro and finally calls new player name
    def menu_char_new(self):
        print("\nSelect hero class:")
        choice = validate([" Warrior\t" + str(attributes("Warrior")), " Wizard\t" + str(attributes("Wizard")),
                           " Thief\t" + str(attributes("Thief")), "Return to main menu."])
        if choice:
            if choice == 1:
                self.character_hero = "Warrior"
            elif choice == 2:
                self.character_hero = "Wizard"
            elif choice == 3:
                self.character_hero = "Thief"
            elif choice == 4:
                clear_cmd()
                self.start_menu()
            else:
                print("Unexpected.")
            # Sends the user to next menu
            clear_cmd()
            print("Selected hero class: " + self.character_hero)
            self.menu_new_player_name()
        else:
            self.menu_char_new()

    # Create new name for new character and then saves to disk
    def menu_new_player_name(self):
        self.character_name = input("\nEnter character name or 0 to return:\n")
        if self.character_name == "":
            print("Blank name not allowed")
            self.menu_new_player_name()
        elif self.character_name == "0":
            print("Returning")
            self.menu_char_new()
        elif self.account_manager.create_new_character(self.character_name, self.character_hero):
            clear_cmd()
            print("\nCharacter " + self.character_name + ", The " + self.character_hero + " was born!")
            self.start_menu()
        else:
            print("\nCharacter name already exists! Try again.")
            self.menu_new_player_name()

    def create_ai_class(self):
        clear_cmd()
        while True:
            print("\nSelect class for the AI:")
            choice = validate(["Warrior", "Wizard", "Thief", "Return to main menu."])
            if choice == 1:
                self.character_hero = "Warrior"
                break
            elif choice == 2:
                self.character_hero = "Wizard"
                break
            elif choice == 3:
                self.character_hero = "Thief"
                break
            elif choice == 4:
                return False
        return True

    def select_wait_time_for_ai(self):
        clear_cmd()
        while True:
            print("Select AI delay after each room and combat, type ""exit"" to go back:")
            wait_time = input()
            if wait_time is "exit":
                return wait_time
            try:
                wait_time = int(wait_time)
                if wait_time > 20:
                    raise TypeError
                return wait_time
            except TypeError:
                print("Must enter a digit and must be lower then 20.\n")
                
    # User selects map size and set position function starts
    def menu_map_size(self):
        print("Select dungeon size:")
        choice = validate(["4 x 4 Grid (16 rooms)", "5 x 5 grid (25 rooms)", "8 x 8 grid (64 rooms)",
                           "Return to main menu"])
        if choice:
            if choice == 1:
                self.size_of_map = 4
            elif choice == 2:
                self.size_of_map = 5
            elif choice == 3:
                self.size_of_map = 8
            elif choice == 4:
                self.start_menu()
            clear_cmd()
            print("\nNumber of rooms in dungeon: " + str(self.size_of_map * self.size_of_map))
            self.menu_player_position()
        elif not choice:
            self.menu_map_size()

    # Position is selected and map started
    def menu_player_position(self):
        print("\nChoose starting corner:")
        choice = validate(["North West", "North East", "South West", "South East", "Return to main menu"])
        if not choice:
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
        print("* Game Start Information *")
        print("Name:\t\t" + self.character_name)
        print("Hero Class:\t" + self.character_hero)
        print("Selected Characters stats:" + self.character.short_string())
        print("Number of rooms: \t" + str(self.size_of_map * self.size_of_map))
        print("Starting corner: \t" + self.starting_pos)
        test = input("\nPress Enter to enter the dungeon or 0 to return to main menu\n")
        if test == "0":
            clear_cmd()
            self.start_menu()
        elif type(self.character) is Ai:
            clear_cmd()
            self.ai_movement()
        else:
            clear_cmd()
            self.player_movement()

    def menu_char_existing(self):
        list_of_existing_char = self.account_manager.get_list_of_names()
        if not list_of_existing_char:
            print("\nNo characters in this account exists! Please create your first now.")
            self.menu_char_new()
        list_of_existing_char.append("Return to main menu")
        print("\nPick one of your characters:")
        choice = validate(list_of_existing_char)
        if not choice:
            self.menu_char_existing()
        elif choice == len(list_of_existing_char):
            self.start_menu()
        else:
            try:
                self.character = self.account_manager.list_of_characters[choice - 1]
                self.character_name = self.character.name
                self.character_hero = self.character.characterClass
                clear_cmd()
                print("\nSelected character: " + self.character_name + "\n")
                self.menu_map_size()
            except TypeError:
                self.menu_char_new()
            except IndexError:
                print("Index Error! Try again")
                self.menu_char_existing()

    def to_print(self, string_to_print):
        clear_cmd()
        print(string_to_print)

    def quit_game(self):
        clear_cmd()
        quit_confirm = input("User requesting to quit game. Confirm with Y/N:\n ")
        if quit_confirm.lower() == 'y':
            print("\nQuitting game")
            raise SystemExit
        elif quit_confirm.lower() == 'n':
            self.start_menu()

    def player_movement(self):
        # Rensa och skriv ut kartan. Hämta möjliga moves från dungeon_map
        # Iterera över moves och skriv ut dessa. Vid korrekt input, flytta spelaren och hantera det nya rummet.

        while True:
            clear_cmd()
            print(self.dungeon_map.print_map())

            list_of_direction = []
            string_of_choices = self.dungeon_map.get_movement_choices()
            for char in string_of_choices:
                if char == "w":
                    list_of_direction.append("W - Up")
                elif char == "a":
                    list_of_direction.append("A - Left")
                elif char == "s":
                    list_of_direction.append("S - Down")
                elif char == "d":
                    list_of_direction.append("D - Right")

            # direction = input("Choose direction to move:\nW - Up, A - Left, S - Down, D - Right:\n").lower()
            direction = input("Choose direction to move:\n" + ", ".join(list_of_direction) + "\n").lower()
            if direction in string_of_choices:
                room = self.dungeon_map.move_player(direction)
                if self.room_handler(room) is "exit":
                    self.start_menu()
            else:
                print("fool, wrong step")

    def ai_movement(self):
        pass

    def room_handler(self, room):
        # Kolla om det finns en utgång. Ge isf valet att avsluta.
        # Kolla ifall det finns några monster i rummet. Isf starta combat.
        # Lever spelaren så får den skatterna som finns i rummet.
        clear_cmd()
        if room.is_exit:
            if type(self.character) is Ai:
                self.character.durability = self.character.max_durability
                print(self.character.summary_string())
                input("Press enter to continue")
                return "exit"
            clear_cmd()
            while True:
                print("There is an exit in the room. Do you wish to leave? Y/N")
                choice = input().lower()
                if choice == "y":
                    # TODO spara alla stats innan avslutar
                    self.character.durability = self.character.max_durability
                    self.account_manager.save_list_characters()
                    self.start_menu()
                    print("- Player found the exit and escaped!")
                    return "exit"
                elif choice == "n":
                    break
                else:
                    print("You must choose yes or no!")
                    continue

        if len(room.list_of_monsters) > 0:
            clear_cmd()
            print("The room is populated with monsters! Defend yourself!\n")
            combat = CombatController(self, room)
            if combat.start():
                if not self.character.is_alive:
                    self.handle_death()
                    return
            else:
                return

        if len(room.list_of_treasures) > 0:
            print("*" * 10)
            money = 0
            clear_cmd()
            print("Room items:")
            for var in room.list_of_treasures:
                print("Treasure: " + str(var[0]))
                print("Value: " + str(var[1]))
                money += var[1]
            self.character.amount_of_gold += money
            print("- Your character has gathered: " + str(self.character.amount_of_gold) + " gold in this room")
            room.list_of_treasures = []
            input("\nPress Enter to confirm and continue")
            self.character.statistics.treasures_collected(room.list_of_treasures)
            print("- Your character has gathered: " + str(self.character.amount_of_gold) + " gold in this room")
            room.list_of_treasures = []
            if type(self.character) is Ai:
                time.sleep(self.character.wait_time)
            else:
                input("\nPress Enter to confirm and continue")

    def handle_death(self):
        # TODO Set char as isDead = true and save
        print("You died, sorry...")
        self.quit_game()

        
def statistics():
    print("Want to show stats")


def statistics_high_scores():
    print("Statistics high score")


def player_ai_start():
    clear_cmd()
    hero_AI = input("Enter hero:\n")
    print("Hero choosen: " + hero_AI)
    number_of_rounds = input("Enter the number of games the AI should play: \n")
    print("Letting AI play " + number_of_rounds + " times. ")

    
def statistics(self):
    pass
    #self.character.statistics.monster_killed_toString()
    #self.character.statistics.treasure_toString()

    
def statistics_high_score():
    print("Statistics high score")


def play_with_ai():
    clear_cmd()
    print("1. ...")
    hero_AI = input("Enter a hero:\n")
    print("Hero choosen: " + hero_AI)
    number_of_rounds = input("Enter number of games the AI should play\n")
    print("Letting AI play " + number_of_rounds + " times")


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
            print("Plattform unknown but printing empty rows..")
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

