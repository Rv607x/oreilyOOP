#Light switch class
class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        """ turn the switch on"""
        self.switchIsOn = True

    def turnOff(self):
        """turn the switch off"""
        self.switchIsOn = False

    def show(self):
        print(self.switchIsOn)
    
oLightSwitch = LightSwitch()

"""oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show() """

oLightSwitch1 = LightSwitch()
oLightSwitch2 = LightSwitch()

oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn() # Turn switch 1 on
# Switch 2 should be off at start, but this makes it clearer
oLightSwitch2.turnOff()  
oLightSwitch1.show()
oLightSwitch2.show()
