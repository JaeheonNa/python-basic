string = input("전화번호를 입력해주세요.")
number = ""
for letter in string:
    if letter == "-":
        continue
    number += letter

print("phone_num : ", number)
