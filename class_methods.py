#To declare a method as a class method, we use the decorator 
# @classmethod. cls is used to refer to the class just
#  like self is used to refer to the object of the class. 

"""class Myclass:
    classVariable = "educative"

    @classmethod
    def demo(cls):
        return cls.classVariable
"""

class Player:
    teamName = "Liverpool"

    def __init__(self, name):
        self.name = name

    @classmethod
    def getTeamName(cls):
        return cls.teamName

print(Player.getTeamName())