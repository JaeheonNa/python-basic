import math

PI = math.pi

def main():
    radius = float(input("원의 반지름을 입력하세요:"))
    print("반지름", radius, "인 원의 면적: ", circle_area(radius))
    print("반지름", radius, "인 원의 둘레: ", circle_circumference(radius))

def circle_area(radius):
    return PI * radius * radius

def circle_circumference(radius):
    return 2 * PI * radius

main()

