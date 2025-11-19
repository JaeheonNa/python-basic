import math


def getCircleInfo(radius):
    circumstance = 2 * math.pi *  radius
    area = math.pi * pow(radius, 2)
    return circumstance, area

if __name__ == "__main__":
    r = float(input("반지름을 입력하세요."))
    (circumstance, area) = getCircleInfo(r)
    print("원의 둘레는: ", circumstance)
    print("원의 넓이는: ", area)

