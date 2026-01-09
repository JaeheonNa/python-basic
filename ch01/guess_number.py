print("숫자 게임 시작합니다.")
number = 62

exact_num = input("1~100사이의 숫자를 추측해보세요.")
guess = int(exact_num)

if number == guess :
    print("맞았습니다!")
else :
    print("틀렸습니다!")

print("게임이 종료됐습니다.")