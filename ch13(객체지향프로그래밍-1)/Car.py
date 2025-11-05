class Car:
    __color = ''
    __speed = 0
    count = 0

    def __init__(self, color):
        self.__color = color
        self.__speed = 0
        Car.count += 1

    def getColor(self):
        return self.__color

    def getSpeed(self):
        return self.__speed

    def setColor(self, color):
        self.__color = color

    def setSpeed(self, speed):
        self.__speed = speed