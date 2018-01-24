from model.Player import Player


class Ai(Player):

    def __init__(self, character_class, wait_time):  # Add number_of_rounds (?)
        super().__init__("AI " + character_class, character_class)
        self.wait_time = wait_time
        # self.number_of_rounds = number_of_rounds

    def summary_string(self):
        summary = "Summary of AI run with " + self.characterClass + "\n"
        if self.is_alive:
            summary += "The AI found the exit and left alive with a durability of " + str(self.durability) + "\n"
        else:
            summary += "The AI was killed during the dungeon run\n"
        summary += "Number of monsters killed:\n"
        summary += self.statistics.monster_killed_toString()
        summary += "Total gold collected: " + str(self.amount_of_gold)
        summary += "Total rooms visited: " + str(self.statistics.room_count)
        return summary

