file = open("/ch19(파일, 예외처리)/text/test-01.txt", "w", encoding="utf-8")
file.write("아이유\n")
file.close()

file = open("/ch19(파일, 예외처리)/text/test-01.txt", "a", encoding="utf-8")
file.write("바이, 썸머")
file.close()