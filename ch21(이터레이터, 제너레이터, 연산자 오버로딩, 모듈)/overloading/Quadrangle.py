class Quadrangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return Quadrangle(self.width + other.width, self.height + other.height)