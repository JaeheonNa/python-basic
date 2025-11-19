from ContentsSender import *

class ConcreteContentsSender(ContentsSender):
    contents = ""
    def __init__(self, title, name, contents):
        super().__init__(title, name)
        self.contents = contents

    def sendMessage(self, receiver):
        print("제목: %s \n주연: %s \n회차: %s \n수신자: %s" % (self.title, self.name, self.contents, receiver))