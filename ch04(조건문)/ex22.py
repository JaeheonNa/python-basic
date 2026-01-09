month = int(input("월을 입력하세요."))

if month == 2:
    year = int(input("연도를 입력하세요."))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, " 년도 ", month, " 월의 일수는 29일 입니다")
    else:
        print(year, " 년도 ", month, " 월의 일수는 28일 입니다")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print(month, "월의 일수는 31일 입니다.")
else:
    print(month, "월의 일수는 30일 입니다.")
