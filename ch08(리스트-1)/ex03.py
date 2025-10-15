dogs = []
while True:
    dog = input("강아지의 이름을 입력하시오(종료시에는 엔터키):")
    if len(dog) > 0:
        dogs.append(dog)
    else:
        break

print("강아지들의 이름")
for dog in dogs:
    print(dog, end=" ")