import model.DungeonMap


class AccountManager:

    def __init__(self):
        self.characterNewName = "NewChar"
        self.characterLoadName = "LoadChar"
        self.selectStartingPos = "NW"
        self.selectSizeOfMap = 5

    def newChar(self):
        test = model.DungeonMap()
        self.characterNewName = input("Enter char name: ")