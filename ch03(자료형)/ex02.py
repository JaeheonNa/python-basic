# 프록시마 켄타우리는 지구로부터 40 * 10^12 km 떨어져있음.
# 빛의 속도로 프록시마 켄타우리까지 갈 때 몇 년이 걸릴까?

from math import *

distance = 40 * (pow(10, 12))
light_speed = 300000

total_second = distance / light_speed

print(total_second)

light_year = total_second / (60 * 60 * 24 * 365)

print(light_year)