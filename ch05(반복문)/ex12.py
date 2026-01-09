i = 0
while i < 5 :
    print("반값습니다.")
    i += 1
print("반복이 종료되었습니다.")
print("--" * 10)


i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print("")
print("--" * 10)

i = 0
sum = 0
while i <= 10:
    sum += i
    i += 1
print(sum)
print("--" * 10)

answer = 1
i = 1
while i <= 10:
    answer *= i
    i += 1
print("10! = ", answer)
print("--" * 10)

i = 1
while i < 10:
    print("3 x %d = %2d" % (i, 3 * i))
    i += 1
print("--" * 10)

answer = 0
i = 1
while i <= 100:
    if i % 3 == 0:
        answer += i
    i += 1
print("1~100 사이의 3의 배수의 합은", answer)
print("--" * 10)

numStr = input("정수를 입력하세요")
i = 0
answer = 0
while i < len(numStr):
    answer += int(numStr[i])
    i += 1
print(answer)
print("--" * 10)

num = int(input("정수를 입력하세요"))
answer = 0
i = 0
while num > 0:
    answer += num % 10
    num = num // 10
print(answer)
print("--" * 10)