stack_data = []
stack_data.append(10)
stack_data.append(20)
stack_data.append(30)
stack_data.append(40)
stack_data.append(50)
print(stack_data)
print(stack_data.pop())
print(stack_data.pop())
print(stack_data)

string = input("문자열을 입력하세요.")
string_list = list(string)
stack_string = []
for _ in range(len(string_list)):
    stack_string.append(string_list.pop())
print(stack_string)
