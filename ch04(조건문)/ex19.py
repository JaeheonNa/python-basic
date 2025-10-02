birth_year = int(input("태어난 연도를 입력하세요."))

age = 2025 - birth_year + 1

print("태어난 연도: ", birth_year)
print("나이: ", age)


if age < 8:
    print("미취학 아동")
elif 8 <= age <= 13:
    print("초등학생")
elif 14 <= age <= 16:
    print("중학생")
elif 17 <= age <= 19:
    print("고등학생")
else:
    print("성인")