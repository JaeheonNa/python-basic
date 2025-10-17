friends = []

def menu_print():
    num = int(input("# 1. 친구 리스트 출력 \n"
                    "# 2. 친구 추가 \n"
                    "# 3. 친구 삭제 \n"
                    "# 4. 이름 변경 \n"
                    "# 9. 종료 \n"
                    "# 메뉴를 선택하시오: "
                    ))
    return num

while True:
    num = menu_print()
    if num == 1:
        print("친구 목록:", friends)
    elif num == 2:
        name = input("추가할 친구의 이름을 입력하시오:")
        friends.append(name)
        print(name, "이/가 추가됐습니다.")
    elif num == 3:
        del_name = input("삭제할 친구의 이름을 입력하시오:")
        if del_name in friends:
            friends.remove(del_name)
            print(del_name, "이/가 삭제됐습니다.")
        else:
            print(del_name, "이/가 존재하지 않습니다.")
    elif num == 4:
        pre_name = input("변경할 친구의 이름을 입력하시오:")
        if pre_name in friends:
            idx = friends.index(pre_name)
            post_name = input("친구의 새 이름을 입력하시오:")
            friends[idx] = post_name
        else:
            print(pre_name, "이/가 존재하지 않습니다.")
    elif num == 9:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하였습니다.")
    print("-" * 10)