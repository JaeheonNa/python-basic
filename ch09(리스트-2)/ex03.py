print("=" * 10, "값 복사: 정수형", "=" * 10)
def func_integer(x):
    print("x:", x, "id(x):", id(x))
    x += 10 # 정수형은 immutable object. 변경이 일어나려고 하면, 기존 객체가 변경되는 게 아니라, 새로운 객체가 생김.
    print("x:", x, "id(x):", id(x))

y = 10
print("y:", y, "id(y):", id(y))
func_integer(y)
print("y:", y, "id(y):", id(y))

print("=" * 10, "값 복사: 문자형", "=" * 10)

def func_string_1(x):
    print("x:", x, "id(x):", id(x))
    x += "하세요" # 문자형은 immutable object. 변경이 일어나려고 하면, 기존 객체가 변경되는 게 아니라, 새로운 객체가 생김.
    print("x:", x, "id(x):", id(x))

y = "안녕"
print("y:", y, "id(y):", id(y))
func_string_1(y)
print("y:", y, "id(y):", id(y))

print("=" * 10, "참조: 리스트", "=" * 10)

def func_list(x):
    print("x:", x, "id(x):", id(x))
    x.append("하세요") # 리스트는 mutable object.
    print("x:", x, "id(x):", id(x))

y = ["안녕"]
print("y:", y, "id(y):", id(y))
func_list(y)
print("y:", y, "id(y):", id(y))