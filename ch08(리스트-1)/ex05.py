naru = ["나루", 2, "84cm", "14kg"]
print("naru[2]:", naru[2])
print("naru[-3]:", naru[-3])
print("naru[1:3]:", naru[1:3])
print("naru[:3]:", naru[:3])
print("naru[3:]:", naru[3:])

print("naru의 id:", id(naru))
li1 = naru[:3]
print("li1의 id:", id(li1))
li2 = naru[3:]
print("li2의 id:", id(li2))

words = ["a", "b", "c", "d", "e", "f", "g", "h"]
print("words의 id:", id(words))
words[1:4] = ["B", "C", "D"]
print("words:", words)
print("words의 id:", id(words))
words[:] = []
print("words의 id:", id(words))
words = []
print("words의 id:", id(words))