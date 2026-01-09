score = int(input("점수를 입력하세요: "))
grade = "NaN"
if score >= 90:
    grade = "A0"
    if score >= 95:
        grade = "A+"
elif score >= 80:
    grade = "B0"
    if score >= 85:
        grade = "B+"
elif score >= 70:
    grade = "C0"
    if score >= 75:
        grade = "C+"
elif score >= 60:
    grade = "D0"
    if score >= 65:
        grade = "D+"
else:
    grade = "F"

print("입력한 점수는 ", score, " 점 이며, 학점은 ",  grade, " 입니다.")
