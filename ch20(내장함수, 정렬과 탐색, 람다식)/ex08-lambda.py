orderList = [(1, "재킷", 5, 120000)
             , (2, "셔츠", 6, 24000)
             , (3, "바지", 3, 50000)
             , (4, "코트", 6, 300000)]

result = list(map(lambda x : (x[0], x[2] * x[3]), orderList))
print(result)
print("--" * 10 )

scores = [("국어", 88), ("수학", 90), ("영어", 99), ("자연", 82)]
result = sorted(scores, key=lambda x : x[1])
print(result)

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x : x % 2 == 0, integers))
print("짝수: ", result)
result = list(filter(lambda x : x % 2 != 0, integers))
print("홀수: ", result)

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x : pow(x, 3), integers))
print(result)