def getMinuteTime(strSchedule):
    if len(strSchedule) == 3:
        hour = int(strSchedule[0]) * 60
        minute = int(strSchedule[1] + strSchedule[2])
        return hour + minute
    else:
        hour = int(strSchedule[0] + strSchedule[1]) * 60
        minute = int(strSchedule[2] + strSchedule[3])
        return hour + minute

def solution(schedules, timelogs, startday):
    answer = 0
    cnts = []
    for _ in range(len(schedules)):
        cnts.append(0)
    for i in range(len(schedules)):
        timelog = timelogs[i]
        for _ in range(startday - 1):
            time = timelog.pop(len(timelog)-1)
            timelog.insert(0, time)
        schedule = getMinuteTime(str(schedules[i]))
        for j in range(5):
            time = timelog[j]
            minuteTime = getMinuteTime(str(time))
            if minuteTime <= schedule + 10:
                cnts[i] += 1

    for cnt in cnts:
        if cnt == 5:
            answer += 1
    return answer



if __name__ == "__main__":
    schedules = [700, 800, 1100]
    timelogs = [[710, 2359, 1050, 700, 650, 631, 659],
                [800, 801, 805, 800, 759, 810, 809],
                [1105, 1001, 1002, 600, 1059, 1001, 1100]]
    startday = 5
    answer = solution(schedules, timelogs, startday)
    if answer == 3 :
        print("정답")
    else:
        print("오답:", answer)