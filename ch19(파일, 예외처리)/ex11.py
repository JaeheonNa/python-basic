import csv

filePath = "text/weather.csv"
file = open(filePath, "r", encoding='euc-kr')
data = csv.reader(file)

header = next(data)
minTemperature = 1000

for row in data:
    if  minTemperature > float(row[3]):
        minTemperature = float(row[3])

print("최저 기온은 %.2f도 입니다." % minTemperature)

file.close()