cities = ["서울", "경기", "인천", "대전", "광주", "대구", "부산"]
print(len(cities))
print(type(cities))
print(cities)
print("2번째 도시 : ", cities[1])
print("3번째 도시 : ", cities[2])
print("3번째 도시 변경")
cities[2] = "춘천"
print("3번째 도시 : ", cities[2])

temp = ["서울", "대구", 10, 3.14]
print(temp)

name = input("이름: ")
age = int(input("나이: "))
address = input("주소: ")
height = int(input("키: "))
weight = int(input("몸무게: "))
person = [name, age, address, height, weight]
print(person)