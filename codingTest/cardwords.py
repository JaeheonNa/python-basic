from collections import deque


def recursive(cards1Deque, cards2Deque, goalDeque):
    answer = ""
    if len(goalDeque) == 0:
        return "Yes"
    else:
        word = goalDeque.popleft()
        if (len(cards1Deque) > 0 and cards1Deque[0] == word) or (
            len(cards2Deque) > 0 and cards2Deque[0] == word
        ):
            if len(cards1Deque) > 0 and cards1Deque[0] == word:
                cards1word = cards1Deque.popleft()
                answer = recursive(cards1Deque, cards2Deque, goalDeque)
                cards1Deque.appendleft(cards1word)

            if len(cards2Deque) > 0 and cards2Deque[0] == word:
                cards2word = cards2Deque.popleft()
                answer = recursive(cards1Deque, cards2Deque, goalDeque)
                cards2Deque.appendleft(cards2word)
        else:
            return "No"

    return answer


def solution(cards1, cards2, goal):
    cards1Deque = deque(cards1)
    cards2Deque = deque(cards2)
    goalDeque = deque(goal)
    answer = recursive(cards1Deque, cards2Deque, goalDeque)

    return answer


if __name__ == "__main__":
    cards1 = ["i", "drink", "water"]
    cards2 = ["want", "to"]
    goal = ["i", "want", "to", "drink", "water"]
    answer = solution(cards1, cards2, goal)
    if answer == "Yes":
        print("정답")
    else:
        print("오답:", answer)

    cards1 = ["i", "water", "drink"]
    cards2 = ["want", "to"]
    goal = ["i", "want", "to", "drink", "water"]
    answer = solution(cards1, cards2, goal)
    if answer == "No":
        print("정답")
    else:
        print("오답:", answer)
