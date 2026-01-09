import random

def gen_password():
    password = ""
    for i in range(6):
        num = random.randint(0,9)
        password += str(num)
    password = password + " "
    return password

print(gen_password())