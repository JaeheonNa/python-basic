from operator import eq

price = 0
print(type(price) == str)
while True:
    inputData = input("상품 금액을 입력하세요:")
    if eq(inputData, "끝"):
        break
    price += int(inputData)

print("총 가격은 %d 원입니다" % price)
