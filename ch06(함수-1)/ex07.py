def printInfo(name, age):
    print("==" * 10)
    print("이름:", name)
    print("나이:", age)
    print("==" * 10)

continueYn = "y"
while True:
    if continueYn == "n":
        break
    name = input("이름을 입력해주세요.")
    age = int(input("나이를 입력해주세요."))
    printInfo(name,age)
    continueYn = input("계속 하시겠습니까?(y/n):")


