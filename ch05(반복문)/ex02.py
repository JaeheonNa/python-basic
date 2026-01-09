sum = 0
for i in range(10):
    sum = sum + i
print("0~9까지의 누계: ", sum)
print("-" * 10)

sum = 0
for i in range(0, 10):
    sum = sum + i
print("0~9까지의 누계: ", sum)
print("-" * 10)

sum = 0
for i in range(0, 10, 2):
    sum = sum + i
print("0~9까지의 정수 가운데 0을 기준으로 2 차이 나는 수들의 누계: ", sum)
print("-" * 10)

name = "Na Jae Heon"
for n in name:
    print(n, end=" ")