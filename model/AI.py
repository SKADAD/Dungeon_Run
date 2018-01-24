from model.Player import Player


class Ai(Player):

    def __init__(self, character_class, wait_time):  # Add number_of_rounds (?)
        super().__init__("AI " + character_class, character_class)
        self.wait_time = wait_time
        self.number_of_deaths = 0
        self.total_rooms = 0
        # self.number_of_rounds = number_of_rounds

    def summary_string(self):
        summary = "Summary of AI run with " + self.characterClass + "\n"
        summary += "The AI died " + str(self.number_of_deaths) + " number of times.\n"
        summary += "Number of monsters killed:\n"
        summary += self.statistics.monster_killed_toString()
        summary += "Total gold collected: " + str(self.amount_of_gold) + "\n"
        summary += "Total rooms visited: " + str(self.statistics.rooms_visited) + "\n"
        return summary


