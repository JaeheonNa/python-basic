# 사용자로부터 참석자 수를 받아 치킨은 인당 1개, 맥주는 인당 2병, 케잇은 인당 4개를 출력하는 프로그램 작성

number = int(input("참석자 수를 입력하세요"))
print(type(number))
chicken = number
beer = number * 2
cake = number * 4

print("chicken = ", chicken)
print("beer = ", beer)
print("cake = ", cake)