class Car:
    color = ''
    speed = 0

    def speedUp(self, speed):
        if speed < 0:
            print("속도는 음수일 수 없습니다.")
        else:
            self.speed += speed
            print(speed, "Up!")

    def speedDown(self, speed):
        if speed < 0:
            print("속도는 음수일 수 없습니다.")
        else:
            if self.speed  < speed:
                print('속력이 0보다 작을 수 없습니다.')
            else:
                self.speed -= speed
                print(speed, "Down!")

    def printFields(self):
        print('car1의 색상: %s, 속도 %dKm/h' % (self.color, self.speed))