for y in range(5):
    for x in range(y+1):
        print("*", end="")
    print("")

print("{} 님의 나이는 {}세 입니다".format("나루", 2))

for i in range(5):
    print("{:>5}".format("*" * (i+1)))

for y in range(5, 0, -1):
    for x in range(y):
        print("*", end="")
    print("")

for i in range(5, 0, -1):
    print("{:>5}".format("*" * i))