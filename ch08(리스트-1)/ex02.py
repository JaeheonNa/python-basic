STUDENT_CNT = 5

scores = []
for i in range(STUDENT_CNT):
    score = int(input("성적을 입력하시오:"))
    scores.append(score)

sum = 0
cnt = 0
for score in scores:
    sum += score
    if score >= 80:
        cnt += 1

print("성적 평균은", sum/STUDENT_CNT, "입니다.")
print("80점 이상 성적을 받은 학생은", cnt, "명 입니다.")
