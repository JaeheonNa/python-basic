from calc import *

integer_1 = int(input("정수를 입력하세요."))
integer_2 = int(input("정수를 입력하세요."))

answer = get_max(integer_1, integer_2)
print("입력하신 정수", integer_1, "와", integer_2, "중 큰 값은", answer, "입니다.")

answer = get_min(integer_1, integer_2)
print("입력하신 정수", integer_1, "와", integer_2, "중 작은 값은", answer, "입니다.")

answer = power(integer_1, integer_2)
print(integer_1, "의", integer_2, "승은", answer, "입니다.")