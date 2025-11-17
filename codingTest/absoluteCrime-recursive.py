def solution(info, n, m):
    a = 0
    b = 0
    answers = []

    recursive(info, n, m, a, b, 0, answers)

    if answers == []:
        return -1
    answer = min(answers)
    return answer

def recursive(info, n, m, a, b, depth, answers):
    if(depth == len(info)):
        if n > a and m > b:
            answers.append(a)
            minN = min(answers)
            answers.clear()
            answers.append(minN)
        return
    elif len(answers) > 0 and answers[0] < a:
        return

    if a + info[depth][0] < n:
        recursive(info, n, m, a + info[depth][0], b, depth + 1, answers)

    if b + info[depth][1] < m:
        recursive(info, n, m, a, b + info[depth][1], depth + 1, answers)

if __name__ == '__main__':
    info = [[1, 2]
          , [2, 3]
          , [2, 1]]
    n, m = 4, 4
    answer = solution(info, n, m)
    if answer == 2:
        print("정답")
    else:
        print("오답:", answer)