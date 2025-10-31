def getGradeInfo(data_list):
    for i, scores in enumerate(data_list):
        total = 0
        for score in scores:
            total += score
        print("%d 번째 학생의 총점은 %d점이고, 평균은 %0.1f입니다." % (i+1, total, total/len(scores)))

if __name__ == "__main__":
    data_list = [(90, 80), (85, 75), (90, 100)]
    getGradeInfo(data_list)