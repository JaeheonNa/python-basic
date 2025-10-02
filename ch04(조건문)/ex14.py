height = float(input("키를 입력하세요.")) / 100
weight = float(input("몸무게를 입력하세요."))

bmi = weight / (height * height)

print("BMI 지수는 ", bmi, "입니다.")

if bmi >= 20 and bmi < 25 :
    print("정상입니다.")
elif bmi >= 25:
    print("비만입니다.")
else :
    print("마른 체형입니다.")