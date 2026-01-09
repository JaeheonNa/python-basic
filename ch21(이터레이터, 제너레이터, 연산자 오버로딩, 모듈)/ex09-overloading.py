from overloading.Circle import *

c1 = Circle(4)
print("c1의 반지름: ", c1.getRadius())
c2 = Circle(5)
print("c2의 반지름: ", c2.getRadius())

c3 = c1 + c2
print("c1의 반지름과 c2의 반지름을 합한 값: ", c3.getRadius())

print("c3 > c2의 결과: ", c3 > c2)
print("c1 < c2의 결과: ", c1 < c2)

print("원의 반지름: ", c3.getRadius())
