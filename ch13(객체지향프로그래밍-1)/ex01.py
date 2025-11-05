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


if __name__ == '__main__':

    car1 = Car()
    car2 = Car()
    car3 = Car()
    print("car1의 주소: ", id(car1))
    print("car2의 주소: ", id(car2))
    print("car3의 주소: ", id(car3))
    print('--' * 10)
    print("car1의 타입: ", type(car1))
    print("car2의 타입: ", type(car2))
    print("car3의 타입: ", type(car3))
    print('--' * 10)

    car1.color = 'blue'
    car1.speedUp(50)
    car1.printFields()