from Phone import *

class DMBPhone(Phone):

    def __init__(self, model, color, channel):
        super().__init__()
        self.model = model
        self.color = color
        self.channel = channel

    def turnOnDMB(self):
        print("채널: ", self.channel, "번 DMB 채널 방송을 수신합니다.")

    def turnOffDMB(self):
        print("DMB 방송을 종료합니다.")

    def changeDMBChannel(self, channel):
        self.channel = channel
        print("채널: ", self.channel, "번 DMB 채널 방송을 수신합니다.")
