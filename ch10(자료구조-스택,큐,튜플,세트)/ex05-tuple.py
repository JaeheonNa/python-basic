colors = ("red", "green", "blue")
print(colors)
print(type(colors))

numbers = (1, 2, 3, 4, 5)
print(numbers)
print(type(numbers))

tuple1 = (1, 2.2, 'hi')
print(tuple1)

tuple2 = ()
print(tuple2)

tuple3 = (3)
print(tuple3)
print(type(tuple3))
tuple4 = (3, )
print(tuple4)
print(type(tuple4))

li = [1, 2, 3, 4, 5]
tuple5 = tuple(li)
print(li)
print(tuple5)

tuple6 = (1, 2, 3)
tuple7 = tuple6, ("안", "녕")
print(tuple7)
print(id(tuple6))
print(id(tuple7[0]))

t1 = (1, 2, 3, 4, 5.5, 6)
print("t1의 길이: ", len(t1))
print("t1의 가장 큰 값: ", max(t1))
print("t1의 가장 작은 값: ", min(t1))

t2 = (1, 2, 3)
t3 = (4, 5.5, 6)
t4 = t2 + t3
print(t4)

t5 = t4 * 2
print(t5)

if 5.5 in t5:
    print("t5에는 5.5가 존재함.")

for x in t5:
    print(x, end=' ')
print()

t6 = (1, 2.2, 3, "철수", "영희", 6)
print(t6[3])
print(t6[-3])
print(t6[-3:-1])

print(dir(t6))

t7 = (1, 2.2, 3, 6)
t8 = (1, 2.2, 3, 6)
t9 = (1, 2.2, 3, 6.6)
print(t7.__eq__(t8))
print(t7.__eq__(t9))