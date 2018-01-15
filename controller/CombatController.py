import random

class CombatController:

    def __init__(self, controller, list_of_monsters):
        self.controller = controller
        self.player = controller.player
        self.order_of_attack = []
        self.create_order_of_attack(list_of_monsters)


    def create_order_of_attack(self, list_of_monsters):
        dict_of_initiative = {}
        dict_of_initiative[self.player] = self.roll_dice(self.player.initiative)
        for monster in list_of_monsters:
            dict_of_initiative[monster] = self.roll_dice(monster.initiative)
            print(monster.monster_type)

        dict_of_initiative = sorted(dict_of_initiative, key=dict_of_initiative.get, reverse=True)
        for creature in dict_of_initiative:
            self.order_of_attack.append(creature)

    @staticmethod
    def roll_dice(number_of_dices):
        value = 0
        for i in range(number_of_dices):
            value += random.randint(1, 6)
        return value

    def player_attack(self, monster_target):
        player_attack = self.roll_dice(self.player.attack)
        enemy_agility = self.roll_dice(monster_target.agility)
        if player_attack > enemy_agility:
            monster_target.durability -= 1
            if monster_target.durability <= 0:
                print("Enemy down")

    def monster_attack(self, monster):
        monster_attack = self.roll_dice(monster.attack)
        player_agility = self.roll_dice(self.player.agility)
        if monster_attack > player_agility:
            self.player.durability -= 1
            if self.player.durability <= 0:
                print("game over")
