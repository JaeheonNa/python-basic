class Animal(object):
    def __init__(self, name, age, weight, instance):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__instance = instance

    def show(self):
        print("이름: ", self.__name)
        print("종류: ", self.__instance.d_name)
        print("나이: ", self.__age)
        print("몸무게: ", self.__weight)
        self.__instance.sound()
        print("--" * 10)