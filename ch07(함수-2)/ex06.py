def test1():
    # text = "(지역변수) 파이썬 공부"
    print(text)

text = "(전역변수) 파이썬 공부"
test1()

def test2():
    text = "(지역변수) 파이썬 공부"
    print(text)

text = "(전역변수) 자바 공부"
test2()
print(text)