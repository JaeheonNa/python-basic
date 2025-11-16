

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    videoLength = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])
    position = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
    opening_start = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
    opening_end = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])

    for command in commands:
        if position >= opening_start and position <= opening_end:
            position = opening_end

        if 'next' == command:
            position += 10
            if position > videoLength:
                position = videoLength

        if 'prev' == command:
            position -= 10
            if position < 0:
                position = 0

    if position >= opening_start and position <= opening_end:
        position = opening_end

    minute = position // 60
    second = position % 60

    if minute < 10:
        answer += '0' + str(minute)
    else:
        answer += str(minute)

    answer += ":"
    if second < 10:
        answer += '0' + str(second)
    else:
        answer += str(second)
    return answer

if __name__ == '__main__':
    answer = solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"])
    if ("13:00" == answer):
        print("정답")
    else:
        print("오답: ", answer)