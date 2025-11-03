from collections import defaultdict

def countLetters(words):
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter


def countLetters_setDefault(words):
    counter = {}
    for word in words:
        counter.setdefault(word, 0)
        counter[word] += 1
    return counter

def countLetters_defaultdict(words):
    counter = defaultdict(int)
    for word in words:
        counter[word] += 1
    return counter


if __name__ == '__main__':
    words = 'apple'

    dic = countLetters(words)
    print(dic.items())
    print('--' * 10)

    dic = countLetters_setDefault(words)
    print(dic.items())
    print('--' * 10)

    dic = countLetters_defaultdict(words)
    print(dic.items())
    print('--' * 10)
