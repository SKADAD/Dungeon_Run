import pickle
from model.Player import Player


class AccountManager:

    def __init__(self):
        self.list_of_characters = []
        self.load_list_characters()

    def create_new_character(self, name, classtype):
        # Kolla ifall namnet redan finns. Om ja, returnera False. Annars skapa ny player och returnera True
        if self.get_character_by_name(name):
            return False
        else:
            self.list_of_characters.append(Player(name, classtype))
            self.save_list_characters()
            return True

    def get_character_by_name(self, name):
        # Loopa igenom listan med characters och jämför namnen.
        try:
            for character in self.list_of_characters:
                if character.name == name:
                    return character
            return False
        except TypeError:
            print("Type Error")

    def get_list_of_names(self):
        while True:
            list_of_names = []
            try:
                for character in self.list_of_characters:
                    list_of_names.append(character.name + "\n\tClass: "+ character.characterClass + "\n\tStats: " + character.short_string())
                return list_of_names
            except TypeError:
                break

    def save_list_characters(self):
        try:
            pickle.dump(self.list_of_characters, open("Database.pickle", "wb"))
            print("Saved!")
            return True
        except:
            return False

    def load_list_characters(self):
        while True:
            print("Trying to load chars.... // Account Manager")
            try:
                Load = pickle.load(open("Database.pickle", "rb"))
                Load = list(Load)
                self.list_of_characters = Load
                break
            except:
                print("Exception")
                break
