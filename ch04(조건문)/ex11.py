input_str = input("문자열을 입력하세요. ")
length = len(input_str)

if length % 2 == 1:
    print(input_str[length//2])
else :
    print(input_str[(length // 2) - 1], input_str[length // 2])