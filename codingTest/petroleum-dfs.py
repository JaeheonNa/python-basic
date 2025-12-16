from collections import deque

def checkPetroleum(drilling, land, oilId, oilIdCntMap):
    petroleumCnt = 0
    oil = set()

    while len(drilling) > 0 :
        site = drilling.popleft()
        depth = site[0]
        trial = site[1]
        if land[depth][trial] == 1 and (depth, trial) not in oil:
            petroleumCnt += 1
            oil.add((depth, trial))
            if len(land) > depth + 1:
                drilling.append([depth + 1, trial])
            if 0 <= depth - 1:
                drilling.append([depth - 1, trial])
            if len(land[0]) > trial + 1:
                drilling.append([depth, trial + 1])
            if 0 <= trial - 1:
                drilling.append([depth, trial - 1])

    for depth, trial in oil:
        land[depth][trial] = oilId
    oilIdCntMap[oilId] = petroleumCnt


def solution(land):
    answer = 0
    oilId = 2
    trialCnt = len(land[0])
    oilIdCntMap = {}
    for trial in range(trialCnt):
        for depth in range(len(land)):
            if land[depth][trial] == 1:
                oilId += 1
                drilling = deque()
                drilling.append([depth, trial])
                checkPetroleum(drilling, land, oilId, oilIdCntMap)
                oilId += 1


    for trial in range(trialCnt):
        encounterOil = set()
        tempAnswer = 0
        for depth in range(len(land)):
            if land[depth][trial] > 1:
                encounterOil.add(land[depth][trial])
        for oid in encounterOil:
            tempAnswer += oilIdCntMap[oid]
        if tempAnswer > answer:
            answer = tempAnswer
    return answer

if __name__ == '__main__':
    land = [[0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1]]
    answer = solution(land)
    if answer == 9:
        print("정답")
    else:
        print("오답: ", answer)