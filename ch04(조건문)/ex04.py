flag = True
print(type(flag))
print(flag)

flag = not flag
print(flag)

if flag :
    print("참")
else :
    print("거짓")
    flag = not flag

if flag :
    print("참")
else :
    print("거짓")