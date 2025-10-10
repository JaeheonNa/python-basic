floor = 5

for y in range(floor):
    print(" " * (floor-y), end="")
    for x in range(y+1):
        print("*", end="")
    print("*"*y)
print("--" * 6)

for y in range(1, floor+1):
    for x in range(floor-y):
        print(" ", end="")
    for x in range(1, y*2):
        print("*", end="")
    print("")
print("--" * 6)

for i in range(1, floor*2+1, 2):
    print("{:^10}".format("*" * i))
print("--" * 6)


for y in range(1, floor+1):
    for x in range(floor-y):
        print(" ", end="")
    for x in range(1, y*2):
        print("*", end="")
    print("")
for y in range(floor, 0, -1):
    for x in range(floor-y):
        print(" ", end="")
    for x in range(1, y*2):
        print("*", end="")
    print("")
