id = input("아이디를 입력하세요.")
password = "1234"
id_list = ["cat", "dog", "bird", "tiger", "lion", "elephant"]

if id in id_list:
    pw = input("비밀번호를 입력하세요.")
    if pw == password:
        print(id, " 님이 로그인했습니다.")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("아이디가 없습니다.")