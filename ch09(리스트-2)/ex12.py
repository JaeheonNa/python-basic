double_list = [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9],
                [11, 12, 13, 14, 15],
               ]
sums = []
for row in range(len(double_list)):
    sum = 0
    for col in range(len(double_list[row])):
        sum += double_list[row][col]
    sums.append(sum)

totalSum = 0
for i in range(len(sums)):
    totalSum += sums[i]
    print(i, "번째 행의 합계:", sums[i])

print("총합:", totalSum)
