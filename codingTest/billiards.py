from math import *

def getPowDistance(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    return int(pow(x, 2) + pow(y, 2))

def getOppositePoint(m, n, startX, startY, ball):
    points = []

    if startX != ball[0] or startY <= ball[1]: # bottom 포함
        points.append((ball[0], ball[1] * -1)) # bottom
    if startX != ball[0] or startY >= ball[1]: # top 포함
        points.append((ball[0], ball[1] + 2 * (n - ball[1]))) # top
    if startY != ball[1] or startX <= ball[0]:
        points.append((ball[0] * -1, ball[1])) # left
    if startY != ball[1] or startX >= ball[0]:
        points.append((ball[0] + 2 * (m - ball[0]), ball[1])) # right

    return points

def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        points = getOppositePoint(m, n, startX, startY, ball)
        tempAnswer = []
        for point in points:
            tempAnswer.append(getPowDistance(startX, startY, point[0], point[1]))
        answer.append(min(tempAnswer))
    return answer

if __name__ == "__main__":
    m = 10
    n = 10
    startX = 3
    startY = 7
    balls = [[7, 7], [2, 7], [7, 3]]
    answer = solution(m, n, startX, startY, balls)
    if answer == [52, 37, 116]:
        print("정답")
    else:
        print("오답:", answer)

    m = 10
    n = 10
    startX = 5
    startY = 2
    balls = [[5, 8]]
    answer = solution(m, n, startX, startY, balls)
    if answer == [100]:
        print("정답")
    else:
        print("오답:", answer)
