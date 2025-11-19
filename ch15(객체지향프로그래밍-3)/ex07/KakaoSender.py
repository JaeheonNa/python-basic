from ContentsSender import *

class KakaoSender(ContentsSender):
    message = ""

    def __init__(self, title, name):
        super().__init__(title, name)

    def sendMessage(self, receiver, message):
        print("수신자: %s \n메시지: %s \n발신자: %s" % (self.name, message, receiver))