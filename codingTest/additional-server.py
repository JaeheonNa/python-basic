def solution(players, m, k):
    answer = 0
    serverInNeed = []
    for _ in range(24):
        serverInNeed.append(1)

    for i in range(24):
        currentPlayer = players[i]
        currentServer = serverInNeed[i]
        if currentPlayer >= currentServer * m:
            totalServerInNeed = currentPlayer // m
            additionalServer = totalServerInNeed - currentServer + 1
            answer += additionalServer
            for j in range(k):
                if i + j < 24:
                    serverInNeed[i + j] += additionalServer
    return answer

if __name__ == '__main__':
    players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
    m = 3
    k = 5
    answer = solution(players, m, k)
    if answer == 7:
        print("정답")
    else:
        print("오답: ", answer)
