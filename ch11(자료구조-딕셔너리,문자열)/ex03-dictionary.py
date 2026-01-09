engDic = {"one":"하나, 일", "two":"둘, 이", "three":"셋, 삼", "four":"넷, 사", "five":"다섯, 오"}
while True:
    key = input("단어를 입력하시오(-1: 종료): ")
    if key in engDic.keys():
        print(engDic[key])
    elif key == "-1":
        break
    else:
        print("해당하는 단어가 없습니다.")
