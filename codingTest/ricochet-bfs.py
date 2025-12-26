from collections import deque

def solution(board):
    answer = 1

    boardDeque = deque(board)
    frontRearRow = ''
    for _ in range(len(board[0])):
        frontRearRow += 'D'
    boardDeque.appendleft(frontRearRow)
    boardDeque.append(frontRearRow)

    startX = 0
    startY = 0

    for i in range(len(boardDeque)):
        row = deque(boardDeque.popleft())
        row.appendleft('D')
        row.append('D')
        if row.__contains__('R'):
            startX = i
            for y in range(len(row)):
                if row[y] == 'R':
                    startY = y
        boardDeque.append(row)

    bfsDeque = deque()
    bfsDeque.append([startX, startY])

    X = [0, 0, 1, -1]
    Y = [1, -1, 0, 0]

    record = set()
    while len(bfsDeque) > 0:
        tempDeque = deque()
        while(len(bfsDeque) > 0):
            cur = bfsDeque.popleft()
            tempDeque.append(cur)
        while len(tempDeque) > 0:
            cur = tempDeque.popleft()
            for i in range(4):
                x = X[i]
                y = Y[i]
                next = [cur[0]+x, cur[1]+y]
                while boardDeque[next[0]][next[1]] != 'D':
                    next[0] += x
                    next[1] += y
                next[0] -= x
                next[1] -= y
                if boardDeque[next[0]][next[1]] == 'G':
                    return answer
                if cur != next and (next[0], next[1]) not in record:
                    bfsDeque.append(next)
                    record.add((next[0], next[1]))
        answer += 1

    return -1

if __name__ == "__main__":
    board = ["...D..R",
             ".D.G...",
             "....D.D",
             "D....D.",
             "..D...."]
    answer = solution(board)
    if answer == 7:
        print("정답")
    else:
        print("오답:", answer)
