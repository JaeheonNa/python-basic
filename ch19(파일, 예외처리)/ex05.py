writeFilePath = "/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/test-03.txt"

file = open(writeFilePath, mode="w", encoding="utf-8")
file.write("안녕하세요. 반갑습니다.\n")
file.write("저는 나재헌입니다.\n")
file.close()

file = open(writeFilePath, mode="a", encoding="utf-8")
file.writelines(", ".join(["하나", "둘", "셋"]))
file.write("\n")
file.writelines("\n".join(["넷", "다섯", "파이팅"]))
file.write("\n")
file.close()