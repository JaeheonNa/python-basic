words = "Nice to meet you!"
print(words[0], words[5], words[-1])

fruits = ["apple", "banana", "peach", "tomato"]
print(fruits[0], fruits[2], fruits[-1])

print("words의 길이:", len(words))
print("fruits의 길이:", len(fruits))

li1 = [1, 2]
print("li1의 id:", id(li1))
li2 = [3, 4, 5]
print("li2의 id:", id(li2))
li3 = li1 + li2
print("li3의 id:", id(li3))
print("li3:", li3)

print(["안녕", "Hi"] * 3)

print(10 in [1, 2, 3])
print(10 not in [1, 2, 3])

print(max([1, 10, 100, 50]))
print(min([1, 10, 100, 50]))

for i in "일이삼":
    print(i)