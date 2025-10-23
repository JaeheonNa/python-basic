def test():
    print(text)         # 함수 안에서 하나의 변수가 전역변수에서 지역변수로 변경될 수 없음. 이 때 에러는 전역 vs 지역 변수 중 어떤 변수를 써야할지 알 수 없어 나는 에러.
    text = "지역변수"
    print(text)

text = "전역변수"
test()

def test():
    global text         # 이 함수 안에서 사용하는 text라는 변수는 전역변수라는 뜻
    print(text)
    text = "지역변수"     # 전역변수의 값을 바꾸게 됨.
    print(text)

text = "전역변수"
test()
print(text)