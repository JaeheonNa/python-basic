from Car import *

class Sedan(Car):

    def __init__(self):
        super().__init__()

    def upSpeed(self, speed):
        self.setSpeed(self.getSpeed() + speed)
        if self.getSpeed() >  150:
            self.setSpeed(150)
            print("세단은 150km/h를 넘길 수 없습니다.")
        print("세단의 현재 속도(자식 클래스): %skm/h" % str(self.getSpeed()))

    def downSpeed(self, speed):
        self.setSpeed(self.getSpeed() - speed)
        if self.getSpeed() < 0:
            self.setSpeed(0)
        print("세단의 현재 속도(자식 클래스): %skm/h" % str(self.getSpeed()))