file = open("/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/test-1.txt", "w", encoding="utf-8")
file.write("아이유\n")
file.close()

file = open("/Users/jaeheon.na/PycharmProjects/PythonProject/ch19(파일, 예외처리)/text/test-1.txt", "a", encoding="utf-8")
file.write("바이, 썸머")
file.close()