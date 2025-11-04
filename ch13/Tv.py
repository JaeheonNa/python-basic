class Tv:
    color = ''
    power = False
    channel = 0
    volume = 0

    def __init__(self, color):
        self.color = color

    def onPower(self):
        self.power = not self.power
        if self.power:
            print("TV가 켜졌습니다.")
        else:
            print("TV가 켜졌습니다.")

    def channelUp(self):
        if not self.power:
            print("TV가 꺼져있습니다.")
            return
        self.channel += 1
        if self.channel > 999:
            self.channel = 0

    def channelDown(self):
        if not self.power:
            print("TV가 꺼져있습니다.")
            return
        self.channel -= 1
        if self.channel < 0:
            self.channel = 999

    def volumeUp(self):
        if not self.power:
            print("TV가 꺼져있습니다.")
            return
        self.volume += 1
        if self.volume > 100:
            self.volume = 100

    def volumeDown(self):
        if not self.power:
            print("TV가 꺼져있습니다.")
            return
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0

    def __str__(self):
        print("TV의 색상: %s" % self.color)
        print("TV의 channel: %d" % self.channel)
        print("TV의 볼륨: %d" % self.volume)

