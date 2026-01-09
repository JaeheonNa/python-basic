set1 = {1, 2, 3}
set2 = {1, 2, 3}

print("set1 == set2: ", set1 == set2)
print("set1 != set2: ", set1 != set2)

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

print("set1 > set2: ", set1 > set2)                     # 부분집합 여부
print("set2.issubset(set1): ", set2.issubset(set1))     # 부분집합 여부

print("set1.issuperset(set2): ", set1.issuperset(set2)) # 상위집합 여부

setString1 = set("안녕하세요.")
print(setString1)

if "안" in setString1:
    print("'안' 문자는 setString1에 포함돼 있습니다.")

setString2 = set({"안녕하세요."})
print(setString2)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3}
print("set1 | set2: ", set1 | set2)             # 합집합
print("set1.union(set2): ", set1.union(set2))   # 합집합
print("set2.union(set1): ", set2.union(set1))   # 합집합

print("set1 & set2: ", set1 & set2)                             # 교집합
print("set1.intersection(set2): ", set1.intersection(set2))     # 교집합
print("set2.intersection(set1): ", set2.intersection(set1))     # 교집합

print("set1 - set2: ", set1 - set2)                             # 차집합
print("set1.difference(set2): ", set1.difference(set2))         # 차집합
print("set2.difference(set1): ", set2.difference(set1))         # 차집합

# 0은 False, 나머지는 모두 True
set1 = {0, 1, 2, 3}
print("all(set1): ", all(set1))
set1.discard(0)
print("all(set1): ", all(set1))
print("any(set1): ", any(set1))
set1.clear()
set1.add(0)
print("any(set1): ", any(set1))

set1 = {10, 20, 30, 40, 50}
set2 = {1, 2, 3, 4, 5}
print("set1.isdisjoint(set2): ", set1.isdisjoint(set2)) # 두 집합의 교집합이 공집합인가?

print("set2.pop(): ", set2.pop()) # 임의의 값을 pop()
print("set2.pop(): ", set2.pop()) # 임의의 값을 pop()
print("set2.pop(): ", set2.pop()) # 임의의 값을 pop()

for _ in range(len(set1)):
    print("set1.pop(): ", set1.pop())

set1 = {"한국", "미국", "스페인", "영국", "일본"}
for _ in range(len(set1)):
    print("set1.pop(): ", set1.pop())
