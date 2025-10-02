name = "나재헌"
age = 35
height = 152

print("-"*10, "AND 연산자", "-"*10,)
if (age >= 15) and (height >= 160) :
    print("Both are True")
    print("놀이기구를 탈 수 있습니다.")
else :
    print("At Least one of them is False")
    print("놀이기구를 탈 수 없습니다.")

print("-"*10, "OR 연산자", "-"*10,)

if (age >= 15) or (height >= 160) :
    print("At Least one of them is True")
else :
    print("Both are False")

print("-" * 10, "NOT 연산자", "-" * 10, )

if not name == "나재헌" :
    print("나재헌이 아닙니다.")
else :
    print("나재헌입니다.")