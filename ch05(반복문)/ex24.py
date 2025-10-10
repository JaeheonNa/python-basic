string = input("문자열을 입력해주세요.")
newStatement = ""
for letter in string:
    if letter.isspace():
        continue
    newStatement += letter

print("original statement : ", string)
print("new statement : ", newStatement)
