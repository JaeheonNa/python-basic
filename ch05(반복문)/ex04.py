
num = int(input("어디까지의 합계를 구하겠습니까?"))
sum = 0
for i in range(1, num+1):
    if sum >= 2000:
        print("마지막으로 더해지는 값 =", i-1)
        break
    else:
        sum += i

print("합계 =", sum)