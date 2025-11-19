from Unit import *

class Tank(Unit):
    mode = "탱크: 일반모드"

    def move(self, x, y):
        self.x = x
        self.y = y
        if self.mode == "탱크: 시즈모드":
            self.moveMode()
        print("탱크의 위치: (%d, %d)로 이동함" % (self.x, self.y))

    def siegeMode(self):
        self.mode = "탱크: 시즈모드"
        print(self.mode)

    def moveMode(self):
        self.mode = "탱크: 일반모드"
        print(self.mode)