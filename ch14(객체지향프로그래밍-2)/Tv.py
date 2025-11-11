class Tv:
    def __init__(self, power, channel, volume):
        self.power = power
        self.channel = channel
        self.volumn = volume

    def powerButton(self):
        self.power = not self.power

    def __str__(self):
        powerState = 'OFF'
        if self.power == True:
            powerState = 'ON'
        return "Power: %s, Channel: %d, Volume: %d" % (powerState, self.channel, self.volumn)