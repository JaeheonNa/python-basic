from Car import *

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