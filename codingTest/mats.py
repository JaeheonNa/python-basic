def getMaxMats(mats, park, row_num, col_num):
    maxMats = -1
    criteria = []
    criteria.append(row_num)
    criteria.append(col_num)
    for mat in mats:
        continueYn = True
        for i in range(mat):
            for j in range(mat):
                check_i = criteria[0] + i
                check_j = criteria[1] + j
                if check_i >= len(park) or check_j >= len(park[0]) or park[check_i][check_j] != "-1":
                   continueYn = False
                   break
            if not continueYn:
                break

        if continueYn:
            maxMats = mat

    return maxMats




def solution(mats, park):
    mats = sorted(mats)
    maxMats = -1
    for row_num in range(len(park)):
        row = park[row_num]
        for col_num in range(len(row)):
            cell = row[col_num]
            if cell == "-1":
                tempMaxMats = getMaxMats(mats, park, row_num, col_num)
                if tempMaxMats > maxMats:
                    maxMats = tempMaxMats
    return maxMats

if __name__ == '__main__':
    mats = [5, 3, 2]
    park = [
        ["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
        ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]
    ]
    answer = solution(mats, park)
    if answer == 3:
        print("정답")
    else:
        print("오답: ", answer)

