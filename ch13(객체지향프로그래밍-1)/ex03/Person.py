class Person:
    # __가 붙으면 private. 안 붙으면 public.
    __name = ""
    age = 0
    height = 0
    weight = 0
    address = ""

    # def __init__(self, name, age, height, weight, address):
    #     self.name = name
    #     self.age = age
    #     self.height = height
    #     self.weight = weight
    #     self.address = address

    def __init__(self):
        self.__name = "아이유"
        self.age = 32
        self.height = 160
        self.weight = 45
        self.address = "서울"
        print("Person의 기본 생성자 호출")

    def getName(self):
        return self.__name

    def getAge(self):
        return self.age

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getAddress(self):
        return self.address

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.age = age

    def setHeight(self, height):
        self.height = height

    def setWeight(self, weight):
        self.weight = weight

    def setAddress(self, address):
        self.address = address