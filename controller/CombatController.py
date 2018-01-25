import random
import time

from model.AI import Ai
from model.Monster import Monster
from model.Player import Player
from model.Statistics import Statistics
from model.AccountManager import *
#import controller.Controller




class CombatController:

    def __init__(self, controller, room):
        self.controller = controller
        self.room = room
        self.character = controller.character
        self.order_of_attack = []
        self.list_of_monsters = room.list_of_monsters
        self.temp_monsters = []

        for monster in self.list_of_monsters:
            self.temp_monsters.append(Monster(monster.monster_type))

    def start(self):
        #Skapa ordningen. Så länge det finns minst ett monster i listan över monster och spelaren lever så får spelaren ett val medan monster attakerar
        self.create_order_of_attack()
        self.soldier_special = True
        while len(self.list_of_monsters) > 0 and self.character.is_alive:
            for creature in self.order_of_attack[:]:
                if not self.character.is_alive:
                    break
                if type(creature) is Player:
                    action = self.player_action()
                    if action == "flee":
                        input("Press enter to confirm")
                        return False
                elif type(creature) is Ai:
                    self.player_attack(self.list_of_monsters[0])
                elif creature.durability > 0:
                    self.monster_attack(creature)
        if type(self.character) is Ai:
            time.sleep(self.character.wait_time)
        else:
            input("\nPress Enter to confirm and continue")
        return True

    def player_action(self):
        # Se till att det är ett korrekt värde från spelaren. Lista igenom monster med deras index +1 först.
        # Konvertera input till int. Antingen fly, eller attackera valt monster.

        while True:
            print("Choose your action: ")
            for i, monster in enumerate(self.list_of_monsters):
                print(str(i + 1) + ". Attack the " + monster.short_string())
            print("0. Flee to the previous room")

            try:
                choice = int(input())
            except ValueError:
                print("\n- You must enter a valid input!")
                continue

            if choice == 0:
                if self.flee():
                    clear_cmd()
                    print("\n- You fled from the room!\n")
                    self.room.list_of_monsters = self.temp_monsters
                    # self.list_of_monsters = self.temp_monsters
                    return "flee"
                else:
                    # Clear cmd
                    clear_cmd()
                    print("\n- Your escape attempt failed!\n")
                    return "failed"
            elif choice <= len(self.list_of_monsters):
                self.player_attack(self.list_of_monsters[choice - 1])
                return "attack"
            else:
                print("Must enter a valid input!")

    def create_order_of_attack(self):
        # Skapa en dictionary med varje deltagare och deras initiativ för striden.
        # Skapa en sorterad lista med det rullade initiativet som sorteringsvärde. Reverse=True ger högst först.

        dict_of_initiative = {self.character: self.roll_dice(self.character.initiative)}

        for monster in self.list_of_monsters:
            dict_of_initiative[monster] = self.roll_dice(monster.initiative)

        sorted_list_of_initiative = sorted(dict_of_initiative, key=dict_of_initiative.get, reverse=True)
        for creature in sorted_list_of_initiative:
            self.order_of_attack.append(creature)

    @staticmethod
    def roll_dice(number_of_dices):
        value = 0
        for i in range(number_of_dices):
            value += random.randint(1, 6)
        return value

    def player_attack(self, monster_target):
        player_attack = self.roll_dice(self.character.attack)
        enemy_agility = self.roll_dice(monster_target.agility)
        if player_attack >= enemy_agility:
            if self.character.is_thief and random.randint(1, 100) <= 25:
                print("- Double Strike hit " + monster_target.monster_type + " for 2 durability.")
                monster_target.durability -= 2
            else:
                print("- Your attack hit " + monster_target.monster_type + " for 1 durability.")
                monster_target.durability -= 1
            if monster_target.durability <= 0:
                print("- You killed: " + monster_target.monster_type + "!")
                self.character.statistics.monster_killed(monster_target.monster_type)
                self.list_of_monsters.remove(monster_target)
                self.order_of_attack.remove(monster_target)

                for monster in self.temp_monsters:
                    if monster.monster_type is monster_target.monster_type:
                        self.temp_monsters.remove(monster)
                        break
        else:
            print("- Your attack missed!\n")

    def monster_attack(self, monster):
        monster_attack = self.roll_dice(monster.attack)
        player_agility = self.roll_dice(self.character.agility)
        if monster_attack > player_agility:
            if self.character.is_warrior and self.soldier_special:
                print("- The shield blocked the attack. You take no damage.\n")
                self.soldier_special = False
            else:
                print("- " + monster.monster_type + " hit you for 1 durability!\n")
                self.character.durability -= 1
            if self.character.durability <= 0:
                self.character.is_alive = False
                # self.controller.handle_death()
        else:
            print("- " + monster.monster_type + " tried to attack but missed!\n")

    def flee(self):
        flee_var = self.character.agility * 10
        dice_roll = random.randrange(0, 100)
        if self.character.is_wizard:
            flee_var = 80
        if dice_roll <= flee_var:
            self.controller.dungeon_map.playerPosY = self.controller.dungeon_map.last_position[0]
            self.controller.dungeon_map.playerPosX = self.controller.dungeon_map.last_position[1]
            return True
        else:
            return False


def clear_cmd():
    import os
    import platform
    try:
        if platform.system() == 'Windows':
            os.system('cls')
            print('\n' * 10)
        elif platform.system() == 'Linux':
            os.system('clear')
            # Used for debugging in Pycharm IDE:
            print('\n' * 10)
        else:
            print("Platform unknown but printing empty rows..")
            print('\n' * 10)
    except Exception:
        print("Clear failed")