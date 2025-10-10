num_1 = int(input("첫 번째 정수를 입력하세요."))
num_2 = int(input("두 번째 정수를 입력하세요."))

if num_1 > num_2:
    print("첫 번째 수가 더 작아야 합니다.")

for i in range(num_1, num_2+1):
    if i % 3 == 0 and i % 4 == 0:
        continue
    print(i, end=" ")