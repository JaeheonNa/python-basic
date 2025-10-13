# Call by reference
# Python에서는 매개변수에 인자를 넘길 때, 그 인자가 list나 dictionary라면 주소값을 넘김.
# list나 dictionary는 mutable object임.

def change(dictionary):
    dictionary["height"] = 84
    return dictionary

dictionary = {"name":"나루", "age":2}

print("호출 전 list의 값:", dictionary)
print("호출 전 list의 주소(id):", id(dictionary))
x = change(dictionary)
print("호출 후 list의 값:", dictionary)
print("호출 후 list의 주소(id):", id(dictionary))
print("호출 후 s의 값:", x)
print("호출 후 s의 주소(id):", id(x))