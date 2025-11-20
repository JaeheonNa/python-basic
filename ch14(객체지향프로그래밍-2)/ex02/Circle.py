class Circle:
    def __init__(self, radius=0):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def __eq__(self, other):
        print("__eq__ 메소드 호출됨.")
        return self.__radius == other.getRadius()