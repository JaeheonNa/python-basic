num = int(input("어디까지의 합계를 구하겠습니까?"))
sum = 0
for i in range(1, num+1):
    sum += i

print("1부터", num, "까지의 합계 =", sum)