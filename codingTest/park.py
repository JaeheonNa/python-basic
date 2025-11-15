def solution(park, routes):
    answer = []

    for height in range(len(park)):
        h = park[height]
        width = list(h)
        if width.__contains__('S') > 0:
            answer.append(height)
            answer.append(h.index('S'))

    for route in routes:
        do = True
        direction, distance = route.split(' ')
        distance = int(distance)
        if direction == 'E':
            if answer[1] + distance >= len(park[0]):
                do = False
            if do:
                for d in range(1, distance+1):
                    if park[answer[0]][answer[1]+d] == 'X':
                        do = False
                        break
        elif direction == 'S':
            if answer[0] + distance >= len(park):
                do = False
            if do:
                for d in range(1, distance+1):
                    if park[answer[0]+d][answer[1]] == 'X':
                        do = False
                        break
        elif direction == 'W':
            if answer[1] - distance < 0:
                do = False
            if do:
                for d in range(1, distance+1):
                    if park[answer[0]][answer[1]-d] == 'X':
                        do = False
                        break
        else:
            if answer[0] - distance < 0:
                do = False
            if do:
                for d in range(1, distance+1):
                    if park[answer[0]-d][answer[1]] == 'X':
                        do = False
                        break

        if do:
            if direction == 'E':
                answer[1] = answer[1] + distance
            elif direction == 'S':
                answer[0] = answer[0] + distance
            elif direction == 'W':
                answer[1] = answer[1] - distance
            else:
                answer[0] = answer[0] - distance

    return answer

if __name__ == '__main__':
    answer = solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"])
    if answer == [0,0]:
        print("Correct")
    else:
        print("Incorrect:", answer)

    answer = solution(  ["OOOOO", "OOOOO", "OOSOO", "OOOOO", "OOOOO"], ["E 3", "W 3", "S 3", "N 3", "E 2", "E 1", "W 4", "W 1", "S 2", "S 1", "N 4", "N 1"])
    if answer == [0,0]:
        print("Correct")
    else:
        print("Incorrect:", answer)