from random import *

answer = randint(1, 100)
submit = 0
cnt = 0

while submit != answer:
    submit = int(input("Up & Down, Up & Down!"))
    cnt += 1
    if submit > answer:
        print("Down!")
    elif submit < answer:
        print("Up!")
    else:
        print("정답입니다!", cnt, "회 만에 맞추셨습니다!")
        continueYn = input("게임을 계속하시겠습니까? (y/n)")
        if continueYn == "n":
            break
        else:
            print("---게임을 재시작 합니다---")
            answer = randint(1, 100)
            submit = 0
            cnt = 0

print("게임을 종료합니다.")

