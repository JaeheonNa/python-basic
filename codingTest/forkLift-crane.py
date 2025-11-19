from collections import deque

def prepare_1(storage):
    newStorage = deque()
    for row in storage:
        newRow = deque(row)
        newStorage.append(newRow)

    outerContainerSet = set()
    for i in range(len(newStorage[0])):
        outerContainerSet.add((0, i))
        outerContainerSet.add((len(newStorage) -1, i))

    for i in range(len(newStorage)):
        outerContainerSet.add((i, 0))
        outerContainerSet.add((i, len(newStorage[0]) - 1))

    return newStorage, outerContainerSet

def checkAndAddNewOuterContainer(row, col, storage, outerContainerSet, memo):
    if row+1 < len(storage) and storage[row+1][col] != "0":
        outerContainerSet.add((row+1, col))
    elif row+1 < len(storage) and storage[row+1][col] == "0" and not memo.__contains__((row+1, col)) and not outerContainerSet.__contains__((row+1, col)):
        memo.add((row + 1, col))
        checkAndAddNewOuterContainer(row+1, col, storage, outerContainerSet, memo)

    if row-1 >= 0 and storage[row-1][col] != "0":
        outerContainerSet.add((row-1, col))
    elif row-1 >= 0 and storage[row-1][col] == "0" and not memo.__contains__((row-1, col)) and not outerContainerSet.__contains__((row-1, col)):
        memo.add((row-1, col))
        checkAndAddNewOuterContainer(row-1, col, storage, outerContainerSet, memo)

    if col+1 < len(storage[0]) and storage[row][col+1] != "0":
        outerContainerSet.add((row, col+1))
    elif col+1 < len(storage[0]) and storage[row][col+1] == "0" and not memo.__contains__((row, col+1)) and not outerContainerSet.__contains__((row, col+1)):
        memo.add((row, col + 1))
        checkAndAddNewOuterContainer(row, col+1, storage, outerContainerSet, memo)

    if col-1 >= 0 and storage[row][col-1] != "0":
        outerContainerSet.add((row, col-1))
    elif col-1 >= 0 and storage[row][col-1] == "0" and not memo.__contains__((row, col-1)) and not outerContainerSet.__contains__((row, col-1)):
        memo.add((row, col-1))
        checkAndAddNewOuterContainer(row, col-1, storage, outerContainerSet, memo)

def useForkLift(storage, outerContainerSet, request):
    moveOutContainerSet = set()
    for row, col in outerContainerSet:
        if storage[row][col] == request:
            moveOutContainerSet.add((row, col))

    for row, col in moveOutContainerSet:
        storage[row][col] = "0"
        memo = {(row, col)}
        checkAndAddNewOuterContainer(row, col, storage, outerContainerSet, memo)


def useCrane(storage, outerContainerSet, request):
    moveOutContainerSet = set()
    for row in range(len(storage)):
        for col in range(0, len(storage[0])):
            if storage[row][col] == request:
                moveOutContainerSet.add((row, col))

    for row, col in moveOutContainerSet:
        storage[row][col] = "0"
        if outerContainerSet.__contains__((row, col)):
            memo = {(row, col)}
            checkAndAddNewOuterContainer(row, col, storage, outerContainerSet, memo)

def solution(storage, requests):
    answer = 0
    refinedStorage, outerContainerSet = prepare_1(storage)
    for request in requests:
        if len(request) == 1:
            useForkLift(refinedStorage, outerContainerSet, request)
        else:
            useCrane(refinedStorage, outerContainerSet, request[0])

    for i in range(len(refinedStorage)):
        row = refinedStorage[i]
        for j in range(len(row)):
            cell = row[j]
            if cell != "0" :
                answer += 1

    return answer

if __name__ == '__main__':
    storage = ["AZWQY",
               "CAABX",
               "BBDDA",
               "ACACA"]
    requests = ["A", "BB", "A"]
    answer = solution(storage, requests)
    if answer == 11:
        print("정답")
    else:
        print("오답:", answer)