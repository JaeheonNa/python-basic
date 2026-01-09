from collections import deque

def solution(board, h, w):
    answer = 0

    boardDeque = deque()
    for row in board:
        rowDeque = deque(row)
        rowDeque.appendleft(0)
        rowDeque.append(0)
        boardDeque.append(rowDeque)

    boardDeque.appendleft([[0] for _ in range(len(boardDeque[0]))])
    boardDeque.append([[0] for _ in range(len(boardDeque[0]))])

    height = [0, 0, 1, -1]
    width = [1, -1, 0, 0]
    h += 1
    w += 1
    for i in range(4):
        if boardDeque[h][w] == boardDeque[h + height[i]][w + width[i]]:
            answer += 1

    return answer

if __name__ == '__main__':
    board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
    h = 1
    w = 1
    answer = solution(board, h, w)
    print(answer)