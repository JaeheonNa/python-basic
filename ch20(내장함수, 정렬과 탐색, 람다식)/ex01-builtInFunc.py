# abs() : 숫자의 절대값을 반환
print("abs()")
i = -20
print("-20의 절대값: ", abs(i))
i = -20.55
print("-20.55의 절대값: ", abs(i))
print("--" * 10)

# all() : 시퀀스 내에 모든 값이 참인지 여부를 반환(0 혹은 False가 포함돼 있으면 False)
print("all()")
li = [0, 1, 2, 3, 4, 5]
print("all([0, 1, 2, 3, 4, 5]): ", all(li))
li = [1, 2, 3, 4, 5, 6]
print("all([1, 2, 3, 4, 5, 6]): ", all(li))
print("--" * 10)

# any() : 시퀀스 내에 하나라도 참인지 여부를 반환(모든 값이 0 혹은 False일 때만 False)
print("any()")
li = [0, 1, 2, 3, 4, 5]
print("any([0, 1, 2, 3, 4, 5]): ", any(li))
li = [0, 0, 0, 0, 0, 0]
print("any([0, 0, 0, 0, 0, 0]): ", any(li))
print("--" * 10)

# bin() : 바이너리 값을 반환
print("bin()")
print("bin(15): ", bin(15))
print("--" * 10)

# eval() : str 수식을 해석하여 연산
print("eval()")
print("eval('4+7'): ", eval("4+7"))
print("--" * 10)

# sum() : 리스트 내 모든 값의 합을 반환
print("sum()")
print("sum([1, 10, 100]): ", sum([1, 10, 100]))
print("--" * 10)

# len() : 길이 반환
print("len()")
print("문자열-len('안녕하세요, Hello!'): ", len("안녕하세요, Hello!"))
print("리스트-len([1, 2, 3, 4, 5, 6, 7]): ", len([1, 2, 3, 4, 5, 6, 7]))
print("딕셔너리-len({'a':1, 'b':2, 'c':3}):", len({'a':1, 'b':2, 'c':3}))
print("튜플-len(('a', 'b', 'c', 'd', 'e')): ", len(('a', 'b', 'c', 'd', 'e')))
print("--" * 10)

# list() : 리스트 생성
print("list()")
s = "abcdefg"
print("list('abcdefg'): ", list(s))
print("--" * 10)

# map() : 시퀀스 내 각각의 요소에 특정 함수를 일괄 적용
print("map()")
def square(num):
    return num ** 2
li = [1, 2, 3, 4, 5]
print("list(map(square, [1, 2, 3, 4, 5])): ", list(map(square, li)))
print("--" * 10)

# dir() : 객체가 갖고 있는 변수나 함수 반환
print("dir()")
print("dir([1, 2, 3]): ", dir([1,2,3]))
print("--" * 10)

# max()/min() : 리스트나 튜플, 문자열에서 가장 큰(작은) 항목 반환
print("max()/min()")
values = [1, 2, 3, 4, 5]
print("max([1, 2, 3, 4, 5]): ", max(values))
print("min([1, 2, 3, 4, 5]): ", min(values))
print("--" * 10)

# enumerate() : 시퀀스 객체를 받아 열거형 객체를 반환
print("enumerate()")
fruits = ["apple", "banana", "cherry", "orange", "strawberry", "grapefruit", "watermelon", "mango", "peach", "melon"]
print("list(enumerate(fruits, start=1)): ", list(enumerate(fruits, start=1)))
print("--" * 10)

# filter() : 특정 조건을 만족하는 요소만을 리스트로 반환
print("filter()")
print("list(filter(lambda x: x.startswith('m'), fruits)): ", list(filter(lambda x: x.startswith('m'), fruits)))
print("--" * 10)

# zip : 2개의 리스트를 튜플을 갖는 리스트 하나로 결합 반환
print("zip()")
numbers = ["하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉", "열"]
print("list(zip(fruits, numbers)): ", list(zip(fruits, numbers)))
print("--" * 10)