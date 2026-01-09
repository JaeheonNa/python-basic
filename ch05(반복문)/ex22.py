string = input("문자열을 입력해주세요.")
alpha_cnt = 0
space_cnt = 0
num_cnt = 0
for letter in string:
    if letter.isalpha():
        alpha_cnt += 1
    elif letter.isspace():
        space_cnt += 1
    elif letter.isdigit():
        num_cnt += 1

print("알파벳 수: ", alpha_cnt)
print("공백 수: ", space_cnt)
print("숫자 수: ", num_cnt)
