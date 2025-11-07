import copy

li1 = [1, 2, 3, 4, 5]
print("li의 id:", id(li1))
li2 = li1
li1.insert(0, 0)

print("li1:", li1)
print("li1의 id:", id(li1))
print("li2:", li2)
print("li2의 id:", id(li2))