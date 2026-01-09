word = "python"
print("단어 길이: ", len(word))
print("5번째 글자: ", word[4])
print("3번째 글자: ", word[2])
print("마지막 글자: ", word[len(word) - 1])

first_word = input("첫번째 어절을 입력하세요.")
second_word = input("두번째 어절을 입력하세요.")
third_word = input("세번째 어절을 입력하세요.")


abbreviation = first_word[0] + second_word[0] + third_word[0]
print(abbreviation)