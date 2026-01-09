normal_price = int(input("구입 금액을 입력하세요. : "))

discount_price = 0
final_price = 0

if normal_price >= 50000 :
    discount_price = normal_price * 0.05
    final_price = normal_price - discount_price
    print("할인 대상입니다.")
else :
    final_price = normal_price
    print("할인 대상이 아닙니다.")
print("기본 금액은 ", normal_price, "원 입니다.")
print("할인 금액은 ", discount_price, "원 입니다.")
print("최종 금액은 ", final_price, "원 입니다.")