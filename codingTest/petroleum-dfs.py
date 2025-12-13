from collections import deque
import copy

def checkPetroleum(drilling, trialLand, oilId, oilIdCntMap):
    petroleumCnt = 0
    oil = []

    while len(drilling) > 0 :
        site = drilling.popleft()
        depth = site[0]
        trial = site[1]
        if trialLand[depth][trial] == 1 and (depth, trial) not in oil:
            petroleumCnt += 1
            oil.append((depth, trial))
            if len(trialLand) > depth + 1:
                drilling.append([trialLand, depth + 1, trial])
            if 0 <= depth - 1:
                drilling.append([trialLand, depth - 1, trial])
            if len(trialLand[0]) > trial + 1:
                drilling.append([trialLand, depth, trial + 1])
            if 0 <= trial - 1:
                drilling.append([trialLand, depth, trial - 1])

    for depth, trial in oil:
        trialLand[depth][trial] = oilId
    oilIdCntMap[oilId] = petroleumCnt


def solution(land):
    answer = 0
    oilId = 1
    trialCnt = len(land[0])
    oilIdCntMap = {}
    for trial in range(trialCnt):
        trialLand = copy.deepcopy(land)
        for depth in range(len(trialLand)):
            if trialLand[depth][trial] == 1:
                oilId += 1
                drilling = deque()
                drilling.append([depth, trial])
                checkPetroleum(drilling, trialLand, oilId, oilIdCntMap)





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