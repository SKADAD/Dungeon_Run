import sys
sys.path.append('../')
from model.DungeonMap import *
from model.Player import *
from controller.CombatController import *


class Controller:

    def __init__(self):
        self.character = None  # Object of character
        self.character_hero = "Hero type"
        self.character_name = "Name"
        self.starting_pos = "NW"
        self.size_of_map = 1
        self.account_manager = AccountManager()
        self.dungeon_map = DungeonMap(5, "NW")
        self.number_of_rounds = 0

    def start_menu(self):    # Main menu. User makes a choice and the appropriate function is called:
        while True:
            print("* Main Menu *")
            # Validate returns true if users selected choice is within the available choices, otherwise false
            choice = validate(["New Character", "Existing Character(s)", "AI Auto Play", "High Scores",
                               "Quit game"])
            clear_cmd()
            if choice:
                if choice == 1:
                    self.menu_char_new()
                elif choice == 2:
                    self.menu_char_existing()
                elif choice == 3:
                    self.menu_ai_class_select()
                elif choice == 4:
                    self.menu_statistics_high_scores()
                elif choice == 5:
                    self.menu_game_quit()

    # Create new character intro and finally calls new player name
    def menu_char_new(self):
        print("Select hero class:")
        choice = validate([" Warrior\t" + str(attributes("Warrior")), " Wizard\t" + str(attributes("Wizard")),
                           " Thief\t" + str(attributes("Thief")), "Return to main menu."])
        clear_cmd()
        if choice:
            if choice != 4:
                if choice == 1:
                    self.character_hero = "Warrior"
                elif choice == 2:
                    self.character_hero = "Wizard"
                elif choice == 3:
                    self.character_hero = "Thief"
                print("Selected hero class: " + self.character_hero)
                self.menu_new_player_name()
            elif choice == 4:
                self.start_menu()
        else:
            self.menu_char_new()

    # Create new name for new character and then saves to disk
    def menu_new_player_name(self):
        self.character_name = input("Enter character name or \"0\" to return (max 10 characters in name):\n")
        clear_cmd()
        if self.character_name == "":
            print("Blank name not allowed")
            self.menu_new_player_name()
        elif len(self.character_name) > 10:
            print("Name can not be longer then 10 characters")
            self.menu_new_player_name()
        elif self.character_name == "0":
            self.menu_char_new()
        elif self.account_manager.create_new_character(self.character_name, self.character_hero):
            print("\nCharacter " + self.character_name + ", The " + self.character_hero + " was born!")
            self.character = self.account_manager.get_character_by_name(self.character_name)
            self.menu_map_size()
        else:
            print("\nCharacter name already exists! Try again.")
            self.menu_new_player_name()

    def menu_ai_class_select(self): # AI Option select class
        print("Select hero class for the AI:")
        choice = validate(["Warrior", "Wizard", "Thief", "Return to main menu."])
        clear_cmd()
        if choice:
            if choice != 4:
                if choice == 1:
                    self.character_hero = "Warrior"
                elif choice == 2:
                    self.character_hero = "Wizard"
                elif choice == 3:
                    self.character_hero = "Thief"
                print("Selected AI Hero class: " + self.character_hero)
                self.menu_ai_select_wait_time()
            elif choice == 4:
                self.start_menu()
        else:
            self.menu_ai_class_select()

    def menu_ai_select_wait_time(self): # AI Option select delay
        print("Enter seconds to delay or type \"cancel\" to cancel:")
        wait_time = input()
        try:
            if str(wait_time.lower()) == "cancel":
                clear_cmd()
                self.menu_ai_class_select()
            wait_time = int(wait_time)
            if wait_time > 20:
                raise TypeError
            else:
                self.character = Ai(self.character_hero, wait_time)
                self.character_name = self.character.name
                clear_cmd()
                # self.menu_map_size()
                self.menu_ai_number_of_rounds()
        except (TypeError, ValueError):
            clear_cmd()
            print("\nYou must enter a digit lower then 20!\n")

    def menu_ai_number_of_rounds(self): # AI Option sets number of rounds AI should play
        number_of_rounds = input("Enter number of rounds AI should play or type \"cancel\" to cancel:\n")
        try:
            if number_of_rounds.lower() == "cancel":
                clear_cmd()
                return
            self.number_of_rounds = int(number_of_rounds)
            clear_cmd()
            print("Number of rounds AI will play: " + str(number_of_rounds))
            self.menu_map_size()
        except (TypeError, ValueError):
            clear_cmd()
            print("\nYou must enter a digit!\n")
            self.menu_ai_number_of_rounds()

    # User selects map size and set position function starts
    def menu_map_size(self):
        print("Select dungeon size:")
        choice = validate(["4 x 4 Grid (16 rooms)", "5 x 5 grid (25 rooms)", "8 x 8 grid (64 rooms)",
                           "Return to main menu"])
        clear_cmd()
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
        elif not choice:
            self.menu_map_size()

    # Position is selected and map started
    def menu_player_position(self):
        print("Choose starting corner:")
        choice = validate(["North West", "North East", "South West", "South East", "Return to select dungeon size"])
        clear_cmd()
        if not choice:
            self.menu_player_position()
        if choice:
            if choice != 5:
                if choice == 1:
                    self.starting_pos = "NW"
                elif choice == 2:
                    self.starting_pos = "NE"
                elif choice == 3:
                    self.starting_pos = "SW"
                elif choice == 4:
                    self.starting_pos = "SE"
                self.dungeon_map = DungeonMap(self.size_of_map, self.starting_pos)
                self.present_game_start_info()
            elif choice == 5:
                self.menu_new_player_name()

    # Before starting game, shows game selected info:
    def present_game_start_info(self):
        clear_cmd()
        print("* Game Start Information *")
        print("Name:\t\t" + self.character_name)
        print("Hero Class:\t" + self.character_hero)
        # print("Selected Characters stats:" + self.character.short_string())
        print("Number of rooms: \t" + str(self.size_of_map * self.size_of_map))
        print("Starting corner: \t" + self.starting_pos)
        test = input("\nPress Enter to enter the dungeon or \"0\" to return to main menu\n")
        clear_cmd()
        if test == "0":
            clear_cmd()
            self.start_menu()
        elif type(self.character) is Ai:
                for i in range(self.number_of_rounds):
                    print("New round")
                    self.ai_movement()
                    self.dungeon_map = DungeonMap(self.size_of_map, self.starting_pos)
                print(self.character.summary_string())
                input("Press Enter to return to main menu")
        else:
            self.character = self.account_manager.get_character_by_name(self.character_name)
            self.player_movement()

    # If user wants to play with existing character:
    def menu_char_existing(self):
        clear_cmd()
        list_of_existing_char = self.account_manager.get_list_of_names()
        if not list_of_existing_char:
            print("No characters in this account exists! Please create your first now.")
            self.menu_char_new()
        list_of_existing_char.append("Return to main menu")
        print("Pick one of your characters:")
        choice = validate(list_of_existing_char)
        if not choice:
            self.menu_char_existing()
        elif choice == len(list_of_existing_char):
            self.start_menu()
        else:
            try:
                self.character = self.account_manager.list_of_characters[choice - 1]
                if self.character.is_alive:
                    self.character_name = self.character.name
                    self.character_hero = self.character.characterClass
                    print("\nSelected character: " + self.character_name)
                    self.menu_map_size()
                else:
                    print("The character is dead, choose one that is alive or create a new.")
                    self.menu_char_existing()
            except TypeError:
                self.menu_char_new()
            except IndexError:
                print("Index Error! Try again")
                self.menu_char_existing()

    def menu_game_quit(self):    # If user request quit from Main Menu
        clear_cmd()
        quit_confirm = input("User requesting to quit game. Confirm with Y/N:\n ")
        clear_cmd()
        if quit_confirm.lower() == 'y':
            print("\nQuitting game. Bye!")
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
                    list_of_direction.append("W (Up)")
                elif char == "a":
                    list_of_direction.append("A (Left)")
                elif char == "s":
                    list_of_direction.append("S (Down)")
                elif char == "d":
                    list_of_direction.append("D (Right)")
            # direction = input("Choose direction to move:\nW - Up, A - Left, S - Down, D - Right:\n").lower()
            direction = input("Choose direction to move:\n" + ", ".join(list_of_direction) + "\n").lower()
            if direction in string_of_choices:
                room = self.dungeon_map.move_player(direction)
                if self.room_handler(room) is "exit":
                    self.finish_adventure()
                    self.start_menu()
            else:
                print("fool, wrong step")

    def ai_movement(self):
        # Ta reda på vilka riktningar som är möjliga. Slumpa ett index ifrån denna sträng och flytta AI
        while True:
            clear_cmd()
            print(self.dungeon_map.print_map())
            string_of_choices = self.dungeon_map.get_movement_choices()
            index = random.randrange(0, len(string_of_choices))
            direction = string_of_choices[index]
            room = self.dungeon_map.move_player(direction)
            if self.room_handler(room) is "exit":
                self.finish_adventure()
                self.character.is_alive = True
                return

    def room_handler(self, room):
        # Kolla om det finns en utgång. Ge isf valet att avsluta.
        # Kolla ifall det finns några monster i rummet. Isf starta combat.
        # Lever spelaren så får den skatterna som finns i rummet.
        if room.is_exit:
            if type(self.character) is Ai:
                clear_cmd()
                return "exit"
            clear_cmd()
            while True:
                #self.update_visited_rooms()
                print(self.character.summary_string_dungeon())
                # print(Player.summary_string_dungeon(self.character))
                exit_confirm = input("User found the exit! Do you want to leave dungeon? \nConfirm with Y/N:\n ").lower()
                if exit_confirm == "y":
                    # rooms_visited = self.dungeon_map.get_number_of_visited_rooms()
                    # self.character.statistics.room_count(rooms_visited)
                    # self.character.durability = self.character.max_durability
                    # self.account_manager.save_list_characters()
                    clear_cmd()
                    print("- Player found the exit and escaped!\n")
                    return "exit"
                elif exit_confirm == "n":
                    return
                else:
                    print("You must choose yes or no!")
                    continue

        if len(room.list_of_monsters) + len(room.list_of_treasures) == 0 and type(self.character) is Ai:
            time.sleep(self.character.wait_time)

        if len(room.list_of_monsters) > 0:
            clear_cmd()
            print("The room is populated with monsters! Defend yourself!")
            combat = CombatController(self, room)
            if combat.start():
                if not self.character.is_alive:
                    if type(self.character) is Ai:
                        self.character.number_of_deaths += 1
                        self.character.amount_of_gold = 0
                        self.finish_adventure()
                        print("\n- AI Player died!\n")
                    return "exit"
                # if not self.character.is_alive and type(self.character) == Player:
                #     self.handle_death()
                #     return
                # elif not self.character.is_alive:
                #     self.character.number_of_deaths += 1
                #     return "exit"
            else:
                return

        if len(room.list_of_treasures) > 0:
            money = 0
            clear_cmd()
            print("Room items:")
            for var in room.list_of_treasures:
                print("Treasure: " + str(var[0]))
                print("Value: " + str(var[1]))
                money += var[1]
            self.character.amount_of_gold += money
            print("- Your character has gathered: " + str(self.character.amount_of_gold) + " gold so far")
            self.character.statistics.treasures_collected(room.list_of_treasures)
            room.list_of_treasures = []
            if type(self.character) is Ai:
                time.sleep(self.character.wait_time)

    def finish_adventure(self):
        # Updatera antal besökta rum. Återställ durability. Spara. Skriv ut sammanställning
        self.update_visited_rooms()
        self.character.durability = self.character.max_durability
        self.character.statistics.rooms_visited = self.character.total_rooms
        self.character.total_rooms = 0
        self.character.statistics.total_amount_of_gold = self.character.amount_of_gold
        self.character.amount_of_gold = 0
        if type(self.character) is Player:
            self.account_manager.save_list_characters()
            print(self.character.summary_string_dungeon())
            input("\nPress Enter to continue to main menu")
            clear_cmd()
            return

    def update_visited_rooms(self):
        # Uppdatera statistik över besökta rum
        rooms_visited = self.dungeon_map.get_number_of_visited_rooms()
        self.character.total_rooms = rooms_visited


    #def handle_death(self):
    #    self.character.is_alive = False
    #    self.character.total_runs += 1
    #    self.account_manager.save_list_characters()
    #    clear_cmd()
    #    print(Player.summary_string_dungeon(self.character))

    #    input("Press Enter to continue to main menu")
    #    self.start_menu()

    def menu_statistics_high_scores(self):
        # Ge användaren ett val på vilken highscore dom vill se. Skicka vidare till korrekt printout.
        while True:
            clear_cmd()
            print("Choose which highscore to show:")
            list_of_choices = ["Most rooms visited", "Most gold collected", "Most monsters killed", "Go back to main menu"]
            choice = validate(list_of_choices)
            if not choice:
                continue
            elif choice == 1:
                self.show_highscore("rooms")
            elif choice == 2:
                self.show_highscore("gold")
            elif choice == 3:
                self.show_highscore("kills")
            elif choice == len(list_of_choices):
                return

    def show_highscore(self, category):
        # Hämta lista med top 5 spelare i rätt kategori. Skriv ut dess med snygg formatering.
        clear_cmd()
        list_of_characters = self.account_manager.get_highscore(category)
        print("Name\t\t\tTotal rooms\tTotal gold\tTotal kills")
        for i, character in enumerate(list_of_characters):

            character_string = (str(i + 1) + ". " + character.name)
            if len(character.name) > 8:
                character_string += "\t\t"
            elif len(character.name) > 4:
                character_string += "\t\t\t"
            else:
                character_string += "\t\t\t\t"
            character_string += (str(character.statistics.total_rooms) + "\t\t\t" +
                                str(character.statistics.total_amount_of_gold) + "\t\t\t" +
                                str(character.statistics.total_kills()))
            print(character_string)
        input("Press Enter to go back")

def clear_cmd():
    import os
    import platform
    try:
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux':
            os.system('clear')
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


game_run = True
while game_run:
    start = Controller()
    clear_cmd()
    start.start_menu()
