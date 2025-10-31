from collections import deque
import time

print("--" * 5, "append 성능 테스트", "--" * 5)
deque_test = deque()
start = time.time()
for i in range(100000):
    deque_test.append(i)
end = time.time()
print("deque append: ", end - start)

list_test = list()
start = time.time()
for i in range(100000):
    list_test.append(i)
end = time.time()
print("list append: ", end - start)

# print("--" * 5, "pop 성능 테스트", "--" * 5)
# start = time.time()
# for i in range(len(deque_test)):
#     deque_test.pop()
# end = time.time()
# print("deque pop: ", end - start)
#
# start = time.time()
# for i in range(len(list_test)):
#     list_test.pop()
# end = time.time()
# print("list pop: ", end - start)

print("--" * 5, "popleft 성능 테스트", "--" * 5)
start = time.time()
for i in range(len(deque_test)):
    deque_test.popleft()
end = time.time()
print("deque popleft: ", end - start)

start = time.time()
for i in range(len(list_test)):
    list_test.pop(0)
end = time.time()
print("list pop(0): ", end - start)

print("결론1: stack 자료형을 쓸 땐, list가 미세하게 우세.")
print("결론2: queue 자료형을 쓸 땐, deque가 압도적으로 우세.")