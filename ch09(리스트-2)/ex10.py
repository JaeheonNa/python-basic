list_1 = [4, 8, 9 , -1, 10]
list_1.sort()
print(list_1)
list_1.sort(reverse=True)
print(list_1)

# 선택 정렬

def selection_sort(list):
    cnt = 0
    for i in range(len(list)):
        min = list[i]
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < min:
                min = list[j]
                min_index = j
            if min_index == j:
                list[i], list[min_index] = list[min_index], list[i]
                cnt += 1
    print("총", cnt, "번 교환이 이뤄졌습니다.")

list_2 = [4, 8, 9 , -1, 10, -2, 7, 5]
selection_sort(list_2)
print("selection_sort:", list_2)

def buble_sort(list):
    cnt = 0
    for i in range(len(list)):
        for j in range(len(list) - i):
            if ((j+1) < len(list)) and (list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
                cnt += 1
    print("총", cnt, "번 교환이 이뤄졌습니다.")

list_3 = [4, 8, 9 , -1, 10, -2, 7, 5]
buble_sort(list_3)
print("buble_sort:", list_3)