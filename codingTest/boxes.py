from collections import deque

def solution(n, w, num):
    answer = 0

    directionRight = True
    boxes = []
    box = deque()

    position = [0,0]
    where = [0,0]
    for i in range(1, n + 1):
        if i == num:
            where[0] = position[0]
            where[1] = position[1]
        if len(box) < w:
            if directionRight:
                box.append(i)
            else:
                box.appendleft(i)
        else:
            boxes.append(box.copy())
            box = deque()
            directionRight = not directionRight
            if directionRight:
                box.append(i)
            else:
                box.appendleft(i)
        if i % w == 0:
            position[1] += 1
        elif directionRight:
            position[0] += 1
        else:
            position[0] -= 1



    answer = position[1] - where[1]

    if len(box) > 0:
        leng = len(box)
        for _ in range(w - leng):
            if directionRight:
                box.append(0)
            else:
                box.appendleft(0)
        boxes.append(box.copy())

    if len(boxes) > position[1]:
        if boxes[len(boxes)-1][where[0]] != 0:
            answer += 1


    return answer

if __name__ == '__main__':
    answer = solution(22, 6, 8)
    print(answer)
    answer = solution(13, 3, 6)
    print(answer)