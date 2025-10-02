from random import *

answer = randint(1, 100)
cnt = 0
while True:
    num = int(input("업 앤 다운~ 업 앤 다운!"))
    cnt += 1
    print(num, "!")
    if num == answer:
        break
    elif num > answer:
        print("Down!")
    else:
        print("Up!")

print(answer, "! 정답입니다! ", cnt, "회만에 맞추셨습니다!")