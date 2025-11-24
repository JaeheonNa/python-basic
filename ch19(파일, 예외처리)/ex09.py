filePath = "/Users/heonyboogy/PycharmProjects/python-basic/ch19(파일, 예외처리)/text/mobydick.txt"
file = open(filePath, "r", encoding="utf-8")

alphaDict = dict()
char = file.read(1)
while char != "":
    if char.isalpha():
        alphaDict[char.lower()] = alphaDict.get(char.lower(), 0) + 1
    char = file.read(1)
file.close()
print("--"*10)

file = open(filePath, "r", encoding="utf-8")
count = [0] * 26
char = file.read(1)
while char != "":
    char = char.lower()
    if char >= "a" and char <= "z":
        i = ord(char) - ord("a")
        count[i] += 1
    char = file.read(1)
file.close()
