import sys

def checkFigure(nodes, currentNode, rootNode, rootNodeCnt):
    if currentNode == rootNode:
        rootNodeCnt += 1


    if currentNode not in nodes.keys() or len(nodes[currentNode]) == 0:
        return 1 # 막대 그래프
    elif len(nodes[currentNode]) == 2:
        return 2 # 8자 그래프
    elif rootNodeCnt == 2:
        return 0# 도넛 그래프

    return checkFigure(nodes, nodes[currentNode][0], rootNode, rootNodeCnt)

def solution(edges):
    sys.setrecursionlimit(10 ** 6) # 재귀 깊이 제한 해제
    answer = []
    nodes = dict()
    for edge in edges:
        nodes[edge[0]] = nodes.get(edge[0], [])
        nodes[edge[0]].append(edge[1])

    nextNodesSet = set()
    for nextNodes in nodes.values():
        for nextNode in nextNodes:
            nextNodesSet.add(nextNode)

    nodesSet = set(nodes.keys())
    oneWayNodes = nodesSet - nextNodesSet
    for node in oneWayNodes:
        if len(nodes[node]) >= 2:
            answer.append(node)
            break

    answer.append(0)
    answer.append(0)
    answer.append(0)

    for rootNode in nodes[answer[0]]:
        result = checkFigure(nodes, rootNode, rootNode, 0)
        if result == 0:
            answer[1] += 1
        elif result == 1:
            answer[2] += 1
        elif result == 2:
            answer[3] += 1

    return answer



if __name__ == '__main__':
    edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
    answer = solution(edges)
    if answer ==[4, 0, 1, 2]:
        print("정답")
    else:
        print("오답: ", answer)