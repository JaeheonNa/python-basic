x, y = 2, 0
try:
    z = x / y
    print(z)
except ZeroDivisionError:
    print("모든 수는 0으로 나눌 수 없습니다.")


try:
    n = int(input("정수를 입력하세요: "))
    print(n)
except ValueError:
    print("정수가 아닙니다.")

try:
    fname = input("파일 이름을 입력하세요: ")
    file = open(fname, "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("해당하는 파일이 존재하지 않습니다.")

raise NameError("비밀번호가 잘못됐습니다.")