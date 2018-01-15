import random

from model.Player import Player


class CombatController:

    def __init__(self, controller, list_of_monsters):
        self.controller = controller
        self.player = controller.character
        self.order_of_attack = []
        self.list_of_monsters = list_of_monsters

    def start(self):
        #Skapa ordningen. Så länge det finns minst ett monster i listan över monster och spelaren lever så får spelaren ett val medan monster attakerar
        self.create_order_of_attack()
        while len(self.list_of_monsters) > 0 and self.player.is_alive:
            for creature in self.order_of_attack:
                if type(creature) is Player:
                    self.player_action()
                else:
                    self.monster_attack(creature)

    def player_action(self):
        # Se till att det är ett korrekt värde från spelaren. Lista igenom monster med deras index +1 först.
        # Konvertera input till int. Antingen fly, eller attackera valt monster.

        while True:
            self.controller.to_print("Choose your action:")
            for i, monster in enumerate(self.list_of_monsters):
                self.controller.to_print(str(i + 1) + ". Attack the " + monster.monster_type)
            self.controller.to_print("0. Flee to the previous room")

            try:
                choice = int(input())
            except Exception:
                self.controller.to_print("Must enter a valid input!")
                continue

            if choice == 0:
                self.player_flee()
                break
            elif choice < len(self.list_of_monsters):
                self.player_attack(self.list_of_monsters[choice - 1])
                break
            else:
                self.controller.to_print("Must enter a valid input!")

    def create_order_of_attack(self):
        # Skapa en dictionary med varje deltagare och deras initiativ för striden.
        # Skapa en sorterad lista med det rullade initiativet som sorteringsvärde. Reverse=True ger högst först.

        dict_of_initiative = {self.player: self.roll_dice(self.player.initiative)}
        for monster in self.list_of_monsters:
            dict_of_initiative[monster] = self.roll_dice(monster.initiative)
            print(monster.monster_type)

        sorted_list_of_initiative = sorted(dict_of_initiative, key=dict_of_initiative.get, reverse=True)
        for creature in sorted_list_of_initiative:
            self.order_of_attack.append(creature)

    @staticmethod
    def roll_dice(number_of_dices):
        value = 0
        for i in range(number_of_dices):
            value += random.randint(1, 6)
        return value
