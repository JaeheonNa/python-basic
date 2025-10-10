num_list = []
for i in range(151):
    num_list.append(i)

prime_num_list = []
for i in range(2, 151):
    if num_list[i] != 0:
        prime_num_list.append(num_list[i])
        for j in range(2, 151):
            index = num_list[i] * j
            if index > 150:
                break
            num_list[index] = 0

answer = 0
last_num = 0
temp = 0
for i in prime_num_list:
    temp += i
    if temp > 2000:
        break
    answer += i
    last_num = i

print("2000보다 작은 최대 합: ", answer)
print("이 때, 가장 큰 소수: ", last_num)
