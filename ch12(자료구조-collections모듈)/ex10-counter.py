from collections import Counter
from itertools import repeat, chain

text = list("high school")
counter = Counter(text)
print(type(counter))
print(counter)
print(counter['h'])

print('--' * 10)
count = Counter(b=2, a=3, c=5)
print(count)
print(sorted(count.elements()))

li1 = list(repeat(['a', 'b', 'c'], 2))
li1.append(['a', 'c', 'c', 'c'])
print(sorted(chain.from_iterable(li1)))
print('--' * 10)

text = 'abcdefg repeat count! You can do it. Nice to meet you. A Coun' \
    'telephone!!!!'.lower().split()
print(text)
wordCnt = Counter(text)
print(wordCnt)
print('--' * 10)

count = Counter({"가":4, "나":3})
print(count)
print(list(count.elements()))