from collections import defaultdict

def countWords(words):
    counter = defaultdict(list)
    for word in words:
        length = len(word)
        counter[length].append(word)
    return counter


if __name__ == '__main__':
    li1 = ['감자', '귤', '사과', '배', '오징어', '꼼장어', '불가사리']
    dic = countWords(li1)
    print(dic)
