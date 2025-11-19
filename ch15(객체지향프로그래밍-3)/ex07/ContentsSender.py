from abc import *

class ContentsSender(metaclass=ABCMeta):
    title = ""
    name = ""

    def __init__(self, title, name):
        self.title = title
        self.name = name

    @abstractmethod
    def sendMessage(self, receiver):
        pass

    @abstractmethod
    def sendMessage(self, receiver, message):
        pass