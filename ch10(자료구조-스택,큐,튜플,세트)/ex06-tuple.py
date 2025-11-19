x = 10
y = 20
print("값 변경 전:", x, y)
temp = x
x = y
y = temp
print("값 변경 후:", x, y)
print("--" * 10)

(x, y) = (10, 20)
print("값 변경 전: ", (x, y))
(x, y) = (y, x)
print("값 변경 후: ", (x, y))
print("--" * 10)

person = ("나루", 2, "어린이집 원생")
(name, age, student_grade) = person
print("이름:", name, ", 나이:", age, ", 신분:", student_grade)
print("--" * 10)


