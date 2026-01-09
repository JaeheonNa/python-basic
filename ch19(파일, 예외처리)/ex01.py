file = open('/ch19(파일, 예외처리)/text/test-00.txt', mode="r", encoding="utf-8")
line = file.readline()
while line != "":
    print(line.strip())
    line = file.readline()
file.close()