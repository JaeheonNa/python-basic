class Card:
    __kind = ""
    __number = 0
    __width = 100
    __height = 250

    def __init__(self, kind, number):
        self.__kind = kind
        self.__number = number

    def __str__(self):
        print("kind:", self.__kind)
        print("number:", self.__number)
        print("width:", self.__width)
        print("height:", self.__height)
