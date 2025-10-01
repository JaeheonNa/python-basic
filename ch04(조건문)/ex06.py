weight = int(input("수화물의 무게 : "))

if weight <= 20 :
    print("추가 비용이 발생하지 않았습니다.")
else :
    additionalFee = (weight - 20) * 20000
    print("추가 비용 : ", additionalFee)