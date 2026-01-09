def solution(n, m, section):
    answer = 0

    wall = [0 for _ in range(n)]

    for no in section:
        wall[no - 1] = 1

    cursor = 0
    while cursor < len(wall):
        if wall[cursor] == 1:
            for no in range(m):
                if no + cursor < len(wall):
                    wall[no + cursor] = 0
            answer += 1
        cursor += 1

    return answer


if __name__ == "__main__":
    n = 8
    m = 4
    section = [2, 3, 6]
    answer = solution(n, m, section)
    if answer == 2:
        print("정답")
    else:
        print("오답:", answer)
