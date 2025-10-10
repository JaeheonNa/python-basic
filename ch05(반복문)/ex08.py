num = int(input("출력하려는 구구단의 단 수를 입력하세요: "))

if num < 2 or num > 9:
    print("단을 잡못 입력하셨습니다.")
else:
    for i in range(1, 10):
        print(num, "x", i, "=", num * i)