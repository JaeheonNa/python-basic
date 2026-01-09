def test(n1, n2):
    global a
    a = 20
    n1 = n2
    n2 = n1
    b = 10
    print(a, b, n1, n2) # 20, 10 88, 88

a = 10
b = 20
n1 = 77
n2 = 88
test(n1, n2)
print(a, b, n1, n2) # 20, 20, 77, 88