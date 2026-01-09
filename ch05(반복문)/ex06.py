num = int(input("피보나치 수열을 구해보도록 하죠. 몇 번째까지 구해볼까요?"))

fibonacci = []

for i in range(num):
    if (i == 0) or (i == 1):
        fibonacci.append(1)
    else :
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(num, "번째까지의 피보나치 수열은", fibonacci)