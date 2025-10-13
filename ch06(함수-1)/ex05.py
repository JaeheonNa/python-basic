def is_prime(num):
    if num < 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

integer = int(input("정수를 입력하세요."))
if is_prime(integer):
    print(integer, "는 소수입니다.")
else:
    print(integer, "는 소수가 아닙니다.")