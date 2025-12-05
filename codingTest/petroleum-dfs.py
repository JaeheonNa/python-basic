from collections import deque
import copy

def checkPetroleum(drilling):
    petroleumCnt = 0
    while len(drilling) > 0 :
        site = drilling.popleft()
        trialLand = site[0]
        depth = site[1]
        trial = site[2]
        if trialLand[depth][trial] == 1:
            petroleumCnt += 1
            trialLand[depth][trial] = 0
            if len(trialLand) > depth + 1:
                drilling.append([trialLand, depth + 1, trial])
            if 0 <= depth - 1:
                drilling.append([trialLand, depth - 1, trial])
            if len(trialLand[0]) > trial + 1:
                drilling.append([trialLand, depth, trial + 1])
            if 0 <= trial - 1:
                drilling.append([trialLand, depth, trial - 1])
    return petroleumCnt


def solution(land):
    answer = 0
    trialCnt = len(land[0])
    for trial in range(trialCnt):
        trialLand = copy.deepcopy(land)
        petroleumCnt = 0
        for depth in range(len(trialLand)):
            if trialLand[depth][trial] == 1:
                drilling = deque()
                drilling.append([trialLand, depth, trial])
                petroleumCnt += checkPetroleum(drilling)
        if petroleumCnt > answer:
            answer = petroleumCnt

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