from collections import defaultdict

li1 = [('yellow', 1), ('blue', 2), ('red', 3), ('green', 4), ('blue', 5)]

dic1 = defaultdict(list)
for k, v in li1:
    dic1[k].append(v)

print(dic1)