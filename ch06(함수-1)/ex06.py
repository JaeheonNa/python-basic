def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return round(x / y, 2)

continueYn = "y"

while True:
    if continueYn == "n":
        break
    else:
        n1 = float(input("첫 번째 수 입력: "))
        n2 = float(input("첫 번째 수 입력: "))
        op = input("원하는 연산을 입력(+, -, *, /): ")
    if op == "+":
        print(n1, "+", n2, "=", add(n1, n2))
    elif op == "-":
        print(n1, "-", n2, "=", substract(n1, n2))
    elif op == "*":
        print(n1, "*", n2, "=", multiply(n1, n2))
    elif op == "/":
        print(n1, "/", n2, "=", divide(n1, n2))
    else:
        print("잘못된 연산자입니다.")
    continueYn = input("계속 계산하시겠습니까?(y/n)")


