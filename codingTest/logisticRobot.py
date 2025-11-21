def solution(points, routes):
    answer = 0

    allRobotsRoute = []
    for i in range(len(routes)):
        iRobotsPointRoute = routes[i]
        iRobotsRoute = []
        iRobotsRoute.append(points[iRobotsPointRoute[0]-1].copy())
        for j in range(1, len(iRobotsPointRoute)):
            nextPoint = points[iRobotsPointRoute[j]-1]
            currentPoint = iRobotsRoute[len(iRobotsRoute)-1].copy()
            while nextPoint != currentPoint:
                if currentPoint[0] != nextPoint[0]:
                    if currentPoint[0] > nextPoint[0]:
                        currentPoint[0] -= 1
                    else:
                        currentPoint[0] += 1
                else:
                    if currentPoint[1] > nextPoint[1]:
                        currentPoint[1] -= 1
                    else:
                        currentPoint[1] += 1
                iRobotsRoute.append(currentPoint.copy())
        allRobotsRoute.append(iRobotsRoute)

    maxTime = 0
    for robotsRoute in allRobotsRoute:
        if maxTime < len(robotsRoute):
            maxTime = len(robotsRoute)

    for time in range(maxTime):
        currentRobotsPointDict = dict()
        for robotsRoute in allRobotsRoute:
            if len(robotsRoute) > time:
                currentRobotsPointDict[str(robotsRoute[time])] = currentRobotsPointDict.get(str(robotsRoute[time]), 0) + 1
        for key, value in currentRobotsPointDict.items():
            if value > 1:
                answer += 1

    return answer

if __name__ == '__main__':
    points = [[3, 2], [6, 4], [4, 7], [1, 4]]
    routes = [[4, 2], [1, 3], [4, 2], [4, 3]]
    answer = solution(points, routes)
    if answer == 9:
        print("정답")
    else:
        print("오답:", answer)

    points = [[3, 2], [6, 4], [4, 7], [1, 4]]
    routes = [[4, 2], [1, 3], [2, 4]]
    answer = solution(points, routes)
    if answer == 1:
        print("정답")
    else:
        print("오답:", answer)

    points = [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]]
    routes = [[2, 3, 4, 5], [1, 3, 4, 5]]
    answer = solution(points, routes)
    if answer == 0:
        print("정답")
    else:
        print("오답:", answer)