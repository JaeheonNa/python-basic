readFilePath = "/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/sales.txt"
writeFilePath = "/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/summary.txt"
file = open(readFilePath, "r", encoding="utf-8")
totalSales = 0
dayCnt = 0
try:
    line = file.readline()
    while line != "":
        totalSales += int(line)
        dayCnt += 1
        line = file.readline()
finally:
    file.close()

meanSales = totalSales / dayCnt

file = open(writeFilePath, "w", encoding="utf-8")
try:
    file.write("총 매출: %d\n" % totalSales)
    file.write("평균 매출: %d\n" % meanSales)
finally:
    file.close()

##
# file.read():      모든 파일의 내용을 문자열로 읽어들임.
# file.readline():  한 번에 한 라인을 문자열로 읽어들임.
# file.readlines(): 여러 라인을 한꺼번에 리스트로 읽어들임. 기본적으로 개행, 빈칸이 포함됨.
print("1. read() 함수 읽기")
readFilePath = "/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/test-2.txt"
file = open(readFilePath, "r", encoding="utf-8")
string = file.read()
print(string)
file.close()
print("--" * 10)

print("2. readline() 함수 읽기")
readFilePath = "/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/test-2.txt"
file = open(readFilePath, "r", encoding="utf-8")
line = file.readline()
print(line, end='')
file.close()
print("--" * 10)

print("3. readlines() 함수 읽기")
readFilePath = "/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/test-2.txt"
file = open(readFilePath, "r", encoding="utf-8")
lines = file.readlines()
print(lines)
file.close()
print("--" * 10)
