from Car import *

if __name__ == '__main__':
    car1 = Car('Black')
    car1.setSpeed(100)
    print("car1의 색상은 %s 이고, 속도는 %d 이며, 현재 생산된 차량은 총 %d 대입니다." % (car1.getColor(), car1.getSpeed(), Car.count))
    car2 = Car('White')
    car2.setSpeed(80)
    print("car2의 색상은 %s 이고, 속도는 %d 이며, 현재 생산된 차량은 총 %d 대입니다." % (car2.getColor(), car2.getSpeed(), Car.count))
    car3 = Car('Blue')
    car3.setSpeed(50)
    print("car3의 색상은 %s 이고, 속도는 %d 이며, 현재 생산된 차량은 총 %d 대입니다." % (car3.getColor(), car3.getSpeed(), Car.count))