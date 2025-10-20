data = []
dir = "/Users/heonyboogy/PycharmProjects/python-basic/text.txt"
fp = open(dir, mode="r", encoding="utf-8")
for line in fp.readlines():
    print(line.strip())

fp = open(dir, mode="w", encoding="utf-8")
fp.write("안녕하세요.\n")
fp.write("영광입니다.\n")
fp.close()
print("-" * 10)

fp = open(dir, mode="r", encoding="utf-8")
for line in fp.readlines():
    print(line.strip())

fp = open(dir, mode="a", encoding="utf-8")
fp.write("네, 안녕하세요.\n")
fp.write("저도 영광입니다.\n")
fp.close()
print("-" * 10)

fp = open(dir, mode="r", encoding="utf-8")
for line in fp.readlines():
    print(line.strip())