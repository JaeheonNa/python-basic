import math

def get_sphereVolume(radius):
    return 4/3 * math.pi * math.pow(radius,3)

radius = int(input("구의 반지름을 입력하세요."))
print("반지름", radius, "인 구의 부피는", round(get_sphereVolume(radius), 2), "입니다.")