def solution(infos, n, m):
    cases = {(0,0)}

    for info in infos:
        newCase = set()
        for case in cases:
            if case[0] + info[0] < n:
                newCase.add((case[0] + info[0], case[1]))
            if case[1] + info[1] < m:
                newCase.add((case[0], case[1] + info[1]))
        cases = newCase

    if not cases:
        return -1

    return min(a for a, b in cases)

if __name__ == '__main__':
    info = [[1, 2], [2, 3], [2, 1]]
    n, m = 1, 7
    answer = solution(info, n, m)
    if answer == 0:
        print("정답")
    else:
        print("오답:", answer)