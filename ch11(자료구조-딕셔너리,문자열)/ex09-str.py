def getAcronym(string):
    words = string.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym

if __name__ == "__main__":
    string = input("문자열을 입력하시오: ")
    print("머리문자열: ", getAcronym(string))