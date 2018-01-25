from model.Player import Player


class Ai(Player):

    def __init__(self, character_class, wait_time):  # Add number_of_rounds (?)
        super().__init__("AI " + character_class, character_class)
        self.wait_time = wait_time
        self.number_of_deaths = 0
        # self.number_of_rounds = number_of_rounds

    def summary_string(self):
        summary = "Summary of AI run with " + self.characterClass + ":\n\n"
        if self.number_of_deaths == 0:
            summary += "The AI survived the dungeon(s) and is still alive.\n"
        else:
            summary += "The AI died " + str(self.number_of_deaths) + " times of " + str(self.total_runs) + " dungeon runs.\n"
            summary += "Total rounds = " + str(self.total_runs) + "\n"
        summary += "Number of monsters killed:\n" + self.statistics.monster_killed_toString()
        summary += "Total gold collected = " + str(self.amount_of_gold) + "\n"
        summary += "Total rooms visited = " + str(self.statistics.rooms_visited) + "\n"
        return summary
