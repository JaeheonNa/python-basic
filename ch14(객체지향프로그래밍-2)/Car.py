class Car:

    __speed = 0

    def __init__(self):
        pass

    def upSpeed(self, speed):
        self.__speed += speed
        print("현재 속도(조상 클래스): %skm/h" % str(self.__speed))

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed