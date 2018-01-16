from model.Player import Player


class AccountManager:

    def __init__(self):
        self.list_of_characters = []

    def create_new_character(self, name, classtype):
        # Kolla ifall namnet redan finns. Om ja, returnera False. Annars skapa ny player och returnera True
        if self.get_character_by_name(name):
            return False
        else:
            self.list_of_characters.append(Player(name, classtype))
            return True

    def get_character_by_name(self, name):
        # Loopa igenom listan med characters och jämför namnen.
        for character in self.list_of_characters:
            if character.name == name:
                return character
        return False
