writeFilePath = "/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/test-03.txt"

file = open(writeFilePath, mode="r", encoding="utf-8")
print("파일 포인터의 현재 위치: ", file.tell())
print(file.read())
print("파일 포인터의 현재 위치: ", file.tell())
print("--" * 10)

print(file.seek(0))
print("파일 포인터의 현재 위치: ", file.tell())
print("--" * 10)
print(file.seek(6))
print("파일 포인터의 현재 위치: ", file.tell())
print("--" * 10)
print(file.read())