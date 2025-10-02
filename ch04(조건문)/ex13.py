total_score = float(input("총 이수 학점을 입력하세요: "))
gpa_score = float(input("평균 점수를 입력하세요: "))

if total_score >= 140 and gpa_score >= 2.0 :
    print("졸업 대상자입니다.")
else :
    print("졸업할 수 없습니다.")