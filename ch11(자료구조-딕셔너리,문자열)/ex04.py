fileName = input("파일 이름 입력: ")
# file = open(fileName, 'r')
file = open(file=fileName, mode='r', encoding='utf-8')
lines = file.readlines()
wordsSet = dict()
for line in lines:
    words = line.strip().split()
    for word in words:
        word = word.removesuffix('.')
        wordsSet[word] = wordsSet.get(word, 0) + 1

print(wordsSet)
file.close()