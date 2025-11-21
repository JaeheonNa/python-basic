filePath = "/Users/heonyboogy/PycharmProjects/python-basic/ch19(파일, 예외처리)/text/input.txt"
file = open(filePath, "r", encoding="utf-8")
for line in file:
    print(line)
file.close()
print("--" * 10)

filePath = "/Users/heonyboogy/PycharmProjects/python-basic/ch19(파일, 예외처리)/text/proverbs.txt"
file = open(filePath, "r", encoding="utf-8")
for line in file:
    line = line.rstrip()
    wordList = line.split()
    for word in wordList:
        print(word)
file.close()
print("--" * 10)

line = "apple,grape,banana,pear"
wordList = line.split(",")
for word in wordList:
    print(word)
print("--" * 10)

filePath = "/Users/heonyboogy/PycharmProjects/python-basic/ch19(파일, 예외처리)/text/input.txt"
file = open(filePath, "r", encoding="utf-8")
ch = file.read(1)
while ch != "":
    print(ch)
    ch = file.read(1)
file.close()
print("--" * 10)

