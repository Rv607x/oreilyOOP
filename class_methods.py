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

print("\n")


"""Static methods are methods that are usually limited to class only and not 
their objects. They have no direct relation 
to class variables or instance variables."""

"""
class MyClass:

    @staticmethod
    def demo()
        print("I am a static method")
"""

class Player2:
    teamName = "Liverpool" #class variable

    def __init__(self, name):
        self.name = name

    @staticmethod
    def demo():
        print("I am a static method")

p1 = Player2("lol")
p1.demo()
Player2.demo()