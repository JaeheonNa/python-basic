num = int(input("n!을 구해보도록 하죠. n값을 입력하세요."))

answer = 1
for i in range(1, num+1) :
    answer *= i

print("n! 값은", answer)