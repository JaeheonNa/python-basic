from Unit import *
import time

class Marine(Unit):
    mode = "마린: 일반모드"

    def move(self, x, y):
        self.x = x
        self.y = y
        print("마린의 위치: (%d, %d)로 이동함" % (self.x, self.y))

    def stimPack(self):
        self.mode = "마린: 스팀팩모드"
        print(self.mode)

        time.sleep(5)
        print(self.mode, "해제")
        self.mode = "마린: 일반모드"
        print(self.mode)
