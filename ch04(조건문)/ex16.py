appleQuality = input("사과의 상태는?")

if appleQuality == "좋음" :
    applePrice = int(input("사과 1개당 가격을 입력하세요."))
    if applePrice < 1000 :
        print("10개를 산다.")
    else:
        print("5개를 산다.")
else:
    print("사지 않는다.")