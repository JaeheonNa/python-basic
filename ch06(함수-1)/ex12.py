def decimalToBinary(num):
    bin = ""
    while num > 0:
        bin = str(num % 2) + bin
        num = num // 2
    return bin

print(decimalToBinary(3))

num = 12
print("10진수", num, "의 2진수 값은", bin(num), "입니다.")
print("10진수", num, "의 8진수 값은", oct(num), "입니다.")
print("10진수", num, "의 16진수 값은", hex(num), "입니다.")

num = 13
print("2진수", bin(num), "의 10진수 값은", int(bin(num), 2), "입니다.")
print("8진수", oct(num), "의 10진수 값은", int(oct(num), 8), "입니다.")
print("16진수", hex(num), "의 10진수 값은", int(hex(num), 16), "입니다.")