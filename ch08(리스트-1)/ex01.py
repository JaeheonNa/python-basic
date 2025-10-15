scores = []
print("리스트 값: ", scores)

scores.append(30)
print("리스트 값: ", scores)

scores.append("안녕")
print("리스트 값: ", scores)

scores.append(10.1123)
print("리스트 값: ", scores)
print("리스트 크기: ", len(scores))

scores[0] = "Hello"
print("리스트 값: ", scores)

print("==" * 10)
for i in range(len(scores)):
    print(i, "번째 리스트 값: ", scores[i])

for i in range(len(scores)):
    scores[i] = i + 10
print("리스트 값: ", scores)

for i in scores:
    print(i)

nums = []
for i in range(5):
    nums.append(int(input("정수를 입력하세요: ")))
print(nums)

li1 = list()
print("li1:", li1)

li2 = list(range(0, 5, 2))
print("li2:", li2)

li3 = list("안녕")
print("li3:", li3)

li4 = ["안녕"]
print("li4:", li4)

li5 = [["서울", 10], ["뉴욕", 20], ["파리", 30]]
print("li5:", li5)

for i in range(len(li5)):
    for j in range(len(li5[i])):
        print("li5[", i, "][", j, "]", li5[i][j])