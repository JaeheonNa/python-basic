string = input("문자열을 입력해주세요.")
reversedString = ""
for letter in string:
    reversedString = letter + reversedString
print("Reversed string : ", reversedString)

s_list = list(string)
s_list.reverse()
print("Reversed string : ", end=" ")
print("".join(s_list))

s1 = string
print("Reversed string : ", end=" ")
print("".join(reversed(s1)))

print("Reversed string : ", end=" ")
print(string[::-1])