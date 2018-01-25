from model.Player import Player


class Ai(Player):

    def __init__(self, character_class, wait_time):  # Add number_of_rounds (?)
        super().__init__("AI " + character_class, character_class)
        self.wait_time = wait_time
        self.number_of_deaths = 0
        # self.number_of_rounds = number_of_rounds

    def summary_string(self):
        summary = "Summary of AI run with " + self.name + ":\n\n"
        summary += "The AI played " + str(self.statistics.total_runs) + " dungeon(s) and died " + str(self.number_of_deaths) + " time(s).\n"
        summary += "Number of monsters killed:\n" + self.statistics.monster_killed_toString()
        summary += "Total gold collected = " + str(self.statistics.total_amount_of_gold) + "\n"
        summary += "Total rooms visited = " + str(self.statistics.total_rooms) + "\n"
        return summary

