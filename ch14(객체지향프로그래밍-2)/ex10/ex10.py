from Sedan import *
from Truck import *

if __name__ == '__main__':
    sedan1 = None
    truck1 = None

    sedan1 = Sedan()
    truck1 = Truck()

    print("세단의 현재 속도: %skm/h" % str(sedan1.getSpeed()))
    sedan1.upSpeed(200)

    print("트럭의 현재 속도: %skm/h" % str(truck1.getSpeed()))
    truck1.upSpeed(200)