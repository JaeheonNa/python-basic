def solution(keymap, targets):
    answer = []

    keyDict = dict()
    for key in keymap:
        for i in range(len(key)):
            alpha = key[i]
            cnt = keyDict.get(alpha, len(key))
            if cnt > i:
                keyDict[alpha] = i

    for target in targets:
        tempAnswer = 0
        for alpha in target:
            if keyDict.get(alpha, -1) == -1:
                tempAnswer = -1
                break
            tempAnswer += keyDict.get(alpha) + 1
        answer.append(tempAnswer)
    return answer


if __name__ == "__main__":
    keymap = ["ABACD", "BCEFD"]
    targets = ["ABCD", "AABB"]
    answer = solution(keymap, targets)
    if answer == [9, 4]:
        print("정답")
    else:
        print("오답:", answer)
