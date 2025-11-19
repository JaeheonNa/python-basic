from Unit import *

class DropShip(Unit):
    loadedUnit = []

    def move(self, x, y):
        self.x = x
        self.y = y
        print("드랍쉽의 위치: (%d, %d)로 이동함" % (self.x, self.y))

    def load(self, unit):
        self.loadedUnit.append(unit)
        print("드랍쉽: ", unit.name, "을 탑승시킴")

    def unload(self):
        unit = self.loadedUnit.pop(0)
        print("드랍쉽: ", unit.name, "을 하차시킴")