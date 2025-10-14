# 피보나치 수열을 구하는 함수
def fib(n):
    n1 = 0
    n2 = 1
    while n2 < n:
        print(n2, end = ' ')
        sum = n2 + n1
        n1 = n2
        n2 = sum

# n까지의 자연수를 더하는 함수
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

