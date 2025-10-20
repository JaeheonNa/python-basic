colors = ["red", "orange", "yellow", "green", "blue", "purple"]
search_word = input("찾고자 하는 색깔을 입력하세요.")
if search_word in colors:
    colorIdx = colors.index(search_word)
    print("찾고자하는 단어는 Index", colorIdx, "에 존재합니다.")
else:
    print("찾고자하는 단어가 없습니다.")
print("="*10)

def sequential_search(list, key):
    cnt = 0;
    for idx in range(len(list)):
        if list[idx] == key:
            cnt += 1
    return cnt
num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100]
integer = int(input("찾을 정수를 입력하세요."))
return_value = sequential_search(num_list, integer)
if return_value > 0:
    print(integer, "은/는", return_value, "개 존재합니다.")
else:
    print(integer, "은/는 존재하지 않습니다.")

target_num = int(input("정수를 입력하세요."))
result = []
for num in num_list:
    if num >= target_num:
        result.append(num)

print("결과: ", result)
print("총", len(result), "개")