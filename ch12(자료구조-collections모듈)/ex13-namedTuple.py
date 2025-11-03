def file_read(text):
    fileName = 'text.txt'
    file = open(fileName, mode='r')
    lines = file.readlines()
    for line in lines:
        words = line.strip().split()
        for word in words:
            text.append(word)
    file.close()


if __name__ == "__main__":
    from collections import defaultdict, OrderedDict

    text = []
    file_read(text)
    word_count = defaultdict(int)

    for word in text:
        word_count[word] += 1

    for i, v in dict(sorted(word_count.items(), key=lambda t : t[1], reverse=True)).items():
        if v > 2:
            print("[",i,":", v,"]", end=' ')
    print()
    for i, v in OrderedDict(sorted(word_count.items(), key=lambda t : t[1], reverse=True)).items():
        if v > 2:
            print("[",i,":", v,"]", end=' ')
