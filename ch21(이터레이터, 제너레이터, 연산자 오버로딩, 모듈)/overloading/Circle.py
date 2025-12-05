from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def area(self):
        return pi * self.radius * self.radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius
