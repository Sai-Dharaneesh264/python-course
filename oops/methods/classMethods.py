class Player:
    teamName = "Liverpool"

    def __init__(self, name):
        self.name = name
    

    @classmethod
    def getTeamName(cls):
        return cls.teamName

print(Player.getTeamName())