# 파이썬에서의 자료형(Data Type)

print(type(17)) # int
print(type(3.14)) # float
print(type("안녕하세요")) # str

from math import *
r = 5

# 반기름이 5인 구의 부피
volume1 = (4 / 3) * pi * (r ** 3)
volume2 = (4 / 3) * pi * (pow(r, 3))

print(volume1 == volume2)
print("구의 부피: ", volume1)

# 반기름이 5인 구의 겉넓이
outer_area = 4 * pi * pow(r, 2)
print("구의 겉넓이: ", outer_area)

