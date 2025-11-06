class Square:
    __height = 0
    __width = 0
    __area = 0

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.calcArea()

    def calcArea(self):
        self.__area = self.__height*self.__width

    def setHeight(self, height):
        self.__height = height
        self.calcArea()

    def setWidth(self, width):
        self.__width = width
        self.calcArea()

    def getHeight(self):
        return self.__height
    def getWidth(self):
        return self.__width
    def getArea(self):
        return self.__area

    def __eq__(self, other):
        return self.__height == other.getHeight() and self.__width == other.getWidth() and self.__area == other.getArea()

    def __str__(self):
        return "높이: %d, 너비: %d, 넓이: %d" % (self.__height, self.__width, self.__area)
