def solution(wallet, bill):
    answer = 0

    while True:
        if (wallet[0] < bill[0] or wallet[1] < bill[1]) and (wallet[0] < bill[1] or wallet[1] < bill[0]):
            if bill[0] < bill[1]:
                bill[1] = bill[1] // 2
            else :
                bill[0] = bill[0] // 2
            answer += 1
        else:
            break

    return answer

if __name__ == '__main__':
    answer = solution([30, 15],	[26, 17])
    if answer == 1:
        print('정답')
    else:
        print('오답: ', answer)