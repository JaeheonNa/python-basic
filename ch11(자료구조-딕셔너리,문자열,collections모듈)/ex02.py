scores = {"국어":80, "수학":95, "영어":80}

print("--" * 5, "key 출력", "--" * 5)
print(scores.keys())

for subject in scores.keys():
    print(subject, end=" ")
print()

for subject in scores:
    print(subject, end=" ")
print()

print("--" * 5, "value 출력", "--" * 5)
print(scores.values())

for score in scores.values():
    print(score, end=" ")
print()

print("--" * 5, "key-value 출력", "--" * 5)
for scoreSet in scores.items():
    print(scoreSet, end=" ")
    print(scoreSet[0], scoreSet[1])

print("--" * 5, "dictionary 생성", "--" * 5)
dic = dict()
print(dic)
triples = {x : pow(x, 3) for x in range(6)}
print(triples)

print("--" * 5, "dictionary 정렬", "--" * 5)
dic1 = {"cups":2, "bags":1, "books":5, "bottles":4, "coins":7}
print(dic1)
print(sorted(dic1))
print(sorted(dic1.keys()))
print(sorted(dic1.values()))
print(sorted(dic1.items()))
print(sorted(dic1, key=dic1.__getitem__)) # 값에 따라 키를 정렬
