def solution(wallpaper):
    answer = [0 for _ in range(4)]
    answer[0] = len(wallpaper) + 1
    answer[1] = len(wallpaper[0]) + 1

    for row_no in range(len(wallpaper)):
        col = list(wallpaper[row_no])
        for col_no in range(len(col)):
            if col[col_no] == "#":
                if answer[0] >= row_no:
                    answer[0] = row_no

                if answer[1] >= col_no:
                    answer[1] = col_no

                if answer[2] <= row_no:
                    answer[2] = row_no

                if answer[3] <= col_no:
                    answer[3] = col_no

    answer[2] += 1
    answer[3] += 1
    return answer


if __name__ == "__main__":
    wallpaper = [".#...", "..#..", "...#."]
    answer = solution(wallpaper)
    if answer == [0, 1, 3, 4]:
        print("정답")
    else:
        print("오답:", answer)
