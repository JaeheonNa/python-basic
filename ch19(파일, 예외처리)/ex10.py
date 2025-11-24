filePath = "/Users/heonyboogy/PycharmProjects/python-basic/ch19(파일, 예외처리)/text/%s"
fileName = input("파일명을 입력하세요.")
filePath = filePath % fileName.strip()

freqDict = dict()

file = open(filePath, "r", encoding="utf-8")
for line in file:
    for char in line:
        char = char.strip()
        freqDict[char] = freqDict.get(char, 0) + 1

print(freqDict)


file.close()