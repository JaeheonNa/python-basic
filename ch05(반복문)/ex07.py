from math import *

print("화씨", "섭씨")
for f in range(0, 101, 10):
    c = (f - 32) * 5 / 9
    print(f, "->", round(c, 2))