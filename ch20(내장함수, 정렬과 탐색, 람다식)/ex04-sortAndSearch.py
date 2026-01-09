# sort vs sorted
# sort: 리스트의 메서드. 리스트 원본을 정렬함. sorted보다 약간 성능이 좋음.
# sorted: 내장 함수. 반복 가능한 객체로부터 정렬된 리스트를 생성함. 원본 유지 됨.

a = [4, 2, 1, 5, 7, -1]

print("a: ", a)
b = sorted(a)
print("after sorted a: ", a)
a.sort()
print("after sort a: ", a)
print("--" * 10)

dict1 = {3: "D", 2:"B", 5:"B", 4:"E", 1:"A"}
print(sorted(dict1))
print("--" * 10)

print(sorted("가는 고향 아쉬운 사람 The Health not of their but".split(), key=str.lower))
print("--" * 10)

students = [("나루", 4.5, 20240214), ("아이유", 4.4, 19930516), ("문경진", 4.2, 19890515), ("나재헌", 4.17, 19900528)]
print(sorted(students, key=lambda x: x[2]))
print("--" * 10)

print(sorted(students, key=lambda x: x[2], reverse=True))
print("--" * 10)

data = [(1, 100), (1, 200), (1, 300), (2, 100), (2, 200)]
print(sorted(data, key=lambda x: x[0]))
print("--" * 10)