class DimmerSwitch():
    def __init__(self):
        self.SwitchOn = False
        self.brightness = 0
    
    def turnOn(self):
        self.SwitchOn = True
    
    def turnOff(self):
        self.SwitchOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness  = self.brightness + 1
    
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1
    
    def show(self):
        print("Switch is on?", self.SwitchOn)
        print("Brightness is:", self.brightness)

oDimmer = DimmerSwitch()

oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()