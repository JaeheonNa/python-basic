import csv

filePath = "/Users/heonyboogy/PycharmProjects/python-basic/ch19(파일, 예외처리)/text/weather.csv"
file = open(filePath, "r", encoding='euc-kr')
data = csv.reader(file)

header = next(data)
for row in data:
    print(row)
file.close()