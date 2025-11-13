import turtle

from Shape import *


class Rectangle(Shape):

    __width = 0
    __height = 0

    def __init__(self, sx, sy):
        super().__init__()
        self.sx = sx
        self.sy = sy
        self.__width = random.randrange(20, 100)
        self.__height = random.randrange(20, 100)
        print("width: %d, height: %d" % (self.__width, self.__height))

    def drawShape(self):
        lx = self.sx - (self.__width / 2)
        rx = self.sx + (self.__width / 2)
        uy = self.sy + (self.__height / 2)
        dy = self.sy - (self.__height / 2)

        self.setPen()
        self.myTurtle.shape('turtle')
        self.myTurtle.penup()
        self.myTurtle.goto(lx, uy)
        self.myTurtle.pendown()
        self.myTurtle.goto(rx, uy)
        self.myTurtle.goto(rx, dy)
        self.myTurtle.goto(lx, dy)
        self.myTurtle.goto(lx, uy)

    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def setWidth(self, width):
        self.__width = width
    def setHeight(self, height):
        self.__height = height