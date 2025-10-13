# Call by value(= Pass by value)
# Python에서는 매개변수에 인자를 넘길 때, 그 인자가 문자열이라면 주소값이 아니라 값을 넘김.
# 숫자형과 문자열은 immutable object임.

def change(string):
    string = string + "공부합니다."
    print("change() 내의 string 값:", string)
    print("change() 내의 string 의 주소(id):", id(string))
    return string

string = "안녕하세요 저는 파이썬을 "
print("호출 전 n의 값:", string)
print("호출 전 n의 주소(id):", id(string))
x = change(string)
print("호출 후 n의 값:", string)
print("호출 후 n의 주소(id):", id(string))
print("호출 후 x의 값:", x)
print("호출 후 x의 주소(id):", id(x))
