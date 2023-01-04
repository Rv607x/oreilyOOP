class Player:
    teamName = "Liverpool"  # class variable
    def __init__(self, name):
        self.name = name  #instance variable
        self.formerTeams = []

p1 = Player("Ronaldo")
p1.formerTeams.append("Manchester United")
p1.formerTeams.append("Juventus")

p2 = Player("Gakpo")
p2.formerTeams.append("PSV")

print("Player Name: ", p1.name)
print("Team Name: ", p1.teamName)
print("Former Teams: ",p1.formerTeams)
print("")

print("Player Name: ", p2.name)
print("Team Name: ", p2.teamName)
print("Former Teams: ", p2.formerTeams)