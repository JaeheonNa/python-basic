set1 = {2, 1, 3, 5, 4}
print(set1)

set2 = {"Hi", "Bye", "Car", "Person"}
print(set2)

print(len(set1))
print(len(set2))

set3 = {1, 2, "Hi", "Bye", "Car", "Person", "Hi", 1, "Bye"}
print(set3)

if "Hi" in set3:
    print("set3에는 Hi가 존재합니다.")

for value in set3:
    print(value, end=' ')
print()

set4 = set() # set4 = {} (x)
set4.add("spring")
set4.add("summer")
set4.add("autumn")
set4.add("winter")
print(set4)

set4.update({"봄", "여름", "가을", "겨울"})
print(set4)

set4.update({"인간", 1, 2, -1, 6.6})
print(set4)

set4.discard("인간")
print(set4)

set4.remove(6.6)
print(set4)

set4.clear()
print(set4)
print(len(set4))
