squares = []
for x in range(1, 11):
    squares.append(x ** 2)
print("squares:", squares)
squares = []
print("squares:", squares)
squares = [x**2 for x in range(1, 11)]
print("squares:", squares)

print("==" * 10)
oddNum = [x for x in range(1, 21) if x % 2 != 0]
print("oddNum:", oddNum)

print("==" * 10)
evenNum = [x for x in range(1, 21) if x % 2 == 0]
print("evenNum:", evenNum)

print("==" * 10)
multiplication_table = [str(x) + "x" + str(y) + "=" + str(x * y)
                            for x in range(2, 10)
                            for y in range(1, 10)]
print("구구단:", multiplication_table)

