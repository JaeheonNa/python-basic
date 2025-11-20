import math

class Circle:
    __radius = 0
    __circumference = 0
    __area = 0

    def __init__(self, radius):
        self.__radius = radius
        self.__area = self.calcArea()
        self.__circumference =self.calcCircumference()

    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__area
    def setArea(self, area):
        self.__area = area

    def getCircumference(self):
        return self.__circumference
    def setCircumference(self, circumference):
        self.__circumference = circumference

    def calcArea(self):
        return round(math.pi * pow(self.__radius, 2), 2)

    def calcCircumference(self):
        return round(2 * math.pi * self.__radius, 2)