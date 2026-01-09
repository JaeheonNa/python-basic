def solution(diffs, times, limit):
    answer = max(diffs)
    minLevel = 1
    maxLevel = max(diffs)

    while minLevel <= maxLevel:
        mid = (minLevel + maxLevel) // 2

        if canSolve(diffs, mid, times, limit):
            answer = mid
            maxLevel = mid -1
        else:
            minLevel = mid +1

    return answer

def canSolve(diffs, level, times, limit):
    totalTime = 0
    timeTakes = [diff - level for diff in diffs]  # 몇 번 수행해야 풀 수 있는지
    for i in range(len(timeTakes)):
        cnt = timeTakes[i]
        if cnt < 0: cnt = 0
        if i - 1 >= 0:
            totalTime += (times[i] + times[i - 1]) * cnt + times[i]
        else:
            totalTime = times[i] * cnt + times[i]
    if totalTime <= limit:
        return True
    else:
        return False

if __name__ == "__main__":
    diffs = [1, 5, 3]
    times = [2, 4, 7]
    limit =30
    answer = solution(diffs, times, limit)
    if answer == 3:
        print("정답")
    else:
        print("오답: ", answer)

    diffs = [1, 4, 4, 2]
    times = [6, 3, 8, 2]
    limit = 59
    answer = solution(diffs, times, limit)
    if answer == 2:
        print("정답")
    else:
        print("오답: ", answer)

    level = 294
    diffs = [1, 328, 467, 209, 54]
    times = [2, 7, 1, 4, 3]
    limit = 1723
    answer = solution(diffs, times, limit)
    if answer == 294:
        print("정답")
    else:
        print("오답: ", answer)

    diffs = [1, 99999, 100000, 99995]
    times = [9999, 9001, 9999, 9001]
    limit = 3456789012
    answer = solution(diffs, times, limit)
    if answer == 39354:
        print("정답")
    else:
        print("오답: ", answer)