if __name__ == "__main__":
    fileName = input("입력 파일 이름: ")
    file = open(fileName, mode="r")
    # file = open("words.txt", mode="r")
    lines = file.readlines()
    lineSet = set()
    for line in lines:
        words = line.strip().split()
        for word in words:
            lineSet.add(word.removesuffix(".").lower())

    print("사용된 단어의 수: ", len(lineSet))
    print(lineSet)
    file.close()