def square(number):
    return number * number

def get_max(number_1, number_2):
    if number_1 > number_2:
        return number_1
    else:
        return number_2

def get_min(number_1, number_2):
    if number_1 < number_2:
        return number_1
    else:
        return number_2

def power(x, y):
    answer = 1
    for i in range(y):
        answer *= x
    return answer