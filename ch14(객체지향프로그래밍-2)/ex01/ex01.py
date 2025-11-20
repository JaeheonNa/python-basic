from Square import *

def increaseHeight(rect):
    rect.setHeight(rect.getHeight() + 1)

if __name__ == '__main__':
    rectangle1 = Square(10, 5)
    print("rectangle1: ",rectangle1.__str__())
    increaseHeight(rectangle1)

    rectangle2 = Square(11, 5)
    print("rectangle1: ",rectangle1.__str__())
    print("rectangle2: ",rectangle2.__str__())

    print("rectangle1 == rectangle2: ", rectangle1.__eq__(rectangle2))
