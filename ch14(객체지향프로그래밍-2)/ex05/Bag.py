class Bag:
    def __init__(self):
        self.__data = []

    def add(self, item):
        self.__data.append(item)

    def add2(self, item):
        self.add(item)
        self.add(item)

    def __str__(self):
        return str(self.__data)