from collections import deque

def solution(bandage, health, attacks):
    maxHealth = health
    time = attacks[len(attacks)-1][0]
    attacks = deque(attacks)

    healCnt = 0
    for i in range(time+1):
        attack = attacks.popleft()
        if attack[0] == i:
            health -= attack[1]
            healCnt = 0
            if health <= 0:
                return -1
        else:
            attacks.appendleft(attack)
            health += bandage[1]
            healCnt += 1
            if healCnt == bandage[0]:
                healCnt = 0
                health += bandage[2]
            if health >= maxHealth:
                health = maxHealth

    return health

if __name__ == '__main__':
    bandage = [5, 1, 5]
    health = 30
    attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]

    answer = solution(bandage, health, attacks)
    if answer == 5:
        print("정답")
    else:
        print("오답: ", answer)

    bandage = [3, 2, 7]
    health = 20
    attacks = [[1, 15], [5, 16], [8, 6]]
    answer = solution(bandage, health, attacks)
    if answer == -1:
        print("정답")
    else:
        print("오답: ", answer)

    bandage =  [4, 2, 7]
    health = 20
    attacks = [[1, 15], [5, 16], [8, 6]]
    answer = solution(bandage, health, attacks)
    if answer == -1:
        print("정답")
    else:
        print("오답: ", answer)

    bandage = [1, 1, 1]
    health = 5
    attacks = [[1, 2], [3, 2]]
    answer = solution(bandage, health, attacks)
    if answer == 3:
        print("정답")
    else:
        print("오답: ", answer)