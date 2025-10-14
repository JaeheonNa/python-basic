# mutable 객체라고 하더라도, 함수 내에서 새로 할당하게 되면 참조 관계가 끊김. java의 new와 같은 동작.

def list_test(my_list):
    print("함수 내부에서의 my_list id:", id(my_list))
    my_list = [1, 2, 3, 4, 5]
    print("함수 내부에서 '할당 후' my_list id:", id(my_list))
    print("함수 내부에서 '할당 후' my_list:", my_list)
    return my_list

my_list = [100, 200, 300, 400, 500]
print("함수 외부에서의 my_list:", my_list)
print("함수 외부에서의 my_list id:", id(my_list))
list_test(my_list)
print("함수 외부에서의 my_list:", my_list)
print("함수 외부에서의 my_list id:", id(my_list))
