i = 0
cnt = 0
total = 0
while True:
    i = int(input(str(cnt+1)+ "번째 학생의 성적을 입력하세요."))
    if i < 0 :
        break
    total += i
    cnt += 1

if cnt != 0:
    print(cnt, "명의 학생 점수 합계:", total, ", 평균:", total / cnt)
