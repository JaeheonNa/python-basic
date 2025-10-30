def isPalindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return False
    return True

if __name__ == "__main__":
    word = input("문자열을 입력하시오: ")
    word = word.replace(" ", "")
    print(word, "의 회문 여부: ", isPalindrome(word))