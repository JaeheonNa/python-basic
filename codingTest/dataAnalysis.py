def solution(data, ext, val_ext, sort_by):
    answer = []
    by = [ "code", "date", "maximum", "remain" ]
    i = by.index(ext)

    for item in data:
        if item[i] < val_ext:
            answer.append(item)

    j = by.index(sort_by)
    answer.sort(key=lambda x: x[j])
    return answer

if __name__ == "__main__":
    # ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
    data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
    ext = "date"
    val_ext = 20300501
    sort_by = "remain"
    answer = solution(data, ext, val_ext, sort_by)
    if answer == [[3,20300401,10,8],[1,20300104,100,80]]:
        print("정답")
    else:
        print("오답:", answer)