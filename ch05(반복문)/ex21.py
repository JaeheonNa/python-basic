fruit = "apple"
for letter in fruit:
    print(letter, end=" ")
print("")
print("--" * 10)

string = input("문자열(영어)를 입력하세요")
vowels = "aeiouAEIOU"
for letter in string:
    if letter not in vowels:
        print(letter, end="")
print("")
print("--" * 10)

string = input("문자열(영어)를 입력하세요")
vowel_cnt = 0
consonant_cnt = 0
for letter in string:
    if letter.isalpha():
        if letter not in vowels:
            consonant_cnt += 1
        else:
            vowel_cnt += 1

print("모음 수: ", vowel_cnt)
print("자음 수: ", consonant_cnt)