from functools import reduce

def solution(picks, minerals):
    answer = 0
    trialCnt = reduce(lambda acc, x : acc + x,  picks, 0)
    trialCnt *= 5
    if trialCnt > len(minerals):
        trialCnt = len(minerals)
    windowCnt = trialCnt // 5
    if trialCnt % 5 != 0:
        windowCnt += 1

    windowTired = []
    for i in range(windowCnt):
        iWindowTiredSum = 0
        mineral = []
        for j in range(5):
            index = i * 5 + j
            if len(minerals) > index:
                if minerals[index] == "diamond" :
                    iWindowTiredSum += 25
                elif minerals[index] == "iron" :
                    iWindowTiredSum += 5
                else:
                    iWindowTiredSum += 1
                mineral.append(minerals[index])
        windowTired.append((i, iWindowTiredSum, mineral))

    windowTired.sort(key=lambda x: x[1], reverse=True)

    while picks != [0, 0, 0] and len(windowTired) > 0 :
        window = windowTired.pop(0)
        if window[2] == []:
            break

        if picks[0] > 0:
            picks[0] -= 1
            answer += len(window[2])
        elif picks[1] > 0:
            picks[1] -= 1
            answer += len(window[2])
            answer += len(list(filter(lambda x: x == "diamond", window[2]))) * 4
        elif picks[2] > 0:
            picks[2] -= 1
            answer += len(window[2])
            answer += len(list(filter(lambda x: x == "iron", window[2]))) * 4
            answer += len(list(filter(lambda x: x == "diamond", window[2]))) * 24

    return answer

if __name__ == "__main__":
    picks = [1, 3, 2]
    minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
    answer = solution(picks, minerals)
    if answer == 12:
        print("정답")
    else:
        print("오답:", answer)