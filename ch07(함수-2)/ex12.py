def main():
    print("두 값의 합:", getSum(x, y))
    print("두 값의 합(람다):", lambda_getSum(x, y))
    print(lambda x, y : x + y)
    print((lambda x, y : x + y)(10, 20))


def getSum(x, y):
    return x + y

lambda_getSum = lambda x, y : x + y

x = 10
y = 100

main()

li = [
    lambda x : x ** 1,
    lambda x : x ** 2,
    lambda x : x ** 3
]

for f in li:
    print(f(9))