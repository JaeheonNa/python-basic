double_list = [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
               ]
print(double_list)
print(double_list[0])
print(double_list[1])
print(double_list[2])

print(id(double_list))
print(id(double_list[0]))
print(id(double_list[1]))
print(id(double_list[2]))

print(len(double_list))
print(len(double_list[0]))
print(len(double_list[1]))
print(len(double_list[2]))

for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        print(double_list[i][j], end=' ')
    print()

rows = int(input("원하는 행을 입력해주세요."))
cols = int(input("원하는 열을 입력해주세요."))

dbl_list = []
for row in range(rows):
    dbl_list.append([])
    for col in range(cols):
        dbl_list[row].append(int(input("값을 입력해주세요.")))
print(dbl_list)

dbl_list = [[0] * cols for row in range(rows)]
print(dbl_list)

li1 = [1,2,3]
li1[0] = 10
print(li1)

li2 = [[1,2], [3,4]]
li2[0][1] = -7
print(li2)