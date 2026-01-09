score = int(input("성적을 입력하세요. (0 ~ 100점)"))
grade = "NaN"
if score >= 90 :
    grade = "A"
elif score >= 80 :
    grade = "B"
elif score >= 70 :
    grade = "C"
elif score >= 60 :
    grade = "D"
else :
    grade = "F"

print("학점 ", grade)