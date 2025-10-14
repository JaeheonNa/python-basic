# 튜플은 리스트와 거의 비슷한 자료 구조 형태. 소괄호로 표현.
# 리스트와 달리 한 번 값으로 만들면 값을 변경할 수 없음.

def tuple_return():
    return 1, "안녕", 5 # 튜플 형태로 반환함.

a, b, c = tuple_return()
print(a, b, c)

tuple_var =  tuple_return()
print(tuple_var)

list_var = list(tuple_var)
print(list_var)