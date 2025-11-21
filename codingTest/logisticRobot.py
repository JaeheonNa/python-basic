def solution(points, routes):
    answer = 0

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