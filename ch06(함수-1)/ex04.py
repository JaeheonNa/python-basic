def fToC(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    return round(temp_c,2)

temp_f = float(input("화씨 온도를 입력해주세요."))
temp_c = fToC(temp_f)
print("화씨", temp_f, "도는 섭씨", temp_c, "도입니다.")