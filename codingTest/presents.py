class Friend:

    def __init__(self, name, friends):
        self.name = name
        self.friends = dict()
        self.giveCnt = 0
        self.getCnt = 0
        self.point = 0
        self.presents = 0

        cnt = [0 for x in range(len(friends))]
        for friend, cnt in zip(friends, cnt):
            if(self.name != friend):
                self.friends[friend] = cnt

    def setCnt(self, presentHistory):
        for present in presentHistory:
            history = present.split()
            if history[0] == self.name:
                self.friends[present.split()[1]] = self.friends.get(present.split()[1], 0) + 1
                self.giveCnt += 1
            else:
                self.getCnt += 1
            self.point = self.giveCnt - self.getCnt



def solution(friends, gifts):
    answer = 0

    friendDict = dict()
    for myName in friends:
        me = Friend(myName, friends)
        history = [history for history in gifts if myName in history.split()]
        me.setCnt(history)
        friendDict[myName] = me

    for myName, me in friendDict.items():
        for friendsName, giveCnt in me.friends.items():
            getCnt = friendDict[friendsName].friends[myName]
            if giveCnt > getCnt:
                me.presents += 1
            elif (giveCnt == getCnt) and (me.point > friendDict[friendsName].point):
                me.presents += 1

    for myName, me in friendDict.items():
        if me.presents > answer:
            answer = me.presents

    return answer

if __name__ == '__main__':
    friends = ["muzi", "ryan", "frodo", "neo"]
    gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    answer = solution(friends, gifts)
    if answer == 2:
        print("정답")
    else:
        print("오답: ", answer)