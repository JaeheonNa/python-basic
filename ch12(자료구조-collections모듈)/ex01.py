from collections import deque

deque_list = deque()
print(deque_list)

for i in range(5):
    deque_list.append(i)

print(deque_list)
print(deque_list.pop())
print(deque_list.popleft())
print(deque_list)

print("--" * 10)
deque_list.clear()
for i in range(5):
    deque_list.appendleft(i)
print(deque_list)
print(deque_list.pop())
print(deque_list.pop())
print(deque_list.pop())
print(deque_list)

print("--" * 10)
deque_list.clear()
for i in range(5):
    deque_list.appendleft(i)
print(deque_list)
deque_list.rotate(1)
print(deque_list)
deque_list.rotate(-1)
print(deque_list)

print("--" * 10)
deque_list.clear()
for i in range(5):
    deque_list.appendleft(i)
print(deque_list)
deque_list.reverse()
print(deque_list)
print(deque(reversed(deque_list)))

print("--" * 10)
deque_list.clear()
for i in range(5):
    deque_list.appendleft(i)
print(deque_list)
deque_list.extend([5, 6, 7])
print(deque_list)
deque_list.extendleft([5, 6, 7])
print(deque_list)

print("--" * 10)
deque_list.clear()
basedata = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
deque_list = deque(basedata, maxlen=5)
print(deque_list)
print(deque_list.popleft())
print(deque_list)
