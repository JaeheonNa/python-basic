print("map()")
li = [1, 2, 3, 4, 5]
print("li = [1, 2, 3, 4, 5]")
f = lambda x: x * 2
print("f = lambda x: x * 2")
map_result = list(map(f, li))
print("list(map(f, li)): ", map_result)
print('--' * 10)

print("filter()")
li = [1, 2, 3, 4, 5]
print("li = [1, 2, 3, 4, 5]")
f = lambda x : x % 2 == 0
print("f = lambda x : x % 2 == 0")
print("list(filter(f, li)): ", list(filter(f, li)))
print('--' * 10)

print("sorted()")
li = [(1, 300), (1, 200), (1, 100), (2, 300), (2, 200), (2, 100)]
print("li =  [(1, 300), (1, 200), (1, 100), (2, 300), (2, 200), (2, 100)]")
f = lambda x : x[1]
print("f = lambda x : x[1]")
print("sorted(li, key=f): ", sorted(li, key=f))
print('--' * 10)

print("reduce()")
from functools import *
li = [1, 2, 3, 4, 5]
print("li = [1, 2, 3, 4, 5]")
f = lambda x, y : x * y
print("f = lambda x, y : x * y")
print("reduce(f, li): ", reduce(f, li))