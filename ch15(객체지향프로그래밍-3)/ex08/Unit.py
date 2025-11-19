from abc import *

class Unit(metaclass=ABCMeta):
    x = 0
    y = 0
    name = ""

    @abstractmethod
    def move(self, x, y):
        pass

    def stop(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        print("%s가 (%d, %d)에 멈춥니다." % (name, self.x, self.y))