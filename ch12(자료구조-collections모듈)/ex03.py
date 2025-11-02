from collections import OrderedDict

# python 3.7 버전부터는 dictionary의 순서가 보장됨.
# python 3.7 미만의 dictionary = HashMap
# python 3.7 이상의 dictionary = LinkedHashMap
dict1 = dict()
dict1['a'] = 100
dict1['b'] = 200
dict1['c'] = 300
dict1['d'] = 400
dict1['e'] = 500

for k, v in dict1.items():
    print(k, v)

# 정렬도 가능함
dict3 = dict()
dict3['e'] = 100
dict3['d'] = 200
dict3['c'] = 300
dict3['b'] = 400
dict3['a'] = 500
print(sorted(dict3.items(), key=lambda x: x[0])) # 키 기준 정렬
print(sorted(dict3.items(), key=lambda x: x[1])) # 값 기준 정렬

print('==' * 5, "[OrderedDict를 사용하는 이유-1]", '==' * 5)
# OrderedDict는 동등성 비교 시 순서를 고려함.
# Dictionary는 동등성 비교 시 순서를 고려하지 않음. 논리적 동등.
dict2 = dict()
dict2['e'] = 500
dict2['d'] = 400
dict2['c'] = 300
dict2['b'] = 200
dict2['a'] = 100

print("dict1 == dict2: ", dict1 == dict2) # 순서가 달라도 참.

orderedDict1 = OrderedDict()
orderedDict1['a'] = 100
orderedDict1['b'] = 200
orderedDict1['c'] = 300
orderedDict1['d'] = 400
orderedDict1['e'] = 500

orderedDict2 = OrderedDict()
orderedDict2['e'] = 500
orderedDict2['d'] = 400
orderedDict2['c'] = 300
orderedDict2['b'] = 200
orderedDict2['a'] = 100

print("orderedDict1 == orderedDict2: ", orderedDict1 == orderedDict2) # 순서가 다르면 거짓.
reversedOrderedDict2 = OrderedDict(sorted(orderedDict2.items(), key=lambda x: x[0]))
print("orderedDict1 == reversedOrderedDict2: ", orderedDict1 == reversedOrderedDict2) # 순서가 같으면 참.

# OrderedDict.move_to_end()
print('==' * 5, "[OrderedDict를 사용하는 이유-2]", '==' * 5)
print(orderedDict1)
orderedDict1.move_to_end('a')
print(orderedDict1)
orderedDict1.move_to_end('a', last=False)
print(orderedDict1)

