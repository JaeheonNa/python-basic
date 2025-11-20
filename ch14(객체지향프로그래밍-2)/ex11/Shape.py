import turtle
import random

class Shape(object):
    myTurtle = None
    sx, xy = 0, 0

    def __init__(self):
        self.myTurtle = turtle.Turtle()

    def setPen(self):
        r = random.random()
        g = random.random()
        b = random.random()
        print("r: %f, g: %f, b: %f" % (r, g, b))
        self.myTurtle.pencolor(r, g, b)

        penSize = random.randrange(1, 20)
        print("penSize: %d" % penSize)
        self.myTurtle.pensize(penSize)

    def drawShape(self):
        pass