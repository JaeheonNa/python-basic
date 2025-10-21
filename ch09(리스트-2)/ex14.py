scores = [
            [100, 100, 100],
            [20, 20, 20],
            [30, 30, 30],
            [40, 40, 40],
            [50, 50, 50]
        ]

cal_scores = []
cal_scores.append(["번호", "국어", "영어", "수학", "총점", "평균"])
total_scores = []
total_scores.append("총점")

for i in range(len(scores)):
    row = []
    row.append(i + 1)
    sum = 0
    for j in range(len(scores[i])):
        sum += scores[i][j]
        row.append(scores[i][j])
    row.append(sum)
    row.append(sum / len(scores[i]))
    cal_scores.append(row)

for col in range(1, len(cal_scores[0])):
    sum = 0
    for row in range(1, len(cal_scores)):
        sum += cal_scores[row][col]
    total_scores.append(sum)

total_scores[len(total_scores) -1] = total_scores[len(total_scores) -1] / (len(cal_scores) - 1)
cal_scores.append(total_scores)


for row in cal_scores:
    print(row)