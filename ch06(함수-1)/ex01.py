import hello

hello.say_hello_name("나루")
hello.say_hello_name_msg("나루", "반가워")

def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

answer = get_sum(1, 10)
print(answer)

answer = get_sum(1, 30)
print(answer)

answer = get_sum(1, 100)
print(answer)