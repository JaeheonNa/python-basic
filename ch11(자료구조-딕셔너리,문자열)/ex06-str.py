string = "안녕 john 난 지금 학교 가고 있어"
li1 = string.split()
print(type(li1))
print(li1)

string = "안녕,john,난,지금,학교,가고,있어"
li2 = string.split(",")
print(type(li2))
print(li2)

string = "안녕/john/난/지금/학교/가고/있어"
li3 = string.split("/")
print(type(li3))
print(li3)


import regex

string = "안녕|john,난/지금|학교/가고,있어"
li3 = regex.split("[/|,]", string)
print(type(li3))
print(li3)
print("--" * 10)

string = "abcd"
print("'abcd'.isalpha(): ", string.isalpha())
string = "abcd1"
print("'abcd1'.isalpha(): ", string.isalpha())
string = "가나다"
print("'가나다'.isalpha(): ", string.isalpha())

string = "123"
print("'123'.isdigit(): ", string.isdigit())
print("'123'.isnumeric(): ", string.isnumeric())
print("'123'.isdecimal(): ", string.isdecimal())

string = "-10"
print("'-10'.isdigit(): ", string.isdigit())
print("'-10'.isnumeric(): ", string.isnumeric())
print("'-10'.isdecimal(): ", string.isdecimal())

string = "3.14"
print("'3.14'.isdigit(): ", string.isdigit())
print("'3.14'.isnumeric(): ", string.isnumeric())
print("'3.14'.isdecimal(): ", string.isdecimal())

string = "½"
print("'½'.isdigit(): ", string.isdigit())
print("'½'.isnumeric(): ", string.isnumeric())
print("'½'.isdecimal(): ", string.isdecimal())
print("--" * 10)

string = "  "
print("'   '.isspace(): ", string.isspace())
string = " ddd "
print("' ddd '.isspace(): ", string.isspace())
print("--" * 10)

string = input("파이썬 소스를 입력해주세요: ")
if string.endswith(".py"):
    print("올바른 파일 이름입니다.")
else:
    print("파이썬 파일의 확장자가 아닙니다.")

string = "2025-10.30.txt"
if string.startswith("2025"):
    print("2025년 파일입니다.")
else:
    print("2025년 파일이 아닙니다.")
print("--" * 10)

string = input("영단어를 입력하세요: ")
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())
print("--" * 10)

string = "{}b{}"
print(string.format("a", "c"))
print("--" * 10)

stringList = ["a", "b", "c"]
print("!".join(stringList))
print("--" * 10)

string = "jaeheon@gmail.com"
emailTuple = string.partition("@")
id = emailTuple[0]
mailDomain = emailTuple[2]
print("id: ", id)
print("mailDomain: ", mailDomain)
print("--" * 10)

string = "aaaaaabdcdadsf"
print("string.count('a'): ", string.count("a"))
print("string.count('z'): ", string.count("z"))
print("--" * 10)

string = "President Trump agreed to allow South Korea to build nuclear powered submarine."
print(string.find("Korea"))
print(string.index("Korea"))
print(string.find("Japan"))
# print(string.index("Japan")) 없으면 에러
print("--" * 10)

string = "   apple   orange   "
print("시작", string.strip(), "끝")
print("시작", string.lstrip(), "끝")
print("시작", string.rstrip(), "끝")