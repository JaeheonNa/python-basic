from collections import defaultdict

def countWords(words):
    grouper = defaultdict(set)
    for word in words:
        length = len(word)
        grouper[length].add(word)
    return grouper


if __name__ == '__main__':
    li1 = ['한국', '미국', '스페인', '우즈베키스탄', '사우디아라비아']
    set1 = set(li1)
    dic = countWords(set1)
    print(dic)
