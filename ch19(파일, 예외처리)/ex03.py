filePath = "/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/test-1.txt"

try:
    file = open(filePath, mode="r")
    line = file.readline()
    print(line)
    print("안녕")
finally:
    file.close()
    print("First file closed.")

with open(filePath, "r") as file:
    line = file.readline()
    print(line)
    print("안녕")

print("Second file closed.")

