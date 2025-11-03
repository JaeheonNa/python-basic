from collections import namedtuple

person1 = ("나재헌", 35, "남")
person2 = ("문경진", 36, "여")
person3 = ("나루", 2, "남")
for n in [person1, person2, person3]:
    print("%s은(는) %d세의 %s성입니다." % n)
print("--" * 10)

Person = namedtuple(typename='Person', field_names=['name', 'age', 'gender'])
p1 = Person("아이유", 32, "여")
p2 = Person("이지은", 32, "여")
for n in [p1, p2]:
    print("%s은(는) %d세의 %s성입니다." % n)
print("p1.name: ", p1.name)
print("p2.name: ", p2.name)

print(p1.name, p1.age, p1.gender)
print(p2[0], p2[1], p2[2])
print("--" * 10)

p3 = Person._make(['유애나', 15, '남'])
print("p3: ", p3)
p3 = p3._replace(name='이지금', gender='여')
print("p3: ", p3)
print("--" * 10)

print("p1._fields: ", p1._fields)
print("getattr(p1, 'name'): ", getattr(p1, 'name'))
print("getattr(p2, 'name'): ", getattr(p2, 'name'))
print("getattr(p3, 'name'): ", getattr(p3, 'name'))
print("--" * 10)

dic = {'name': '나솔', 'age': 0, 'gender':'여'}
p4 = Person(**dic)
print("%s은(는) %d세의 %s성입니다." % (p4.name, p4.age, p4.gender))
print(type(p4))