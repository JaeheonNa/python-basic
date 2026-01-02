def solution(board):
    answer = 1
    oCnt = 0
    xCnt = 0
    oWin = 0
    xWin = 0
    rCross = ''
    lCross = ''

    for i in range(3):
        if board[i] == 'XXX':
            xWin += 1
        if board[i] == 'OOO':
            oWin += 1
        if board[0][i] + board[1][i] + board[2][i] == 'OOO':
            oWin += 1
        if board[0][i] + board[1][i] + board[2][i] == 'XXX':
            xWin += 1
        rCross += board[i][i]
        lCross += board[i][2 - i]
        for j in range(3):
            if board[i][j] == 'O':
                oCnt += 1
            if board[i][j] == 'X':
                xCnt += 1

    if rCross == 'OOO' or lCross == 'OOO':
        oWin += 1
    if rCross == 'XXX' or lCross == 'XXX':
        xWin += 1

    if oCnt < xCnt:
        answer = 0
    if oCnt - xCnt > 1:
        answer = 0
    if oWin >= 1 and xWin >= 1:
        answer = 0
    if oWin == 1 and oCnt <= xCnt:
        answer = 0
    if xWin == 1 and xCnt < oCnt:
        answer = 0


    return answer

if __name__ == "__main__":
    board = ["OOO", "O..", "XXX"]
    answer = solution(board)
    if answer == 1:
        print("정답")
    else:
        print("오답:", answer)