str1 = "안녕하세요."
str2 = "반갑습니다."
str3 = str1.__add__(str2)
print(str3)
print(str1 + str2)
print("--" * 10)

from overloading.Point import *
pointA = Point(10, 20)
pointB = Point(20, 30)
pointC = pointA + pointB
print("pointA: ", (10, 20))
print("pointB: ", (20, 30))
print("pointA + pointB: ", pointC)
print("--" * 10)

from overloading.NumBox import *
numbox = NumBox(10)
print("numbox: ", numbox)
numbox = numbox + 100
print("numbox + 100: ", numbox)
numbox = numbox - 20
print("numbox - 20: ", numbox)
numbox = 100 + numbox
print("100 + numbox: ", numbox)
numbox = 20 - numbox
print("20 - numbox: ", numbox)
print("--" * 10)