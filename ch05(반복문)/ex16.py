flag = True
speed = 0
while flag:
    print("------------------------")
    print("1. 증속 | 2. 감속 | 3. 중지")
    print("------------------------")
    keyCode = input("입력해주세요")
    if keyCode == "1":
        speed += 10
    elif keyCode == "2":
        speed -= 10
        if speed < 0:
            print("속도가 음수일 수는 없습니다.")
            speed += 10
    elif keyCode == "3":
        print("중지")
        speed = 0
        flag = False
    print("현재 속도: %d" % speed)
