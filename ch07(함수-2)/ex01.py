# Call by value(= Pass by value)
# Python에서는 매개변수에 인자를 넘길 때, 그 인자가 숫자형이라면 주소값이 아니라 값을 넘김.

def change(num):
    num = num + 10
    print("change() 내의 num 값:", num)
    print("change() 내의 num 의 주소(id):", id(num))
    return num

n = 100
print("호출 전 n의 값:", n)
print("호출 전 n의 주소(id):", id(n))
x = change(n)
print("호출 후 n의 값:", n)
print("호출 후 n의 주소(id):", id(n))
print("호출 후 x의 값:", x)
print("호출 후 x의 주소(id):", id(x))
