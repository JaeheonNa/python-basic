from Circle import * 

if __name__ == '__main__':
    c = Circle(10)
    print("원의 반지름:", c.getRadius())
    print("원의 넓이:", c.getArea())
    print("원의 둘레:", c.getCircumference() )

    print('--' * 10)

    c = Circle(20)
    print("원의 반지름:", c.getRadius())
    print("원의 넓이:", c.getArea())
    print("원의 둘레:", c.getCircumference())
