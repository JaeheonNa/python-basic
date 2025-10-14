def readList():
    score_list = []
    flag = True
    while flag:
        score = int(input("점수를 입력하세요(종료를 하시려면 음수(-)를 입력하세요):"))
        if score < 0:
            flag = False
        else:
            score_list.append(score)
    return score_list

def processList(score_list):
    score_list.sort()

def writeList(score_list):
    for score in score_list:
        print(score)