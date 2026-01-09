from collections import defaultdict

dic = defaultdict(lambda: 0)
print(dic['a'])
print(dic['b'])
print(dic)

print("--" * 10)
dic.clear()
dic = defaultdict(int)
print(dic['a'])
print(dic['b'])
print(dic)

print("--" * 10)
dic.clear()
dic = defaultdict(float)
print(dic['a'])
print(dic['b'])
print(dic)

print("--" * 10)
dic.clear()
dic = defaultdict(str)
print(dic['a'])
print(dic['b'])
print(dic)

print("--" * 10)
dic.clear()
dic = defaultdict(int)
dic['a'] += 100
print(dic['a'])
print(dic['b'])
print(dic)